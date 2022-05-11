echo "Starting Experiments \n"

source /home/kriti/anaconda3/etc/profile.d/conda.sh

conda activate potassco

echo "Experiment 1 \n" > result.txt
echo "Experiment 1 \n"

python prob_aspal_with_problog.py -f experiments/smokes.lp -mc 1 >> result.txt

echo "Experiment 2 \n" >> result.txt
echo "Experiment 2 \n"

python prob_aspal_with_problog.py -f experiments/smokes.lp -mc 2 >> result.txt

echo "Experiment 3 \n" >> result.txt
echo "Experiment 3 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -mc 3 >> result.txt

echo "Experiment 4 \n" >> result.txt
echo "Experiment 4 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -mc 4 >> result.txt

echo "Experiment 5 \n" >> result.txt
echo "Experiment 5 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -mc 5 >> result.txt

echo "Experiment 6 \n" >> result.txt
echo "Experiment 6 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -mc 6 >> result.txt

echo "Experiment 7 \n" >> result.txt
echo "Experiment 7 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -mc 7 >> result.txt

echo "Experiment 8 \n" >> result.txt
echo "Experiment 8 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -mc 8 >> result.txt

echo "Experiment 9 \n" >> result.txt
echo "Experiment 9 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -mc 9 >> result.txt

echo "Experiment 10 \n" >> result.txt
echo "Experiment 10 \n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -mc 10 >> result.txt

echo "Finished running experiments. See results in results.txt"