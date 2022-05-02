import os
import re
from itertools import chain, combinations


class OutputWrapper:

    def __init__(self):
        default = True


class HumanOutputWrapper(OutputWrapper):
    debugflag = False

    def __int__(self):
        self.debugflag = False

    def toOut(self, out, type='info', size=1):
        if type == 'info' or (self.debugflag and type == 'debug'):
            if size == 1:
                print(out)
            elif size == 2:
                print('---- {} ----'.format(out))
            elif size == 3:
                print('\n%%%%%%%% {} %%%%%%%%'.format(out))
            elif size == 4:
                print('\n################ {} ################\n'.format(out))


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


def ensure_dir(f):
    """f is a filename. If f's directory doesn't exist, it's created.
    """
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)


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


def extract_predicates(inputs, add_stop=False):
    out = []
    for p in inputs:
        args = get_outer_arguments(p)
        print(args)
        assert len(args) == 2
        key = args[0]
        if add_stop:
            key += '.'
        out.append(key)
    return out

# Process probabilistic facts and examples
def process_inputs(inputs, delim=''):
    out = {}
    for p in inputs:
        print("P: {}".format(p))
        args = get_outer_arguments(p)
        print(args)
        assert len(args) == 2
        key = args[0]
        if delim == 'pf':
            key += '. '
        out[key] = float(args[1])
    return out


def powerset(iterable, max=None):
    s = list(iterable)
    if max is None:
        max = len(s)
    lst = chain.from_iterable(combinations(s, r) for r in range(max + 1))
    return list(lst)

def print_solution(isol, score):
    print("Hypothesis: ")
    if len(isol) == 0:
        print("Empty Hypothesis")
    else:
        for r in isol:
            print(r)
    print("Score: {:.2f}".format(score))


def print_solutions(solutions, best_solution, best_score, time):
    i = 0
    for isol in solutions:
        i += 1
        if len(solutions) > 1:
            print('\n----Solution {}----\n'.format(str(i)))
        # these are frozen sets of clauses
        print_solution(isol, solutions[isol])

    print('\n----Best Solution----\n')
    for isol in best_solution:
        print_solution(isol, best_score)

    print('Found Solution in {:.4f} seconds'.format(time))
