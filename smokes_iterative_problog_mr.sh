echo "Starting Experiments \n"

source /home/kriti/anaconda3/etc/profile.d/conda.sh

conda activate potassco

echo "Experiment 1 \n" > results/surf_iterative_problog_mr.txt
echo "Experiment 1 \n"

python iterative_prob_aspal_with_problog.py -f experiments/surf.lp -mh 25 -mh 25 -mr 1 >> results/surf_iterative_problog_mr.txt

echo "Experiment 2 \n" >> results/surf_iterative_problog_mr.txt
echo "Experiment 2 \n"

python iterative_prob_aspal_with_problog.py -f experiments/surf.lp -mh 25 -mr 2 >> results/surf_iterative_problog_mr.txt

echo "Experiment 3 \n" >> results/surf_iterative_problog_mr.txt
echo "Experiment 3 \n"

python iterative_prob_aspal_with_problog.py -f experiments/surf.lp -mh 25 -mr 3 >> results/surf_iterative_problog_mr.txt

echo "Experiment 4 \n" >> results/surf_iterative_problog_mr.txt
echo "Experiment 4 \n"

python iterative_prob_aspal_with_problog.py -f experiments/surf.lp -mh 25 -mr 4 >> results/surf_iterative_problog_mr.txt

echo "Experiment 5 \n" >> results/surf_iterative_problog_mr.txt
echo "Experiment 5 \n"

python iterative_prob_aspal_with_problog.py -f experiments/surf.lp -mh 25 -mr 5 >> results/surf_iterative_problog_mr.txt

echo "Experiment 6 \n" >> results/surf_iterative_problog_mr.txt
echo "Experiment 6 \n"

python iterative_prob_aspal_with_problog.py -f experiments/surf.lp -mh 25 -mr 6 >> results/surf_iterative_problog_mr.txt

echo "Experiment 7 \n" >> results/surf_iterative_problog_mr.txt
echo "Experiment 7 \n"

python iterative_prob_aspal_with_problog.py -f experiments/surf.lp -mh 25 -mr 7 >> results/surf_iterative_problog_mr.txt

echo "Experiment 8 \n" >> results/surf_iterative_problog_mr.txt
echo "Experiment 8 \n"

python iterative_prob_aspal_with_problog.py -f experiments/surf.lp -mh 25 -mr 8 >> results/surf_iterative_problog_mr.txt

echo "Experiment 9 \n" >> results/surf_iterative_problog_mr.txt
echo "Experiment 9 \n"

python iterative_prob_aspal_with_problog.py -f experiments/surf.lp -mh 25 -mr 9 >> results/surf_iterative_problog_mr.txt

echo "Experiment 10 \n" >> results/surf_iterative_problog_mr.txt
echo "Experiment 10 \n"

python iterative_prob_aspal_with_problog.py -f experiments/surf.lp -mh 25 -mr 10 >> results/surf_iterative_problog_mr.txt

echo "Finished running experiments. See results in results/surf_iterative_problog_mr.txt"