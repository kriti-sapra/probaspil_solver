echo "Starting Experiments \n"

source /home/kriti/anaconda3/etc/profile.d/conda.sh

conda activate potassco

echo "Experiment 1 Prob ASPAL\n" > results/smokes_multiple_as.txt
echo "Experiment 1 Prob ASPAL\n"

python prob_aspal_with_constants.py -f experiments/smokes.lp -mr 6 >> results/smokes_multiple_as.txt

echo "Experiment 2 Early Stop Prob ASPAL\n" >> results/smokes_multiple_as.txt
echo "Experiment 2 Early Stop Prob ASPAL\n"

python early_stop_prob_aspal.py -f experiments/smokes.lp -mr 6  >> results/smokes_multiple_as.txt

echo "Experiment 3 Prob ASPAL with multiple answer sets\n" >> results/smokes_multiple_as.txt
echo "Experiment 3 Prob ASPAL with multiple answer sets\n"

python prob_aspal_multiple_answersets.py -f experiments/smokes.lp -mr 6  >> results/smokes_multiple_as.txt

echo "Experiment 4 Early Stop Prob ASPAL with multiple answer sets\n" >> results/smokes_multiple_as.txt
echo "Experiment 4 Early Stop Prob ASPAL with multiple answer sets\n"

python early_stop_prob_aspal_with_answersets.py -f experiments/smokes.lp -mr 6  >> results/smokes_multiple_as.txt

echo "Experiment 5 Prob ASPAL with credal\n" >> results/smokes_multiple_as.txt
echo "Experiment 5 Prob ASPAL with credal\n"

python creadal_semantics_prob_aspal.py -f experiments/credal_smokes.lp -mr 6  >> results/smokes_multiple_as.txt

echo "Experiment 6 Early Stop Prob ASPAL with credal\n" >> results/smokes_multiple_as.txt
echo "Experiment 6 Early Stop Prob ASPAL with credal\n"

python early_stop_creadal_semantics.py -f experiments/credal_smokes.lp -mr 6  >> results/smokes_multiple_as.txt
