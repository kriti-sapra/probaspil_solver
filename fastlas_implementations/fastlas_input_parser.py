import sys
import re
from prob_utils import *

FILENAME = '/Users/kritisapra/Desktop/Imperial/Fourth_Year/prob_aspal/experiments/fastlast.lp'
TEMP_FILE_BG = '/Users/kritisapra/Desktop/Imperial/Fourth_Year/prob_aspal/fastlas_implementations/temp/prob_background_input.lp'
TEMP_FILE_FASTLAS = '/Users/kritisapra/Desktop/Imperial/Fourth_Year/prob_aspal/fastlas_implementations/temp/fastlas_input.las'


def parse_file(filename):
    modedecs = []
    constants = []
    prob_facts = []
    examples = []
    background = ""
    filetext = read(filename)
    for line in filetext:
        print("LINE : {}".format(line))
        if line.startswith("mode"):
            modedecs.append(line)
        elif line.startswith("example("):
            examples.append(line)
        elif line.startswith("pf("):
            prob_facts.append(line)
        elif line.startswith("constant("):
            constants.append(line)
        elif not line.startswith("%"):
            background = background + line + '\n'

    return modedecs, constants, prob_facts, examples, background


def write_to_background_file(pfs, exs, bg):
    ensure_dir(TEMP_FILE_BG)
    f = open(TEMP_FILE_BG, "w")
    for pf in pfs:
        f.write(pf + '\n')
    for ex in exs:
        f.write(ex + '\n')
    f.write(bg)
    f.close()


def write_to_fastlas_file(mds, consts, pfs, exs):
    ensure_dir(TEMP_FILE_FASTLAS)
    f = open(TEMP_FILE_FASTLAS, "w")
    tcs = powerset(pfs)
    for md in mds:
        f.write('#' + md + '\n')
    i = 0
    for e in exs:
        for tc in tcs:
            ex_string = '#pos(eg{}, {{{}}}, {{}}, '.format(i, e)
            print("NEW EX STRING: {}".format(ex_string))
            # TODO: Add in the total choice and close the example and add to file.
            ex_string += '{'
            ex_string += ' '.join(tc)
            ex_string += ' }). \n'
            print("ADD TC: {}".format(ex_string))

            f.write(ex_string)
            i += 1
    for cnst in consts:
        f.write('#' + cnst + '\n')
    f.close()


def main(filename=FILENAME):
    print("FILENAME: {}".format(filename))
    modedecs, constants, prob_facts, examples, background = parse_file(filename)
    write_to_background_file(pfs=prob_facts, exs=examples, bg=background)
    processed_prob_facts = extract_predicates(prob_facts, add_stop=True)
    processed_examples = extract_predicates(examples)
    write_to_fastlas_file(mds=modedecs, consts=constants, pfs=processed_prob_facts, exs=processed_examples)


if __name__ == "__main__":
    try:
        # main(filename=sys.argv[1])
        main()
    except IndexError:
        print("Filename not provided")
