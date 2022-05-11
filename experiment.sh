echo "Starting Experiments \n"

source /Users/kritisapra/opt/miniconda3/etc/profile.d/conda.sh

conda activate potassco

echo "Experiment 1 \n" > result.txt

python prob_aspal_with_constants.py -f experiments/surf_const_example.lp -mc 1 -mr 2 >> result.txt

echo "Experiment 2 \n" >> result.txt

python prob_aspal_with_constants.py -f experiments/surf_const_example.lp -mc 2 -mr 2 >> result.txt

echo "Experiment 3 \n" >> result.txt

python prob_aspal_with_constants.py -f experiments/surf_const_example.lp -mc 3 -mr 2 >> result.txt

echo "Finished running experiments. See results in results.txt"