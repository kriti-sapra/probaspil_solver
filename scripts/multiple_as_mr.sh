echo "Starting Experiments \n"

source /home/kriti/anaconda3/etc/profile.d/conda.sh

conda activate potassco

echo "Experiment 1 \n" > results/listening_multiple_answerset_mr.txt
echo "Experiment 1 \n"

python prob_aspal_multiple_answersets.py -f experiments/walk_answer_set.lp -mc 1 >> results/listening_multiple_answerset_mr.txt

echo "Experiment 2 \n" >> results/listening_multiple_answerset_mr.txt
echo "Experiment 2 \n"

python prob_aspal_multiple_answersets.py -f experiments/walk_answer_set.lp -mc 2 >> results/listening_multiple_answerset_mr.txt

echo "Experiment 3 \n" >> results/listening_multiple_answerset_mr.txt
echo "Experiment 3 \n"

python prob_aspal_multiple_answersets.py -f experiments/walk_answer_set.lp -mc 3 >> results/listening_multiple_answerset_mr.txt

echo "Experiment 4 \n" >> results/listening_multiple_answerset_mr.txt
echo "Experiment 4 \n"

python prob_aspal_multiple_answersets.py -f experiments/walk_answer_set.lp -mc 4 >> results/listening_multiple_answerset_mr.txt

echo "Experiment 5 \n" >> results/listening_multiple_answerset_mr.txt
echo "Experiment 5 \n"

python prob_aspal_multiple_answersets.py -f experiments/walk_answer_set.lp -mc 5 >> results/listening_multiple_answerset_mr.txt

echo "Experiment 6 \n" >> results/listening_multiple_answerset_mr.txt
echo "Experiment 6 \n"

python prob_aspal_multiple_answersets.py -f experiments/walk_answer_set.lp -mc 6 >> results/listening_multiple_answerset_mr.txt

echo "Experiment 7 \n" >> results/listening_multiple_answerset_mr.txt
echo "Experiment 7 \n"

python prob_aspal_multiple_answersets.py -f experiments/walk_answer_set.lp -mc 7 >> results/listening_multiple_answerset_mr.txt

echo "Experiment 8 \n" >> results/listening_multiple_answerset_mr.txt
echo "Experiment 8 \n"

python prob_aspal_multiple_answersets.py -f experiments/walk_answer_set.lp -mc 8 >> results/listening_multiple_answerset_mr.txt

echo "Experiment 9 \n" >> results/listening_multiple_answerset_mr.txt
echo "Experiment 9 \n"

python prob_aspal_multiple_answersets.py -f experiments/walk_answer_set.lp -mc 9 >> results/listening_multiple_answerset_mr.txt

echo "Experiment 10 \n" >> results/listening_multiple_answerset_mr.txt
echo "Experiment 10 \n"

python prob_aspal_multiple_answersets.py -f experiments/walk_answer_set.lp -mc 10 >> results/listening_multiple_answerset_mr.txt

echo "Finished running experiments. See results in results/listening_multiple_answerset_mr.txt"