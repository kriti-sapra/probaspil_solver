echo "Starting Experiments \n"

source /home/kriti/anaconda3/etc/profile.d/conda.sh

conda activate potassco

echo "Experiment 1 \n" > results/smokes_iterative_window.txt
echo "Experiment 1 \n"

python iterative_prob_aspal.py -f experiments/smokes.lp  -w 1 >> results/smokes_iterative_window.txt

echo "Experiment 2 \n" >> results/smokes_iterative_window.txt
echo "Experiment 2 \n"

python iterative_prob_aspal.py -f experiments/smokes.lp  -w 2 >> results/smokes_iterative_window.txt

echo "Experiment 3 \n" >> results/smokes_iterative_window.txt
echo "Experiment 3 \n"

python iterative_prob_aspal.py -f experiments/smokes.lp  -w 3 >> results/smokes_iterative_window.txt

echo "Experiment 4 \n" >> results/smokes_iterative_window.txt
echo "Experiment 4 \n"

python iterative_prob_aspal.py -f experiments/smokes.lp  -w 4 >> results/smokes_iterative_window.txt

echo "Experiment 5 \n" >> results/smokes_iterative_window.txt
echo "Experiment 5 \n"

python iterative_prob_aspal.py -f experiments/smokes.lp  -w 5 >> results/smokes_iterative_window.txt

echo "Experiment 6 \n" >> results/smokes_iterative_window.txt
echo "Experiment 6 \n"

python iterative_prob_aspal.py -f experiments/smokes.lp  -w 6 >> results/smokes_iterative_window.txt

echo "Experiment 7 \n" >> results/smokes_iterative_window.txt
echo "Experiment 7 \n"

python iterative_prob_aspal.py -f experiments/smokes.lp  -w 7 >> results/smokes_iterative_window.txt

echo "Experiment 8 \n" >> results/smokes_iterative_window.txt
echo "Experiment 8 \n"

python iterative_prob_aspal.py -f experiments/smokes.lp  -w 8 >> results/smokes_iterative_window.txt

echo "Experiment 9 \n" >> results/smokes_iterative_window.txt
echo "Experiment 9 \n"

python iterative_prob_aspal.py -f experiments/smokes.lp  -w 9 >> results/smokes_iterative_window.txt

echo "Experiment 10 \n" >> results/smokes_iterative_window.txt
echo "Experiment 10 \n"

python iterative_prob_aspal.py -f experiments/smokes.lp  -w 10 >> results/smokes_iterative_window.txt

echo "Finished running experiments. See results in results/smokes_iterative_window.txt"