echo "Starting Experiments \n"

source /home/kriti/anaconda3/etc/profile.d/conda.sh

conda activate potassco

echo "Experiment 1 \n" > results/smokes_early_stop_problog_mh.txt
echo "Experiment 1 \n"

python early_stop_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 1 >> results/smokes_early_stop_problog_mh.txt

echo "Experiment 2 \n" >> results/smokes_early_stop_problog_mh.txt
echo "Experiment 2 \n"

python early_stop_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 2 >> results/smokes_early_stop_problog_mh.txt

echo "Experiment 3 \n" >> results/smokes_early_stop_problog_mh.txt
echo "Experiment 3 \n"

python early_stop_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 3 >> results/smokes_early_stop_problog_mh.txt

echo "Experiment 4 \n" >> results/smokes_early_stop_problog_mh.txt
echo "Experiment 4 \n"

python early_stop_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 4 >> results/smokes_early_stop_problog_mh.txt

echo "Experiment 5 \n" >> results/smokes_early_stop_problog_mh.txt
echo "Experiment 5 \n"

python early_stop_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 5 >> results/smokes_early_stop_problog_mh.txt

echo "Experiment 6 \n" >> results/smokes_early_stop_problog_mh.txt
echo "Experiment 6 \n"

python early_stop_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 6 >> results/smokes_early_stop_problog_mh.txt

echo "Experiment 7 \n" >> results/smokes_early_stop_problog_mh.txt
echo "Experiment 7 \n"

python early_stop_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 7 >> results/smokes_early_stop_problog_mh.txt

echo "Experiment 8 \n" >> results/smokes_early_stop_problog_mh.txt
echo "Experiment 8 \n"

python early_stop_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 8 >> results/smokes_early_stop_problog_mh.txt

echo "Experiment 9 \n" >> results/smokes_early_stop_problog_mh.txt
echo "Experiment 9 \n"

python early_stop_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 9 >> results/smokes_early_stop_problog_mh.txt

echo "Experiment 10 \n" >> results/smokes_early_stop_problog_mh.txt
echo "Experiment 10 \n"

python early_stop_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 10 >> results/smokes_early_stop_problog_mh.txt

echo "Experiment 11 \n" > results/smokes_early_stop_problog_mh.txt
echo "Experiment 11 \n"

python early_stop_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 11 >> results/smokes_early_stop_problog_mh.txt

echo "Experiment 12 \n" >> results/smokes_early_stop_problog_mh.txt
echo "Experiment 12 \n"

python early_stop_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 12 >> results/smokes_early_stop_problog_mh.txt

echo "Experiment 13 \n" >> results/smokes_early_stop_problog_mh.txt
echo "Experiment 13 \n"

python early_stop_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 13 >> results/smokes_early_stop_problog_mh.txt

echo "Experiment 14 \n" >> results/smokes_early_stop_problog_mh.txt
echo "Experiment 14 \n"

python early_stop_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 14 >> results/smokes_early_stop_problog_mh.txt

echo "Experiment 15 \n" >> results/smokes_early_stop_problog_mh.txt
echo "Experiment 15 \n"

python early_stop_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 15 >> results/smokes_early_stop_problog_mh.txt

echo "Experiment 16 \n" >> results/smokes_early_stop_problog_mh.txt
echo "Experiment 16 \n"

python early_stop_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 16 >> results/smokes_early_stop_problog_mh.txt

echo "Experiment 17 \n" >> results/smokes_early_stop_problog_mh.txt
echo "Experiment 17 \n"

python early_stop_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 17 >> results/smokes_early_stop_problog_mh.txt

echo "Experiment 18 \n" >> results/smokes_early_stop_problog_mh.txt
echo "Experiment 18 \n"

python early_stop_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 18 >> results/smokes_early_stop_problog_mh.txt

echo "Experiment 19 \n" >> results/smokes_early_stop_problog_mh.txt
echo "Experiment 19 \n"

python early_stop_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 19 >> results/smokes_early_stop_problog_mh.txt

echo "Experiment 20 \n" >> results/smokes_early_stop_problog_mh.txt
echo "Experiment 20 \n"

python early_stop_prob_aspal_with_problog.py -f experiments/smokes.lp -mh 20 >> results/smokes_early_stop_problog_mh.txt

echo "Finished running experiments. See results in results/smokes_early_stop_problog_mh.txt"