from itertools import combinations, chain

import clingo


def get_models(control):
    models = []
    with control.solve(yield_=True) as handle:
        for m in handle:
            models.append(m.symbols(atoms=True))
    return models


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


def main():
    pfs = {"interested(a, logic). ": 0.3554, "interested(b, biology). ": 0.57797,
           "interested(c, sport). ": 0.6982, "interested(d, music). ": 0.8903}
    total_choices = get_total_choices_with_probs(pfs)
    print("TCS: {}".format(total_choices))

    examples = {"shared_interest(c,d,music)": 0, "shared_interest(d,c,music)": 0, "shared_interest(d,a,logic)": 0,
                "shared_interest(a,d,logic)": 0, "shared_interest(b,c,sport)": 0, "shared_interest(c,b,sport)": 0,
                "shared_interest(b,c,biology)": 0, "shared_interest(c,b,biology)": 0}

    for tc in total_choices:
        ctrl = clingo.Control(["0", "--warn=none"])
        ctrl.load('experiments/clingo_eg_for_probs.lp')

        # Add facts as required and ground the program
        instance = tc
        ctrl.add("base", [], instance)
        ctrl.ground([("base", [])])

        # Solve the program and get all models
        models = get_models(control=ctrl)
        str_models = []
        print(len(models))
        for m in models:
            str_models.append(str(m))

        uniform_split = total_choices[tc] / len(models)

        for e in examples:
            for m in str_models:
                if e in m:
                    examples[e] += uniform_split

    for x in examples:
        print("Example: {}, Prob:{}".format(x, examples[x]))


if __name__ == "__main__":
    main()
