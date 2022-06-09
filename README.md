
# [ProbASPIL: Probabilistic Answer Set Programming Inductive Learner](https://github.com/kriti-sapra/prob_aspal_solver)

---

ProbASPIL algorithms are a set of algorithms that explore probabilistic rule learning under the prolog and answer set semantics. This repository contains the following 8 algorithms:

- ProbASPIL: A probabilistic rule learning algorithm for the prolog semantics. This algorithm can only be used with programs that have a single answer set. 
- Early Stop ProbASPIL: An extension to the ProbASPIL algorithm that has an early stopping criteria and performs a breadth first search in increasing length order of the hypothesis search space. This algorithm can also only be used with programs that have a single answer set. 
- ProbASPIL with ProbLog: A probabilistic rule learning algorithm that uses ProbLog as the underlying solver instead of clingo. This automatically restricts the programs that can be used with this algorithm to programs with a single answer set. 
- Early Stop ProbASPIL with ProbLog: An extension of the ProbASPIL with ProbLog algorithm that implements an early stopping criteria for the breadth first search. This algorithm also uses ProbLog as the underlying solver and therefore cannot be used with programs that have multiple answer sets. 
- ProbASPIL+: ProbASPIL+ builds on top of the ProbASPIL algorithm by implementing a system that allows for programs with multiple answer sets. ProbASPIL+ uniformly distributes the probability of a total choice evenly amongst the answer sets. This method allows ProbASPIL+ to be more general than ProbASPIL algorithm as it works on programs with single answer sets as well as multiple answer sets. 
- Early Stop ProbASPIL+: The version of the ProbASPIL+ algorithm that implements the early stopping criteria. This implementation works for programs with a single answer set as well as multiple answer sets. 
- CredalASPIL: A version of the ProbASPIL algorithm that uses the credal semantics instead of the distribution semantics. The examples provided now have a lower and upper probability associated to them. This implementation can work for programs with single answer sets by setting the lower and upper probability to the same value. 
- Early Stop CredalASPIL: The version of CredalASPIL that implements teh early stopping criteria. This algorithm also works for programs that have a single answer set as well as multiple answer sets. 

## Setting up the environment

---

In order to run the ProbASPIL algorithms, an anacoda environment needs to be set up and clingo and problog need to be installed into the anaconda environment. 

1. Create a conda environment
Use this [&lt;link&gt;](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
) or the following command in terminal to create a new conda environment  


```
conda create --name probaspil
```

2. Activate the conda environment 
```
conda activate probaspil
```

3. Download pip into the `probaspil` conda environment 
```
conda install pip
```

3. Use pip to install clingo to the `probaspil` conda environment 
```
{$PATH_TO_ANACONDA}/anaconda/envs/probaspil/bin/pip install clingo
```
4. Use pip to install problog to the `probaspil` conda environment 
```
{$PATH_TO_ANACONDA}/anaconda/envs/probaspil/bin/pip install problog
```

## Running a ProbASPIL algorithm

---

This repo has a different script for each of the 8 algorithms. The algorithms can be run by activating the conda environment then running the appropriate script. The script names are:

- ProbASPIL: `probaspil.py`
- Early Stop ProbASPIL: `probaspil_early_stop.py`
- ProbASPIL with ProbLog: `problog_probaspil.py`
- Early Stop ProbASPIL: `problog_probaspil_early_stop.py`
- ProbASPIL+: `probaspil+.py`
- Early Stop ProbASPIL+: `probaspil+_early_stop.py`
- CredalASPIL: `credalaspil.py`
- Early Stop CredalASPIL: `credalaspil_early_stop.py`

The following command would run the ProbASPIL algorithm with the default parameters. 

```
python3 probaspil.py
```

All the algorithms have the following hyperparameters that can be specified using the corresponding flags:
```
file name: -f 
maximum rules: -mr or --max_rules
maximum conditions: -mc or --max_conditions
```

The Brute Force algorithms have extra hyperparameters: alpha, beta and epsilon. These can be specified using the following flags:
```
alpha: -a or --alpha
beta: -b or --beta
epsilon: -e or --epsilon
```

The Early Stop algorithms have the extra hyperparameters: window and maximum hypothesis length that can be specified using the following flags:

```
window: -w or --window
max hypothesis length: -mh or --max_hyp
```

The following command with run the smokes file in `experiments/` with maximum rules set to 3, maximum conditions set to 3, and other values of alpha, beta and epsilon using the ProbASPIL+ algorithms.

```
python3 probaspil+.py -f experiments/smokes.lp -mr 3 -mc 3 -a 0.5 -b 1 -e 1.
```