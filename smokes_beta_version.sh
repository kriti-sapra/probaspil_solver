echo "Starting Experiments \n"

source /home/kriti/anaconda3/etc/profile.d/conda.sh

conda activate potassco

echo "Experiment 1 \n" > results/smokes_beta_scores.txt
echo "Experiment 1 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -mr 3 -b 0 >> results/smokes_beta_scores.txt

echo "Experiment 2 \n" >> results/smokes_beta_scores.txt
echo "Experiment 2 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -mr 3 -b 0.1 >> results/smokes_beta_scores.txt

echo "Experiment 3 \n" >> results/smokes_beta_scores.txt
echo "Experiment 3 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -mr 3 -b 0.2 >> results/smokes_beta_scores.txt

echo "Experiment 4 \n" >> results/smokes_beta_scores.txt
echo "Experiment 4 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -mr 3 -b 0.3 >> results/smokes_beta_scores.txt

echo "Experiment 5 \n" >> results/smokes_beta_scores.txt
echo "Experiment 5 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -mr 3 -b 0.4 >> results/smokes_beta_scores.txt

echo "Experiment 6 \n" >> results/smokes_beta_scores.txt
echo "Experiment 6 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -mr 3 -b 0.5 >> results/smokes_beta_scores.txt

echo "Experiment 7 \n" >> results/smokes_beta_scores.txt
echo "Experiment 7 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -mr 3 -b 0.6 >> results/smokes_beta_scores.txt

echo "Experiment 8 \n" >> results/smokes_beta_scores.txt
echo "Experiment 8 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -mr 3 -b 0.7 >> results/smokes_beta_scores.txt

echo "Experiment 9 \n" >> results/smokes_beta_scores.txt
echo "Experiment 9 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -mr 3 -b 0.8 >> results/smokes_beta_scores.txt

echo "Experiment 10 \n" >> results/smokes_beta_scores.txt
echo "Experiment 10 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -mr 3 -b 0.9 >> results/smokes_beta_scores.txt

echo "Experiment 11 \n" >> results/smokes_beta_scores.txt
echo "Experiment 11 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -mr 3 -b 1 >> results/smokes_beta_scores.txt

echo "Finished running experiments. See results in results/smokes_beta_scores.txt"
