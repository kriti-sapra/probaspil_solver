echo "Starting Experiments \n"

source /home/kriti/anaconda3/etc/profile.d/conda.sh

conda activate potassco

echo "Experiment 1 \n" > results/smokes_epsilon_scores.txt
echo "Experiment 1 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -e 0.0 >> results/smokes_epsilon_scores.txt

echo "Experiment 2 \n" >> results/smokes_epsilon_scores.txt
echo "Experiment 2 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -e 0.25 >> results/smokes_epsilon_scores.txt

echo "Experiment 3 \n" >> results/smokes_epsilon_scores.txt
echo "Experiment 3 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -e 0.5 >> results/smokes_epsilon_scores.txt

echo "Experiment 4 \n" >> results/smokes_epsilon_scores.txt
echo "Experiment 4 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -e 0.75 >> results/smokes_epsilon_scores.txt

echo "Experiment 5 \n" >> results/smokes_epsilon_scores.txt
echo "Experiment 5 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -e 1.0 >> results/smokes_epsilon_scores.txt

echo "Experiment 6 \n" >> results/smokes_epsilon_scores.txt
echo "Experiment 6 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -e 1.25 >> results/smokes_epsilon_scores.txt

echo "Experiment 7 \n" >> results/smokes_epsilon_scores.txt
echo "Experiment 7 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -e 1.5 >> results/smokes_epsilon_scores.txt

echo "Experiment 8 \n" >> results/smokes_epsilon_scores.txt
echo "Experiment 8 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -e 1.75 >> results/smokes_epsilon_scores.txt

echo "Experiment 9 \n" >> results/smokes_epsilon_scores.txt
echo "Experiment 9 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -e 2.0 >> results/smokes_epsilon_scores.txt

echo "Experiment 10 \n" >> results/smokes_epsilon_scores.txt
echo "Experiment 10 \n"

echo "Finished running experiments. See results in results/smokes_epsilon_scores.txt"
