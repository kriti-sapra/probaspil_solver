
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

    print(f"Found Solution in {time:0.4f} seconds")


