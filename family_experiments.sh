echo "Starting Experiments \n"

source /home/kriti/anaconda3/etc/profile.d/conda.sh

conda activate potassco

echo "Experiment 1 Prob ASPAL\n" > results/family_experiments.txt
echo "Experiment 1 Prob ASPAL\n"

python prob_aspal_with_constants.py -f experiments/family.lp -e 0.5 >> results/family_experiments.txt

echo "Experiment 2 Early Stop Prob ASPAL\n" >> results/family_experiments.txt
echo "Experiment 2 Early Stop Prob ASPAL\n"

python early_stop_prob_aspal.py -f experiments/family.lp  >> results/family_experiments.txt

echo "Experiment 3 EArly Stop Prob ASPAL with ProbLog\n" >> results/family_experiments.txt
echo "Experiment 3 Early STop Prob ASPAL with ProbLog\n"

python early_stop_prob_aspal_with_problog.py -f experiments/family.lp  >> results/family_experiments.txt

#echo "Experiment 4 Prob ASPAL with ProbLog\n" >> results/family_experiments.txt
#echo "Experiment 4 Prob ASPAL with ProbLog\n"
#
#python prob_aspal_with_problog.py -f experiments/family.lp  >> results/family_experiments.txt
