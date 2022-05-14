echo "Starting Experiments \n"

source /home/kriti/anaconda3/etc/profile.d/conda.sh

conda activate potassco

echo "Experiment 1 \n" > results/smokes_iterative_mc_problog.txt
echo "Experiment 1 \n"

python iterative_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 20 -mc 1 >> results/smokes_iterative_mc_problog.txt

echo "Experiment 2 \n" >> results/smokes_iterative_mc_problog.txt
echo "Experiment 2 \n"

python iterative_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 20 -mc 2 >> results/smokes_iterative_mc_problog.txt

echo "Experiment 3 \n" >> results/smokes_iterative_mc_problog.txt
echo "Experiment 3 \n"

python iterative_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 20 -mc 3 >> results/smokes_iterative_mc_problog.txt

echo "Experiment 4 \n" >> results/smokes_iterative_mc_problog.txt
echo "Experiment 4 \n"

python iterative_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 20 -mc 4 >> results/smokes_iterative_mc_problog.txt

echo "Experiment 5 \n" >> results/smokes_iterative_mc_problog.txt
echo "Experiment 5 \n"

python iterative_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 20 -mc 5 >> results/smokes_iterative_mc_problog.txt

echo "Experiment 6 \n" >> results/smokes_iterative_mc_problog.txt
echo "Experiment 6 \n"

python iterative_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 20 -mc 6 >> results/smokes_iterative_mc_problog.txt

echo "Experiment 7 \n" >> results/smokes_iterative_mc_problog.txt
echo "Experiment 7 \n"

python iterative_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 20 -mc 7 >> results/smokes_iterative_mc_problog.txt

echo "Experiment 8 \n" >> results/smokes_iterative_mc_problog.txt
echo "Experiment 8 \n"

python iterative_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 20 -mc 8 >> results/smokes_iterative_mc_problog.txt

echo "Experiment 9 \n" >> results/smokes_iterative_mc_problog.txt
echo "Experiment 9 \n"

python iterative_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 20 -mc 9 >> results/smokes_iterative_mc_problog.txt

echo "Experiment 10 \n" >> results/smokes_iterative_mc_problog.txt
echo "Experiment 10 \n"

python iterative_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 20 -mc 10 >> results/smokes_iterative_mc_problog.txt

echo "Finished running experiments. See results in results/smokes_iterative_mc_problog.txt"