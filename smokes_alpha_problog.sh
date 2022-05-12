echo "Starting Experiments \n"

source /home/kriti/anaconda3/etc/profile.d/conda.sh

conda activate potassco

echo "Experiment 1 \n" > results/smokes_alpha_problog.txt
echo "Experiment 1 \n"

python prob_aspal_with_problog.py -f experiments/smokes.lp -a 0 -b 2 -mr 2 >> results/smokes_alpha_problog.txt

echo "Experiment 2 \n" >> results/smokes_alpha_problog.txt
echo "Experiment 2 \n"

python prob_aspal_with_problog.py -f experiments/smokes.lp -a 0.1 -b 1.9 -mr 2 >> results/smokes_alpha_problog.txt

echo "Experiment 3 \n" >> results/smokes_alpha_problog.txt
echo "Experiment 3 \n"

python prob_aspal_with_problog.py -f experiments/smokes.lp -a 0.2 -b 1.8 -mr 2 >> results/smokes_alpha_problog.txt

echo "Experiment 4 \n" >> results/smokes_alpha_problog.txt
echo "Experiment 4 \n"

python prob_aspal_with_problog.py -f experiments/smokes.lp -a 0.3 -b 1.7 -mr 2 >> results/smokes_alpha_problog.txt

echo "Experiment 5 \n" >> results/smokes_alpha_problog.txt
echo "Experiment 5 \n"

python prob_aspal_with_problog.py -f experiments/smokes.lp -a 0.4 -b 1.6 -mr 2 >> results/smokes_alpha_problog.txt

echo "Experiment 6 \n" >> results/smokes_alpha_problog.txt
echo "Experiment 6 \n"

python prob_aspal_with_problog.py -f experiments/smokes.lp -a 0.5 -b 1.5 -mr 2 >> results/smokes_alpha_problog.txt

echo "Experiment 7 \n" >> results/smokes_alpha_problog.txt
echo "Experiment 7 \n"

python prob_aspal_with_problog.py -f experiments/smokes.lp -a 0.6 -b 1.4 -mr 2 >> results/smokes_alpha_problog.txt

echo "Experiment 8 \n" >> results/smokes_alpha_problog.txt
echo "Experiment 8 \n"

python prob_aspal_with_problog.py -f experiments/smokes.lp -a 0.7 -b 1.3 -mr 2 >> results/smokes_alpha_problog.txt

echo "Experiment 9 \n" >> results/smokes_alpha_problog.txt
echo "Experiment 9 \n"

python prob_aspal_with_problog.py -f experiments/smokes.lp -a 0.8 -b 1.2 -mr 2 >> results/smokes_alpha_problog.txt

echo "Experiment 10 \n" >> results/smokes_alpha_problog.txt
echo "Experiment 10 \n"

python prob_aspal_with_problog.py -f experiments/smokes.lp -a 0.9 -b 1.1 -mr 2 >> results/smokes_alpha_problog.txt

echo "Experiment 11 \n" >> results/smokes_alpha_problog.txt
echo "Experiment 11 \n"

python prob_aspal_with_problog.py -f experiments/smokes.lp -a 1.0 -b 1.0 -mr 2 >> results/smokes_alpha_problog.txt

echo "Experiment 12 \n" >> results/smokes_alpha_problog.txt
echo "Experiment 12 \n"

python prob_aspal_with_problog.py -f experiments/smokes.lp -a 1.1 -b 0.9 -mr 2  >> results/smokes_alpha_problog.txt

echo "Experiment 13 \n" >> results/smokes_alpha_problog.txt
echo "Experiment 13 \n"

python prob_aspal_with_problog.py -f experiments/smokes.lp -a 1.2 -b 0.8 -mr 2 >> results/smokes_alpha_problog.txt

echo "Experiment 14 \n" >> results/smokes_alpha_problog.txt
echo "Experiment 14 \n"

python prob_aspal_with_problog.py -f experiments/smokes.lp -a 1.3 -b 0.7 -mr 2 >> results/smokes_alpha_problog.txt

echo "Experiment 15 \n" >> results/smokes_alpha_problog.txt
echo "Experiment 15 \n"

python prob_aspal_with_problog.py -f experiments/smokes.lp -a 1.4 -b 0.6 -mr 2 >> results/smokes_alpha_problog.txt

echo "Experiment 16 \n" >> results/smokes_alpha_problog.txt
echo "Experiment 16 \n"

python prob_aspal_with_problog.py -f experiments/smokes.lp -a 1.5 -b 0.5 -mr 2 >> results/smokes_alpha_problog.txt

echo "Experiment 17 \n" >> results/smokes_alpha_problog.txt
echo "Experiment 17 \n"

python prob_aspal_with_problog.py -f experiments/smokes.lp -a 1.6 -b 0.4 -mr 2 >> results/smokes_alpha_problog.txt

echo "Experiment 18 \n" >> results/smokes_alpha_problog.txt
echo "Experiment 18 \n"

python prob_aspal_with_problog.py -f experiments/smokes.lp -a 1.7 -b 0.3 -mr 2 >> results/smokes_alpha_problog.txt

echo "Experiment 19 \n" >> results/smokes_alpha_problog.txt
echo "Experiment 19 \n"

python prob_aspal_with_problog.py -f experiments/smokes.lp -a 1.8 -b 0.2 -mr 2 >> results/smokes_alpha_problog.txt

echo "Experiment 20 \n" >> results/smokes_alpha_problog.txt
echo "Experiment 20 \n"

python prob_aspal_with_problog.py -f experiments/smokes.lp -a 1.9 -b 0.1 -mr 2 >> results/smokes_alpha_problog.txt

echo "Experiment 21 \n" >> results/smokes_alpha_problog.txt
echo "Experiment 21 \n"

python prob_aspal_with_problog.py -f experiments/smokes.lp -a 2.0 -b 0.0 -mr 2 >> results/smokes_alpha_problog.txt

echo "Finished running experiments. See results in results/smokes_alpha_problog.txt"
