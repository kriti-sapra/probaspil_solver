import re
import string
from utils_clist import CList

def make_encoder(baseString):
    size = len(baseString)
    d = {ch: i for (i, ch) in enumerate(baseString)}  # Map from char -> value

    if len(d) != size:
        raise Exception("Duplicate characters in encoding string")

    def encode(x):
        if x == 0:
            return baseString[0]  # Only needed if don't want '' for 0
        l = []
        while x > 0:
            l.append(baseString[x % size])
            x //= size  # Divide X by size and round to get next section to encode
        return ''.join(l)

    def decode(s):
        return sum(d[ch] * size ** i for (i, ch) in enumerate(s))

    return encode, decode


def get_outer_arguments(stri):
    """Given a string that represents an atom it returns a list of strings
    that contain all the arguments of the atom.

    All the spaces are deleted (except the one after a not).
    It ignores the final dot (it's ok with and without).
    """
    closingbracket = ')'
    s = re.sub(r'(?<!not)\s', '', stri)
    list_of_args = [""]
    bracketopen = False
    innerbracketopen = 0
    innersquarebracketopen = 0
    for c in s:
        if bracketopen:
            if innerbracketopen == 0 and innersquarebracketopen == 0:
                if c == closingbracket:
                    break
                if c == ',':
                    list_of_args.append("")
                else:
                    list_of_args[len(list_of_args) - 1] = list_of_args[len(list_of_args) - 1] + c
            else:
                list_of_args[len(list_of_args) - 1] = list_of_args[len(list_of_args) - 1] + c
            if c == '(':
                innerbracketopen += 1
            elif c == ')':
                innerbracketopen -= 1
            if c == '[':
                innersquarebracketopen += 1
            elif c == ']':
                innersquarebracketopen -= 1
        else:
            if c == '(':
                bracketopen = True
                closingbracket = ')'
            if c == '[':
                bracketopen = True
                closingbracket = ']'
    if list_of_args != [""]:
        return list_of_args
    else:
        return []


# CLASSES
# Provides new variables to use ensuring they are not repeated
class Variabiliser:
    """Used to keep track of variables. It runs through variables A, B, C, ... Z,
    AA, AB, ..., AZ, AAA...
    """
    currentindex = 0

    def get_new_variable(self):
        """Returns a variable and increments the internal counter.

        The variables start with "A" (when the counter is 0)
        """
        self.currentindex += 1
        return self.get_brand_new_variables(self.currentindex)[self.currentindex - 1]

    def get_new_variables(self, x):
        """Returns a variable and increments the internal counter.

        The variables start with "A" (when the counter is 0)
        """
        outs = []
        for i in range(int(x)):
            self.currentindex += 1
            outs.append(self.get_brand_new_variables(self.currentindex)[self.currentindex - 1])
        return outs

    def get_brand_new_variables(self, x):
        """Returns x variables but doesn't affect the counter.

        The variables start with "A"
        """
        ret = []
        letters = string.ascii_uppercase
        n = len(letters)
        for i in range(0, x):
            t = ''
            while i >= 0:
                t = t + letters[(i % n)]
                i -= n
            ret.append(t)
        return ret

    def __init__(self):
        self.currentindex = 0


class Atom:
    """Defines a Prolog element (not just atoms). It includes literals ('not atom' is treated like positive atoms)
    and variables.
    It also includes the case atoms have placemarkers +, - and #.

    The fields placemarkers is populated with a list of tuples [term, placemarker, type]
    e.g.  ['+bird', 'i', 'bird'],
    or after variabilisation ['C', 'i', 'bird'].
    """

    atom = ''  # Contains the current form of the atom as string
    predicate = ''  # Predicate
    arguments = []  # List of atoms
    placemarkers = ''  # List of tuples of the type ['+bird', 'i', 'bird'] or ['C', 'i', 'bird'],
    variabiliser = None

    def __init__(self, atom):
        """
        The constructor parses a line as it would be written in a learning file.
        It populates the fields atom, arguments and predicate. All the arguments
        are themselves atoms.
        """
        self.atom = re.sub(r'(?<!not)\s', '', atom)
        if len(self.atom) > 0 and self.atom[len(self.atom) - 1] == '.':
            # Trims the '.' from end of predicates
            self.atom = self.atom[:len(self.atom) - 1]
        self.arguments = self.__getArgs__()
        self.predicate = self.__getPredicate__()
        self.placemarkers = self.__getPlacemarkersList__()

    def __getPredicate__(self):
        a = self.atom.split('(', 1)
        return a[0]

    def __getArgs__(self):
        """
        It parses self.atom and creates an atom for each argument (each argument
        then is parsed recursively). It returns all such atoms.
        """
        outlist = []
        q = get_outer_arguments(self.atom)
        if len(q) > 0:
            for i in q:
                outlist.append(Atom(i))
        return outlist

    def __str__(self):
        return self.atom

    def __repr__(self):
        return self.__str__()

    def __getPlacemarkersList__(self):
        # Returns list of [predicate, i/o/c, type]
        args = self.arguments
        out = []
        if not len(args):
            if self.predicate.startswith('+'):
                [_, vartype] = self.predicate.split('+')
                return [[self.predicate, 'i', vartype]]
            elif self.predicate.startswith('-'):
                [_, vartype] = self.predicate.split('-')
                return [[self.predicate, 'o', vartype]]
            elif self.predicate.startswith('#'):
                [_, vartype] = self.predicate.split('#')
                return [[self.predicate, 'c', vartype]]
            else:
                return []
        else:
            for indexatom in range(len(args)):
                ans = args[indexatom].__getPlacemarkersList__()
                out.extend(ans)
            return out

    # See if atom contains any outputs
    def hasOutputs(self):
        args = self.arguments
        if not len(args):
            return self.predicate.startswith('-')
        else:
            for a in args:
                if a.hasOutputs():
                    return True
        return False

    def isVariable(self):
        return len(self.arguments)==0 and\
               (self.predicate[0].upper() == self.predicate[0]) and self.predicate[0].isalpha()

    def __variabiliseWV__(self, variabiliser):
        args = self.arguments
        outplacem = []
        # If there are multiple things to variablise then break them down first
        if not len(args):
            # Returns new variable and the appropriate new palcemarkers for it
            if self.predicate.startswith('+') and not str(self.predicate[1]).isdigit():
                v = variabiliser.get_new_variable()
                outplacem = [v, 'i', self.predicate[1:]]
                return [v, [outplacem]]
            elif self.predicate.startswith('-') and not str(self.predicate[1]).isdigit():
                v = variabiliser.get_new_variable()
                outplacem = [v, 'o', self.predicate[1:]]
                return [v, [outplacem]]
            elif self.predicate.startswith('#'):
                v = variabiliser.get_new_variable()
                outplacem = [v, 'c', self.predicate[1:]]
                return [v, [outplacem]]
            else:
                return [self.atom, []]
        else:
            returnstring = self.predicate+'('
            for indexatom in range(len(args)):
                ans = args[indexatom].__variabiliseWV__(variabiliser)
                if indexatom == len(args)-1:
                    returnstring+=ans[0]+')'
                else:
                    returnstring+=ans[0]+','
                outplacem.extend(ans[1])
            return  [returnstring, outplacem]

    def variabilise(self):
        """
        It has only effect on atoms that represent mode declarations.
        It updates the placemarkers and the atom. The placemarker list
        still keeps the old elements but substitutes the +-#something
        with a variable
        """
        if self.variabiliser is None:
            variabiliser = Variabiliser()
        else:
            variabiliser = self.variabiliser
        [r, pm] = self.__variabiliseWV__(variabiliser)
        self.atom=r
        self.placemarkers=pm
        self.arguments=self.__getArgs__()
        return r

    def getVariables(self):
        variables = []
        args = self.arguments
        if not len(args):
            if self.isVariable():
                return [self]
            else:
                return []
        else:
            for arg in args:
                variables.extend(arg.getVariables())
        return variables

    def getTypeVariables(self, type):
        """ Type is either 'i', 'o', 'c'
        """
        outputlist = []
        for varindex in range(len(self.placemarkers)):
            q = Atom(str(self.placemarkers[varindex][0]))
            if self.placemarkers[varindex][1] == type and q.isVariable():
                outputlist.append(self.placemarkers[varindex][0])
        return outputlist

    def getTypeConditions(self):
        """It returns a list of the type ['bird(A)', nat(B)...]
        """
        outputlist = []
        for i in range(len(self.placemarkers)):
            if Atom(str(self.placemarkers[i][0])).isVariable:
                outputlist.append(str(self.placemarkers[i][2]) + '(' + str(self.placemarkers[i][0]) + ')')
        return outputlist

    def getTypeConditionsForVariableType(self, type):
        """It returns a list of the type ['bird', nat...]
        for the given type. Type is either 'i', 'o', 'c'.
        """
        outputlist = []
        for i in range(len(self.placemarkers)):
            if self.placemarkers[i][1] == type and Atom(str(self.placemarkers[i][0])).isVariable:
                outputlist.append(str(self.placemarkers[i][2]))
        return outputlist

    def getTypeConditionsForVariableTypeComplete(self, type):
        """It returns a list of the type ['bird(A)', 'nat(B)'...]
        for the given type. Type is either 'i', 'o', 'c'.
        """
        outputlist = []
        for i in range(len(self.placemarkers)):
            if self.placemarkers[i][1] == type and Atom(str(self.placemarkers[i][0])).isVariable:
                outputlist.append(str(self.placemarkers[i][2]) + '(' + self.placemarkers[i][0] + ')')
        return outputlist

    def setVariabiliser(self, variabiliser):
        self.variabiliser = variabiliser

    def countPlacemarkers(self, type):
        count = 0
        for i in self.atom:
            if i == type:
                count += 1
        return count

    def __changeInputsFromList__(self, lis, ind, placemarkers, cindex):
        [ins, outs, cons] = lis
        [insind, outsind, consind] = ind
        #        er3 "__changeInputsFromList__(" + str(len(ins))+'#'+str(len(outs))+'#'+str(len(cons)) + "  -  " + str(ind) + "   -  "+str(placemarkers) + "  -> " + str(cindex)
        args = self.arguments
        nindexes = [insind, outsind, consind]
        placemlist = []
        ncindex = cindex
        if not len(args):
            if self.predicate.startswith('+'):
                v = ins[int(str(insind[0])) - 1]
                insind = insind[1:]
                return [v, [[v, placemarkers[cindex][1], placemarkers[cindex][2]]], [insind, outsind, consind],
                        cindex + 1]
            elif self.predicate.startswith('-'):
                v = outs[int(str(outsind[0])) - 1]
                outsind = outsind[1:]
                return [v, [[v, placemarkers[cindex][1], placemarkers[cindex][2]]], [insind, outsind, consind],
                        cindex + 1]
            elif self.predicate.startswith('#'):
                v = cons[int(str(consind[0])) - 1]
                consind = consind[1:]
                return [v, [[v, placemarkers[cindex][1], placemarkers[cindex][2]]], [insind, outsind, consind],
                        cindex + 1]
            else:
                return [self.atom, [], [insind, outsind, consind], cindex]
        else:
            returnstring = self.predicate + '('
            for indexatom in range(len(args)):
                ans = args[indexatom].__changeInputsFromList__([ins, outs, cons], nindexes, placemarkers, ncindex)
                nindexes = ans[2]
                ncindex = ans[3]
                placemlist.extend(ans[1])
                if indexatom == len(args) - 1:
                    returnstring += str(ans[0]) + ')'
                else:
                    returnstring += str(ans[0]) + ','
            return [returnstring, placemlist, nindexes, ncindex]

    def changeInputsFromList(self, list, indexes):
        """Given a list of variables or constants (ordered),
        a list of indexes referred to the list and a type 'i', 'o', 'c'
        it changes all the placemarkers with the corresponding element of the list.
        It returns the new atom, and updates the placemarkers
        """
        returnstring, placemlist, _, _ = self.__changeInputsFromList__(list, indexes, self.placemarkers, 0)
        self.atom=returnstring
        self.placemarkers=placemlist
        self.arguments=self.__getArgs__()
        return returnstring


class Clause:
    head = Atom('')
    body = []
    flattening = []
    constantflattening = []
    variabiliser = None
    outvars = []

    def __init__(self, head, body, variabiliser=None):
        """
        The head is a string or an atom, the body a list of strings or atoms
        """
        self.head = head
        self.body = body
        self.variabiliser = variabiliser
        self.flattening = []
        self.constantflattening = []
        self.outvars = []
        self.constraints = []
        self.producerlength = None
        self.outvarstypes = []

    def __str__(self):
        if len(self.body) > 0:
            s = str(self.head) + ':-\n'
            for i in range(len(self.body)):
                if i < len(self.body) - 1:
                    s += '\t' + str(self.body[i]) + ',\n'
                else:
                    s += '\t' + str(self.body[i]) + '.\n'
        else:
            s = '' + str(self.head) + '.'
        return s

    def __repr__(self):
        return self.toLineStr().replace('\n', '')

    def toLineStr(self):
        if len(self.body) > 0:
            s = str(self.head) + ':- '
            for i in range(len(self.body)):
                if i < len(self.body) - 1:
                    s += ' ' + str(self.body[i]) + ','
                else:
                    s += ' ' + str(self.body[i]) + '.\n'
        else:
            s = '' + str(self.head) + '.'
        return s

    def printAllInfo(self):
        out = ''
        out += self.toLineStr()

        out += '\nflattening:\n'
        out += str(self.flattening)

        out += '\nconstantflattening:\n'
        out += str(self.constantflattening)

        out += '\noutvars:\n'
        out += str(self.outvars)

        out += '\nconstraints:\n'
        out += str(self.constraints)

        out += '\nproducerlength:\n'
        out += str(self.producerlength)

        out += '\noutvarstypes:\n'
        out += str(self.outvarstypes)

        return out

    def addConstraint(self, bodystring):
        self.constraints.append(bodystring)

    def addConstraints(self, bodiestring):
        self.constraints.extend(bodiestring)

    def addCondition(self, bodystring):
        for i in self.body:
            if str(i) == str(bodystring):
                return
        self.body.append(bodystring)

    def addConditions(self, bodiestring):
        for i in bodiestring:
            self.addCondition(i)

    def addFlattening(self, flattening, constantFlattening=[]):
        self.flattening.append(flattening)
        self.constantflattening.extend(constantFlattening)

    def setVariabiliser(self, variabiliser):
        self.variabiliser = variabiliser

    def addOutputVariable(self, typedvariable):
        """typed variable is of the type ('V', 'type')
        """
        self.outvars.append(typedvariable)

    def getAbd(self):
        length = len(self.flattening)
        s = "rule(r("
        for e in self.flattening:
            s += str(e) + ","
        return s[0:-1] + "),{0})".format(length)

    def getComplexity(self):
        if len(self.flattening) > 1:
            return len(self.flattening)
        return 1 + len(self.body)


class ModeDeclaration(Atom):
    """Mode declaration. It defines a mode declaration thus it contains a type (h or b)
    a schema, and additional arguments (options and settings).

    Attributes:
      type: head (h) or body (b)
      schema: schema of the mode declaration
      options: contains a list of options and settings (not implemented yet)
    """

    type = ''
    schema = ''
    label = ''
    options = []

    def __init__(self, line):
        """
        The constructor parses a line as it would be written in a learning file
        """
        Atom.__init__(self, line)
        # we select the content (cut out modeh and last bracket and point)
        q = get_outer_arguments(line)
        # Trim starting digit or *
        if str(q[0]).isdigit():
            self.options = ["o(max, {0})".format(str(q[0]))]
            q = q[1:]
        elif str(q[0]) == '*':
            q = q[1:]

        # Predicates and their arguments
        self.schema = q[0]
        if len(q) == 2:
            self.options = get_outer_arguments(q[1])
        else:
            self.options = []

        # Identify the type
        if line[:5] == 'modeh':
            self.type = 'h'
        elif self.hasOutputs():
            self.type = 'p'
        else:
            self.type = 'c'

        # Encode the string as a number and give it a label
        encode, _ = make_encoder("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
        l = encode(int((self.atom.__hash__() % 10000)))
        self.label = 'id' + self.schema[0:2] + str(l)

    def __str__(self):
        return 'mode{}({})'.format(self.type, self.schema)

    # Count particular instances of a given type in a mode bias
    def counttype(self, type):
        num = 0
        if type == 'i':
            char = '+'
        elif type == 'o':
            char = '-'
        else:
            char = '#'
        for c in self.schema:
            if c == char:
                num += 1
        return num

    # E.g. Get Max Value TODO: Check other options?
    def getOption(self, option):
        for o in self.options:
            ao = Atom(o)
            if str(ao.arguments[0]) == option:
                return ao.arguments[1]
            else:
                return None

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.label == other.label

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.label < other.label

    def __le__(self, other):
        return NotImplemented

    def __gt__(self, other):
        return self.label > other.label

    def __ge__(self, other):
        return NotImplemented

class Flatatom:
    mode = ''
    links = []
    constants = []

    def __init__(self, mode, constants, links=None):
        self.mode = mode
        self.links = links
        self.constants = constants

    def __str__(self):
        c = CList(self.constants)
        l = CList(self.links)
        return "({0},{1},{2})".format(self.mode, c.toTypedString('c'), l.toTypedString('l'))

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (self.mode == other.mode and self.links == other.links)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return (self.mode < other.mode) or (self.mode == other.mode and self.links < other.links)

    def __le__(self, other):
        return NotImplemented

    def __gt__(self, other):
        return (self.mode > other.mode) or (self.mode == other.mode and self.links > other.links)

    def __ge__(self, other):
        return NotImplemented