import os
import time
import copy
import logging
from utils_probaspil import *
from utils_logic_program import *
from utils_clist import CList
import clingo
from itertools import chain, combinations
import argparse

DEFAULT_FILE = 'experiments/smokes.lp'
BASE_PATH = '/Users/kritisapra/Desktop/Imperial/Fourth_Year/prob_aspal'
#BASE_PATH = '/home/kriti/Desktop/FYP/prob_aspal_solver'
LOG_FILENAME = BASE_PATH + '/tmp/aspal.log'

SOLVER = ''
# FILENAME = DEFAULT_FILE

om = HumanOutputWrapper()


# LOGGER SETUP
def ensure_dir(f):
    """f is a filename. If f's directory doesn't exist, it's created.
    """
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)


# set up logging to file
def setup_logger():
    ensure_dir(LOG_FILENAME)
    filename = BASE_PATH + '/tmp/aspal.log'

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename=filename,
                        filemode='w')
    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()

    q = logging.INFO
    console.setLevel(q)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(message)s\n')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)


setup_logger()


def print_task():
    om.toOut("Max rules: " + str(MAX_RULES))
    om.toOut("Max conditions: " + str(MAX_CONDITIONS))
    om.toOut("Max producers: " + str(MAX_PRODUCERS))
    om.toOut("Max consumers: " + str(MAX_CONSUMERS))
    om.toOut("Epsilon: " + str(EPSILON))
    om.toOut("Window: " + str(WINDOW))
    om.toOut("Max Hypothesis Length: " + str(MAX_HYP_LEN))


# PREPROCESSING FILE
def cartesianProduct(elements):
    if elements == []:
        return []
    outlist = []
    head = elements[0]
    t = elements[1:]
    # Recurse into the tail of the elements
    restCartesian = cartesianProduct(t)
    for e in head:
        # The tail was empty so add head to list
        if restCartesian == []:
            outlist.append([e])
        # Append each item to outlist
        for et in restCartesian:
            liste = [e]
            liste.extend(et)
            outlist.append(liste)
    return outlist


# Compare two flat atoms
def getConstantComparison(flatatom1, flatatom2, consumer):
    if consumer == False:
        comparison = "<="
    else:
        comparison = "<"
    a = CList(flatatom1.constants)
    b = CList(flatatom2.constants)
    # As long as both atoms have constants, compare them
    if len(a) > 0 and len(b) > 0:
        return "{0} {2} {1}".format(a.toTypedString('c'), b.toTypedString('c'), comparison)
    return False


# Creates a rule body with all the constant types
def typingformat(cnstlist):
    if cnstlist == []:
        return ''
    out = " :-"
    for c in cnstlist:
        # Adds constants in rule separated by :
        out += c + ", "
    return out[0:-2]


# Make head of rules:
def makeHead(modedec, variabiliser):
    """It returns a list of clauses of strings that go
    into the final top theory
    """

    # Gathers variables and typechecks
    head = Atom(modedec.schema)
    # Assigns a Variablisier to the head atom in order to get unique variable names
    head.setVariabiliser(variabiliser)
    # Updates the atom label and placemarker list by replacing any arguments with new variables.
    head.variabilise()
    # Returns the id assigned to the mode dec
    mname = modedec.label

    logging.debug('Anything in here? ' + str(head))

    # Returns the constant variables in the head
    constantvars = CList(head.getTypeVariables('c'))
    logging.debug("Const vars: {}".format(constantvars))
    # Returns the type of the constants, e.g. day(A)
    constanttypeconds = CList(head.getTypeConditionsForVariableTypeComplete('c'))
    logging.debug("CONST TYPE: {}".format(constanttypeconds))
    # Gets the input variables in the head and the number of input variables
    inputvars = CList(head.getTypeVariables('i'))
    inputnum = len(inputvars)
    # Gets the type of the input variables in the head, e.g. day(A)
    inputtypeconds = CList(head.getTypeConditionsForVariableType('i'))
    # Gets all typed conditions for the head
    typeconds = CList(head.getTypeConditions(), 'empty')
    logging.debug("TYPE SECONDS: {}".format(typeconds))

    # Builds the clause
    # Creates a clause with an empty body and just the variablised head
    returned_clause = Clause(head=str(head), body=[], variabiliser=variabiliser)
    logging.debug("CLAUSE: {}".format(returned_clause))
    # Adds Flattening to the clause by providing the id for the head and any constants in the atom
    returned_clause.addFlattening(Flatatom(mname, constantvars), constantFlattening=constanttypeconds)
    # Adds the types of the variables into the body of the clause to make it safe.
    returned_clause.addConditions(typeconds)

    # Records how many input variables there are as needed for output later
    returned_clause.totouts = inputnum
    returned_clause.lastconditionouts = inputnum

    for i in range(inputnum):
        # Add each input variable and its type to the output variables of the clause
        returned_clause.addOutputVariable((inputvars[i], inputtypeconds[i]))

    declarations = []
    return returned_clause, declarations


# Check ordering of rule given a flatatom
def orderSatisfied(rule, newflat, consumer=False):
    # Gets the outputs of the rule
    newouts = rule.lastconditionouts
    oldouts = rule.totouts

    if consumer == False:
        logging.debug("Checking variable use: totvar=" + str(oldouts) + ", lastvar=" + str(newouts))
        for l in newflat.links:
            # Check the links are more than the difference in outputs
            if l > oldouts - newouts:
                return True
    # If there is a consumer then check ordering for the last item in list
    q = rule.flattening[-1]
    logging.debug("Checking ordering " + str(q) + " < " + str(newflat))
    if q < newflat:
        return True
    elif q == newflat:
        logging.debug("Exactly same condition, constants?")
        additionalconditions = getConstantComparison(q, newflat, consumer)
        # We cannot compare the constants because they are not ground
        # So we add a condition to the rule
        logging.debug("Additional conditions: " + str(additionalconditions))
        if additionalconditions:
            # If not False return them
            return additionalconditions
        else:
            # They are the same and the constants cannot be ordered (empty)
            return not consumer
    return False


# Find bindings of output variables given a condition
def findBindings(outvars, condition):
    """outvars are typed  ('V', 'type')
    Returns a set of elements [  (['A = B', 'C = O'], [2, 3]), .... ]
    """
    logging.debug('Finding bindings')
    logging.debug("Available variables: " + str(outvars))
    logging.debug("Condition to bind: " + str(condition))
    localbindings = []
    # Gets input variables and their types
    ivars = condition.getTypeVariables('i')
    itypes = condition.getTypeConditionsForVariableType('i')

    for i in range(len(ivars)):
        # ways contains all the binding for THIS input variable
        ways = []
        # Binds output variables to the current input variable if their types match
        for j in range(len(outvars)):
            logging.debug('now' + str(outvars[j]))
            ovar, otype = outvars[j]
            logging.debug('input is' + itypes[i] + ivars[i])
            # If type of input matches the type of output, say they must be equal
            if itypes[i] == otype:
                ways.append(('{0}={1}'.format(ovar, ivars[i]), j + 1))
        if len(ways) > 0:
            # localbindings should contain one entry (a list of possible
            # bindings) for each input
            localbindings.append(ways)
        else:
            # if one input has no bindings we fail
            return []

    outbindings = cartesianProduct(localbindings)
    return outbindings


# Extend the rule with the given mode declaration
def extendRuleWithCondition(rule, modedec, iter=0):
    """It returns a set of partial bodies (including the flattening
    that adds up to the current clause) and declarations
    """
    # Finds the condition, adds the variabliser and assigns variables to the atoms
    condition = Atom(modedec.schema)
    condition.setVariabiliser(rule.variabiliser)
    condition.variabilise()
    mname = modedec.label

    # Gets all constant variables
    constantvars = CList(condition.getTypeVariables('c'))
    # Gets all output variables
    outputvars = CList(condition.getTypeVariables('o'))
    # Gets total number of output variables
    outputnum = len(outputvars)
    # Gets types of constants, outputs and all types in the condition
    constanttypeconds = CList(condition.getTypeConditionsForVariableTypeComplete('c'), 'empty')
    outputtypeconds = CList(condition.getTypeConditionsForVariableType('o'))
    typeconds = CList(condition.getTypeConditions(), 'empty')
    type = modedec.type

    # Builds the clause
    # Finds bindings for the inputs and the outputs in the rule
    bindingsandlinklist = findBindings(rule.outvars, condition)
    # If no bindings exist then no new rules created
    if bindingsandlinklist == []:
        return []

    outrules = []

    # Iterate over all bindings
    for bindingelement in bindingsandlinklist:
        # A new rule for each binding to not edit the original
        newrule = copy.deepcopy(rule)
        allinks = []
        # Add new condition to the rule and append the link
        for (b, l) in bindingelement:
            newrule.addCondition(b)
            allinks.append(l)
        # Creates a new flat atom with the id of the modedec, any constants in the mode dec and all links
        newflat = Flatatom(mname, constantvars, allinks)
        if type == 'p':
            orderSat = orderSatisfied(rule, newflat)
        elif iter > 1:
            orderSat = orderSatisfied(rule, newflat, consumer=True)
        else:
            orderSat = True
        if orderSat:
            # Add the type constraints of the condition to the new rule
            newrule.addConditions(typeconds)
            # Add the condition to the rule
            newrule.addCondition(str(condition))
            for i in range(len(outputvars)):
                # Add output variables to the new rule
                newrule.addOutputVariable((outputvars[i], outputtypeconds[i]))
            # Add flattening to the new rule
            newrule.addFlattening(newflat, constantFlattening=constanttypeconds)
            # Increase the number of output variables of rule
            newrule.totouts += outputnum
            newrule.lastconditionouts = outputnum

            # orderSat is a string then add it as a constraint
            if isinstance(orderSat, str):
                newrule.addConstraint(orderSat)

            # add new rule to the output rules
            outrules.append(newrule)

    return outrules


# Grow a rule that has output variables with a given modedec
def growConsumer(rule, modedec):
    outrules = []
    outrules.append(rule)

    logging.debug('#Adding consumer {}'.format(modedec))
    logging.debug('#Flattening of the rule')
    for f in rule.flattening:
        logging.debug('#' + str(f))
    max_mode = None
    # Get the max option of the modedec if it exists
    if modedec.getOption('max'):
        max_mode = int(str(modedec.getOption('max')))
    # Calculate the length of the consumer and the rule length
    consumerlength = len(rule.flattening) - rule.producerlength
    rule_length = len(rule.flattening)
    logging.debug('#Consumer length ' + str(consumerlength))

    iter = 1
    if not max_mode:
        max_mode = MAX_CONSUMERS
    # We do as many iteration as the instances of the modedec we can add
    newRules = [rule]
    while consumerlength < MAX_CONSUMERS and iter <= max_mode and rule_length <= MAX_CONDITIONS:
        # In onw instance we get all the rules that we have (one in the first iteration)
        # In each of these iteration we act on the last produced set
        logging.debug('##Iteration ' + str(iter))
        nextRules = []
        for r in newRules:
            logging.debug('###Extending ' + str(r))
            # Create a deep copy of the rule so you do not edit the original one
            copyrule = copy.deepcopy(r)
            logging.debug("COPY RULE : {}".format(copyrule))
            # Extend the copied rule with the body atom of the mode dec
            here = extendRuleWithCondition(copyrule, modedec, iter=iter)
            # Add all the new rules to the next rules
            nextRules.extend(here)
            logging.debug('###Got {0} new rules'.format(len(here)))
            # Note that we keep the old rule
        logging.debug('##Got a total of {0} new rules:'.format(len(nextRules)))
        for r in nextRules:
            logging.debug(r)
        # Add the extended rules to the output rules
        outrules.extend(nextRules)
        newRules = nextRules
        # Update the interation to stop as required
        iter += 1
        consumerlength += 1
        rule_length += 1
    return outrules


# Grow the rules with modep declarations
def grow(rule, modedecs):
    outrules = []
    outrules.append(rule)

    logging.debug('Flattening of the rule')

    for f in rule.flattening:
        logging.debug(str(f))

    # Grow rule as long as the flattening is less than the producers and the maximum conditions
    if len(rule.flattening) <= 10 and len(rule.flattening) <= 5:
        # Iterate over all possible mode declarations
        for m in modedecs:
            # If it is a predicate and has an output
            if m.type == 'p':
                max_mode = False
                # If it has max options
                if m.getOption('max'):
                    max_mode = int(str(m.getOption('max')))
                pcount = 0
                for q in rule.flattening:
                    # If flat atom matches the label of the mode declaration
                    if q.mode == m.label:
                        pcount += 1

                logging.debug("Evaluating extension with " + str(m))
                newrules = []
                if (max_mode and max_mode) < 1 or not max_mode or (max_mode and pcount < max_mode):
                    # Get new rule that has been extended with predicates that contain outputs
                    newrules = extendRuleWithCondition(rule, m)
                logging.debug("Extended in {0} new rules".format(str(len(newrules))))
                if newrules:
                    for rulen in newrules:
                        logging.debug(rulen)
                        # Grow the rule further with the modedecs
                        addrules = grow(rulen, modedecs)
                        outrules.extend(addrules)
    # Return all rules once you have grown them
    return outrules


# Turn into ModeDeclaration Objects
def createModeDecs(modedecs):
    q = []
    for line in modedecs:
        m = ModeDeclaration(line)
        q.append(m)
    return q


def read(filename, asstring=False):
    """
    Reads filename and returns either a list (asstring = True) or a string.
    """
    if asstring:
        lines = ''
    else:
        lines = []
    try:
        file = open(filename, 'r')
        for line in file:
            nline = re.sub(r'(?<!not)\s', '', line)
            if asstring:
                lines += nline + '\n'
            else:
                lines.append(nline)
        file.close()
    except IOError:
        print("The file does not exist")
    return lines


def parse_file(filename):
    """Given a path to a file, it returns a list
        [modedecs, prob_facts, examples, background].
        The list contains trimmed lines from the file
        (no syntax check).
        """
    modedecs = []
    prob_facts = []
    examples = []
    background = ""
    filetext = read(filename)
    for line in filetext:
        if line.startswith("mode"):
            modedecs.append(line)
        elif line.replace(' ', '').startswith(":-mode"):
            modedecs.append(line.replace(':-', ''))
        elif line.startswith("example("):
            examples.append(line)
        elif line.startswith("pf("):
            prob_facts.append(line)
        elif not line.startswith("%"):
            background = background + line + '\n'

    return [modedecs, prob_facts, examples, background]


def createTop(modedecs):
    rules = []
    finalrules = []
    modedecs.sort()
    for mode in modedecs:
        if mode.type == 'h':
            vrb = Variabiliser()
            logging.debug('Making head for modedec: ' + str(mode))
            top, _ = makeHead(mode, vrb)
            #            declarations.extend(declaration)
            logging.debug('Head ready: ' + str(top) + ' with flattening ' + str(top.flattening))
            rules.append(top)
    logging.debug('Head processed, now expanding the rules')

    for rule in rules:
        # Careful, do not modify the original rule but make a copy
        logging.debug('Extending rule: ' + str(rule))
        alltherules = grow(rule, modedecs)
        finalrules.extend(alltherules)

    for m in modedecs:
        # Grow rules with modeb instances that do not have outputs
        if m.type == 'c':
            # DEBUG
            logging.debug(">>>Now considering mode " + str(m))
            logging.debug(">>>On the following rules ")
            for r in finalrules:
                logging.debug(r.toLineStr())

            newrules = []
            for rule in finalrules:
                logging.debug("Processing" + rule.toLineStr())
                if rule.producerlength is None:
                    rule.producerlength = len(rule.flattening)
                newm = growConsumer(rule, m)
                newrules.extend(newm)

            # DEBUG
            logging.debug(">>>Now the new rules are ")
            for r in newrules:
                logging.debug(r.toLineStr())

            finalrules = newrules

    for r in finalrules:
        logging.debug("Final rule: {}".format(r))

    # For each rule in the final rules, get it's abducible and weight
    for rule in finalrules:
        # Get abducible
        abd = rule.getAbd()
        # Add the abducible to the rule
        rule.addCondition(abd)

    return finalrules


# Process probabilistic facts and examples
def process_inputs(inputs, delim=''):
    out = {}
    for p in inputs:
        args = get_outer_arguments(p)
        assert len(args) == 2
        if delim == 'pf':
            key = args[0] + '. '
        else:
            key = args[0]
        out[key] = float(args[1])
    return out


# Function that creates rule abducibles with any constants already included by running a preprocessing clingo step
def create_abds_with_constants(rules, filename, background):
    logging.debug("Starting to ground rule abducibles with constants")

    # Create temporary file which only includes the background
    finalfile = ''
    finalfile += background

    new_weights = {}
    constant_flattening_required = False

    # Traverse rules. If they require constant flattening then add a rule to get constant flattened abducibles into
    # temp file. If they do not require constant flattening, add them as is to new weights.
    for r in rules:
        rule_abd = r.getAbd()
        if r.constantflattening:
            constant_flattening_required = True
            temp_rule = rule_abd + typingformat(r.constantflattening) + '. \n'
            logging.debug("Temp rule formed: {}".format(temp_rule))
            finalfile += temp_rule
        else:
            # The constants do not need to be flattened so you add the abducible to new weights without change
            args = get_outer_arguments(rule_abd)
            rule_abd += '.'
            new_weights[rule_abd] = int(args[1])

    if constant_flattening_required:
        # Create temporary file and write background and grounding rules for abducibles
        logging.debug("Writing to temporary file for grounding abducibles")
        tempfile = BASE_PATH + "/tmp/wk_get_ground_abds_" + \
                   filename.split("/")[-1]
        ensure_dir(tempfile)
        f = open(tempfile, 'w')
        f.write(finalfile)
        f.close()
        logging.debug('Temporary file for grounding constant abducibles in %s' % tempfile)

        # Run clingo on this temporary file to get all possible groundings of the abducibles
        logging.debug("Running clingo to find ground abducibles.")
        ctrl = clingo.Control(["0", "--warn=none"])
        ctrl.load(tempfile)
        ctrl.ground([("base", [])])

        # Solve the program and get all models
        models = get_models(control=ctrl)

        # For each model, get the grounded rule abducibles and add them to the new weights
        logging.debug("Retrieving ground abdcuible facts from answer set")
        for m in models:
            for fact in m:
                fact = str(fact)
                if 'rule' in fact:
                    new_rule_abd = fact + '.'
                    args = get_outer_arguments(fact)
                    new_weights[new_rule_abd] = int(args[1])

    return new_weights


def process_file(filename):
    logging.debug("Filename: {}".format(filename))
    [modedecs, prob_facts, examples, background] = parse_file(filename)
    logging.debug('File parsed successfully')
    # Creates mode declarations (with type and label)
    fullmodedecs = createModeDecs(modedecs)
    logging.debug('Starting creation of the top theory')
    top = createTop(fullmodedecs)
    logging.debug('Top theory created')

    const_flattened_weights = create_abds_with_constants(rules=top, filename=filename, background=background)

    logging.debug('Starting processing probabilistic facts')
    pfs = process_inputs(prob_facts, 'pf')
    logging.debug('Probabilistic Facts Processed')

    logging.debug('Starting processing examples')
    exs = process_inputs(examples, 'example')
    logging.debug('Examples Processed')

    finalfile = ''

    finalfile += background

    for r in top:
        finalfile += str(r)

    tempfile = BASE_PATH + "/tmp/wk_" + filename.split("/")[-1]
    ensure_dir(tempfile)
    f = open(tempfile, 'w')
    f.write(finalfile)
    f.close()
    logging.debug('Temporary file created in %s' % tempfile)

    return tempfile, const_flattened_weights, fullmodedecs, pfs, exs


# Post Processing
def getElementsNoEmpty(atom):
    if len(atom.arguments) > 0:
        return atom.arguments
    else:
        return []


def transform_rule(r, modedecs):
    outputlist = []
    # r is of the type rule(l((h0,const(empty),links(empty)),(b2,const(empty),links(2))),  (0,  (bx0,const(empty),links(1)), 0))

    lmodedecs = dict()
    # Map the id strings of the modedec to the modedec
    for m in modedecs:
        lmodedecs[m.label] = m

    # Turn the rule into an atom
    q = Atom(r)
    # Extract the internal argument of the rule
    rest = q.arguments[0]  # (0,  (bx0,const(empty),links(1)), 0)
    # Get the arguments of the rule
    flattenedlist = rest.arguments

    # Separate the body and head arguments
    bodyargs = flattenedlist[1:]
    headarg = flattenedlist[0]

    # Create a new variabiliser
    allvars = Variabiliser()
    # Process the head argument

    # Get the id of the head atom
    i = headarg.arguments[0]
    # Get the predicate of the head atom
    modename = i.predicate
    # Get any constants in the head
    constants = getElementsNoEmpty(headarg.arguments[1])
    # Create a new head atom with the schema of the modeh
    headschema = Atom(lmodedecs[str(modename)].schema)
    # Get new variables for any input variables in the head
    clistins = allvars.get_new_variables(headschema.countPlacemarkers('+'))
    # Get new variables for any output variables in the head
    clistouts = allvars.get_new_variables(headschema.countPlacemarkers('-'))
    # Changes all the placemarkers with a corresponding variable
    headschema.changeInputsFromList([clistins, clistouts, constants],
                                    [range(1, len(clistins) + 1), range(1, len(clistouts) + 1),
                                     range(1, len(constants) + 1)])
    vatom = headschema
    # Add any input variables to the output list
    outputlist.extend(vatom.getTypeVariables('i'))
    # Initialise a new clause
    outclause = Clause(vatom, [])
    # Add the head argument to the rule
    outclause.addFlattening(headarg)
    # Add all input variables to the head atom as potential output variables in the clause
    outclause.outvars.extend(clistins)
    # Extend the types of the potential output variables in the clause to include types of input variables in head
    outclause.outvarstypes.extend(headschema.getTypeConditionsForVariableType('i'))
    # Extend the clause by adding types of input and output variables to ensure safety
    outclause.addConditions(vatom.getTypeConditionsForVariableTypeComplete('i'))
    outclause.addConditions(vatom.getTypeConditionsForVariableTypeComplete('o'))
    # outclauselist.extend(types) #these are string
    # Process the body
    for i in bodyargs:
        # Get modename of the body argument
        modename = i.arguments[0].predicate
        # Create a new atom with the schema of the modeb
        schema = Atom(lmodedecs[str(modename)].schema)
        # Get the constants and links in the body predicate
        constants = getElementsNoEmpty(i.arguments[1])
        links = getElementsNoEmpty(i.arguments[2])
        # Get new variables for all the output variables in the body atom
        clistouts = allvars.get_new_variables(schema.countPlacemarkers('-'))
        # Changes all the placemarkers with a corresponding variable
        schema.changeInputsFromList([outputlist, clistouts, constants],
                                    [links, range(1, len(clistouts) + 1), range(1, len(constants) + 1)])
        vatom = schema
        # Extend the output list with any output type variables of the new body atom
        outputlist.extend(vatom.getTypeVariables('o'))
        # Extend the clause with the condition of the modeb
        outclause.addCondition(vatom)
        # Add any flattening from the body condition
        outclause.addFlattening(i)
        # Extend the output variables with any outputs from the current modeb
        outclause.outvars.extend(clistouts)
        # Extend the output tupe variables with any outputs from the modeb
        outclause.outvarstypes.extend(schema.getTypeConditionsForVariableType('o'))
        # Add type conditions for input and output variables of the inputs and outputs of the modeb
        outclause.addConditions(vatom.getTypeConditionsForVariableTypeComplete('i'))
        outclause.addConditions(vatom.getTypeConditionsForVariableTypeComplete('o'))
    return outclause


# Execution Helpers
# Calculates the probability of a total choice using distribution semantics
def prob(total_choice, probabilistic_facts):
    probability = 1
    for pf in probabilistic_facts:
        if pf in total_choice:
            probability *= probabilistic_facts[pf]
        else:
            probability *= (1 - probabilistic_facts[pf])
    return probability


# Calculates the length of a hypothesis
def hyp_len(hypothesis, rule_lengths):
    length = 0
    for h in hypothesis:
        length += rule_lengths[h]
    return length


# Creates a powerset of iterable and calculates their values given a function
def get_powerset_for_hypotheses(iterable):
    s = list(iterable.keys())
    ps = chain.from_iterable(combinations(s, r) for r in range(MAX_RULES + 1))

    return {''.join(s): hyp_len(s, iterable) for s in ps}


def get_total_choices_with_probs(iterable):
    s = list(iterable.keys())
    ps = chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
    return {''.join(s): prob(s, iterable) for s in ps}


# Get all models of a clingo run
def get_models(control):
    models = []
    with control.solve(yield_=True) as handle:
        for m in handle:
            models.append(m.symbols(atoms=True))
    return models


def check_models_for_examples(actual, models, tc_probability):
    for m in models:
        model = str(m)
        for e in actual:
            if e in model:
                actual[e] += tc_probability


def l_mse(expected, actual):
    score = 0
    for e in expected:
        score += pow((expected[e] - actual[e]), 2)
    return (1 / len(expected)) * score


# Calculate loss of hypothesis of 1 - acc
def accuracy(expected, actual):
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0
    for e in expected:
        pos = expected[e]
        posh = actual[e]
        neg = 1 - pos
        negh = 1 - posh
        tp = min(pos, posh)
        tn = min(neg, negh)
        fp = max(0, neg - tn)
        fn = max(0, pos - tp)
        true_positive += tp
        true_negative += tn
        false_positive += fp
        false_negative += fn
        # TODO: Normalise? Maybe use TP + TN / |E|
    return (true_positive + true_negative) / len(expected)


def alt_h_score(h_len, h_loss, a):
    return (h_len * a) + h_loss


# def alt_h_score(h_len, h_loss, a):
#     return ((h_len * a) * 0.2) + (h_loss * 0.8)


# Execute Clingo to check solutions
def execute(filename, rule_weights, modedecs, prob_facts, examples, loss_func=accuracy):
    # proc = subprocess.Popen(SOLVER + ' < ' + file, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    solutions = {}
    bestsolution = set()
    bestsolutionlen = None
    # Set best coverage to be negative to start with
    best_coverage = -1

    logging.debug("Starting to make hypotheses.")
    hypotheses = get_powerset_for_hypotheses(rule_weights)
    # Sort hypotheses by length
    sorted_h = sorted(hypotheses.items(), key=lambda x: x[1])
    logging.debug("Hypotheses made!")
    filtered_h = [(k, v) for k, v in sorted_h if v <= MAX_HYP_LEN]

    logging.debug("Starting to make total choices.")
    total_choices = get_total_choices_with_probs(prob_facts)
    logging.debug("Total choices made.")

    # Traverse hypotheses with shortest first
    total_traversals = 0
    for (h, n) in filtered_h:
        # logging.debug("H: {}, LENGTH: {}".format(h, n))
        # Examples you are trying to reach
        prob_examples_h = {e: 0 for e in examples}
        # logging.debug("Hypothesis: {}".format(h))
        total_traversals += 1
        for tc in total_choices:
            logging.debug("Hypothesis: {}, TC: {}".format(h, tc))
            # Create a Control object that will unify models against the appropriate
            # predicates. Then load the asp file that encodes the problem domain.

            ctrl = clingo.Control(["0", "--warn=none"])
            ctrl.load(filename)

            # Add facts as required and ground the program
            instance = h + tc
            ctrl.add("base", [], instance)
            ctrl.ground([("base", [])])

            # Solve the program and get all models
            models = get_models(control=ctrl)

            # Calculate probability for each example given the hypothesis by adding the probability of the current
            # total choice
            check_models_for_examples(actual=prob_examples_h, models=models,
                                      tc_probability=total_choices[tc])

        # Calculate loss and score of the hypothesis
        coverage = loss_func(expected=examples, actual=prob_examples_h)
        # logging.debug("Hypothesis: {} Score: {}".format(h, coverage))
        # If the coverage of the same length hypothesis is better then update best solutions accordingly
        if best_coverage <= coverage:
            # Reset current solution to avoid duplicates and contamination

            currentsolution = set()
            # Get individual rule abducibles from the hypothesis
            rule_abs = h.split(".")
            for r in rule_abs:
                # Remove any whitespace
                r = r.strip()
                # Check if there are no abducibles/last element of rule_abs, cannot transform empty string
                if r != '':
                    currentclause = transform_rule(r, modedecs)
                    line_rep = currentclause.toLineStr()
                    # Add the line representation of the rule to the current solution
                    currentsolution.add(line_rep)  # TODO: Make this make rules instead of abducibles
            # print("HYpothesis: {}, Score: {:0.4f}, LEN: {}".format(str(currentsolution), coverage, hypotheses[h]))
            if bestsolutionlen == n and best_coverage == coverage:
                # If the coverage is the same as best coverage and the same length then you add the hypothesis to best solutions
                bestsolution.add(frozenset(currentsolution))

            elif best_coverage < coverage:
                # If the coverage is more than currenty best coverage, then the best solution set has to be cleared
                best_coverage = coverage
                bestsolutionlen = n
                bestsolution.clear()
                bestsolution.add(frozenset(currentsolution))

        elif n <= bestsolutionlen + WINDOW:
            continue
        else:
            break

    print("Total Traversals: {}".format(total_traversals))
    # Return all the solutions, the best solutions and the best score
    return solutions, bestsolution, best_coverage


def find_solutions(file):
    om.toOut('Finding Solutions', size=2)

    filename, weights, modedecs, pfs, exs = process_file(file)
    om.toOut('Successfully processed {}. Now starting the solver'.format(filename))
    om.toOut('Invoking {}'.format(SOLVER))
    solutionshere, bestsolutionhere, bestscorehere = execute(filename=filename, rule_weights=weights, modedecs=modedecs,
                                                             prob_facts=pfs, examples=exs)
    return solutionshere, bestsolutionhere, bestscorehere


def main(filename):
    om.toOut('Executing ASPAL on file %s using solver %s.\nDebug logs in %s' % \
             (filename, SOLVER, LOG_FILENAME), type='info')
    print_task()
    start = time.perf_counter()
    solutions, bestsolution, bestscore = find_solutions(file=filename)
    end = time.perf_counter()
    time_taken = end - start
    print_solutions(solutions, bestsolution, bestscore, time_taken)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Processing probabilistic rule learning task')
    parser.add_argument("-mr", "--max_rules", dest='max_rules', help="Max Rules", type=int)
    parser.add_argument("-mc", "--max_conditions", dest='max_conditions', help="Max Conditions", type=int)
    parser.add_argument("-mp", "--max_producers", dest='max_producers', help="Max Producers", type=int)
    parser.add_argument("-mcons", "--max_consumers", dest='max_consumers', help="Max Consumers", type=int)
    parser.add_argument("-w", "--window", dest='window', help="Window", type=int)
    parser.add_argument("-mh", "--max_hyp", dest='max_hyp_len', help="Max Hypothesis Length", type=int)
    parser.add_argument("-f", dest='filename',
                        help="Input file for solver", metavar="FILE")
    args = parser.parse_args()

    # PARAMETERS
    MAX_PRODUCERS = args.max_producers if args.max_producers is not None else 10
    MAX_CONSUMERS = args.max_consumers if args.max_consumers is not None else 10
    FILENAME = args.filename if args.filename is not None else DEFAULT_FILE
    MAX_RULES = args.max_rules if args.max_rules is not None else 5
    MAX_CONDITIONS = args.max_conditions if args.max_conditions is not None else 5
    WINDOW = args.window if args.window is not None else 5
    MAX_HYP_LEN = args.max_hyp_len if args.max_hyp_len is not None else 20

    main(FILENAME)
