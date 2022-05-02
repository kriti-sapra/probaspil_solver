import sys
import time
import logging
from prob_utils import *
import clingo

om = HumanOutputWrapper()
LOG_FILENAME = '//Users/kritisapra/Desktop/Imperial/Fourth_Year/prob_aspal/fastlas_implementations/temp/prob_aspal.log'
DEFAULT_LOGIC_FILE = '/Users/kritisapra/Desktop/Imperial/Fourth_Year/prob_aspal/fastlas_implementations/temp/prob_background_input.lp'
DEFAULT_RULE_FILE = '/Users/kritisapra/Desktop/Imperial/Fourth_Year/prob_aspal/fastlas_implementations/temp/fastlas_output_rules.txt'
MAX_RULES = 10
EPSILON = 1.0


# set up logging to file
def setup_logger():
    ensure_dir(LOG_FILENAME)

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename='/Users/kritisapra/Desktop/Imperial/Fourth_Year/prob_aspal/tmp/aspal.log',
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


# Find solutions
def parse_logic_file(filename):
    """Given a path to a file, it returns a list
        [prob_facts, examples, background].
        The list contains trimmed lines from the file
        (no syntax check).
        """
    prob_facts = []
    examples = []
    background = ""
    filetext = read(filename)
    for line in filetext:
        if line.startswith("example("):
            examples.append(line)
        elif line.startswith("pf("):
            prob_facts.append(line)
        elif not line.startswith("%"):
            background = background + line + '\n'

    return [prob_facts, examples, background]


def process_rule_file(filename):
    print("FILE: {}".format(filename))
    rules = []
    filetext = read(filename)
    for line in filetext:
        l = line.strip()
        if l != '':
            rules.append(l)
        print("L: {}".format(l))

    return rules


def process_logic_file(filename):
    print("FILE: {}".format(filename))
    [prob_facts, examples, background] = parse_logic_file(filename)
    logging.debug('File parsed successfully')

    logging.debug('Starting processing probabilistic facts')
    pfs = process_inputs(prob_facts, 'pf')
    logging.debug('Probabilistic Facts Processed')

    logging.debug('Starting processing examples')
    exs = process_inputs(examples, 'example')
    logging.debug('Examples Processed')

    finalfile = ''

    finalfile += background

    tempfile = "/Users/kritisapra/Desktop/Imperial/Fourth_Year/prob_aspal/tmp/wk_" + filename.split("/")[-1]
    ensure_dir(tempfile)
    f = open(tempfile, 'w')
    f.write(finalfile)
    f.close()
    logging.debug('Temporary file created in {}'.format(tempfile))

    return tempfile, pfs, exs


# Helper functions
# Calculates the probability of a total choice using distribution semantics
def prob(total_choice, probabilistic_facts):
    probability = 1
    for pf in probabilistic_facts:
        if pf in total_choice:
            probability *= probabilistic_facts[pf]
        else:
            probability *= (1 - probabilistic_facts[pf])
    return probability


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
def l_accuracy(expected, actual):
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
    return 1 - ((true_positive + true_negative) / (true_positive + true_negative + false_positive + false_negative))


def h_score(h_len, h_loss, a):
    return ((h_len * a) + h_loss) / 2


def execute(filename, rules, prob_facts, examples, loss_func=l_accuracy):
    # proc = subprocess.Popen(SOLVER + ' < ' + file, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    solutions = {}
    bestscore = None
    bestsolution = set()

    logging.debug("Starting to make hypotheses.")
    hypotheses = powerset(rules, max=MAX_RULES)
    for h in hypotheses:
        print("HS: {}".format(h))
    logging.debug("Hypotheses made!")
    max_hypothesis_length = 1  # TODO: CHANGE THIS
    alpha = 1 / max_hypothesis_length

    logging.debug("Starting to make total choices.")
    total_choices = get_total_choices_with_probs(prob_facts)
    logging.debug("Total choices made.")

    for h in hypotheses:
        # Examples you are trying to reach
        prob_examples_h = {e: 0 for e in examples}
        logging.debug("Hypothesis: {}".format(h))

        for tc in total_choices:
            logging.debug("Hypothesis: {}, TC: {}".format(h, tc))
            # Create a Control object that will unify models against the appropriate
            # predicates. Then load the asp file that encodes the problem domain.

            ctrl = clingo.Control(["0", "--warn=none"])
            ctrl.load(filename)

            # Add facts as required and ground the program
            instance = tc
            for r in h:
                instance += r
            ctrl.add("base", [], instance)
            ctrl.ground([("base", [])])

            # Solve the program and get all models
            models = get_models(control=ctrl)

            # Calculate probability for each example given the hypothesis by adding the probability of the current
            # total choice
            check_models_for_examples(actual=prob_examples_h, models=models,
                                      tc_probability=total_choices[tc])

        # Calculate loss and score of the hypothesis
        loss = loss_func(expected=examples, actual=prob_examples_h)

        score = h_score(h_len=len(h), h_loss=loss, a=alpha)
        print("SCPRE: {}".format(score))

        # Check if hypothesis is a solution and if you have to update best solution
        if score < EPSILON:
            # Reset current solution to avoid duplicates and contamination
            solution = set(h)
            print("SOL: {}".format(solution))
            solutions[frozenset(solution)] = score

            # Check if the score of this hypothesis is better than the current best score
            if bestscore is None or score < bestscore:
                bestscore = score
                bestsolution.clear()
                bestsolution.add(frozenset(solution))
            elif score == bestscore:
                # There could be multiple solutions with the same lowest score
                bestsolution.add(frozenset(solution))

        logging.debug("HYpothesis: {}, Score: {}".format(h, score))

    # Return all the solutions, the best solutions and the best score
    return solutions, bestsolution, bestscore


def find_solutions(lp, rule_file):
    om.toOut('Finding Solutions', size=2)

    filename, pfs, exs = process_logic_file(lp)
    rules = process_rule_file(rule_file)
    om.toOut('Successfully processed {}. Now starting the solver'.format(filename))
    om.toOut('Invoking clingo')
    solutionshere, bestsolutionhere, bestscorehere = execute(filename=filename, rules=rules, prob_facts=pfs,
                                                             examples=exs)
    return solutionshere, bestsolutionhere, bestscorehere


def main(logic_file=DEFAULT_LOGIC_FILE, potential_rules=DEFAULT_RULE_FILE):
    om.toOut('Executing prob on logic file {} with given rules from FastLas {}.\nDebug logs in {}'.format(logic_file,
                                                                                                          potential_rules,
                                                                                                          LOG_FILENAME))

    start = time.perf_counter()
    solutions, bestsolution, bestscore = find_solutions(lp=logic_file, rule_file=potential_rules)
    end = time.perf_counter()
    time_taken = end - start
    print_solutions(solutions, bestsolution, bestscore, time_taken)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(logic_file=sys.argv[1], potential_rules=sys.argv[2])
    else:
        # print("Not enough arguments provided")
        main()
