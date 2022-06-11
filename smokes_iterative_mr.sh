echo "Starting Experiments \n"

#source /home/kriti/anaconda3/etc/profile.d/conda.sh

#conda activate potassco

echo "Experiment 1 \n" > results/smokes_early_stop_window.txt
echo "Experiment 1 \n"

python probaspil_early_stop.py -f experiments/smokes.lp -mr 5 -mc 3 -w  1 >> results/smokes_early_stop_window.txt

echo "Experiment 2 \n" >> results/smokes_early_stop_window.txt
echo "Experiment 2 \n"

python probaspil_early_stop.py -f experiments/smokes.lp -mr 5 -mc 3 -w  2 >> results/smokes_early_stop_window.txt

echo "Experiment 3 \n" >> results/smokes_early_stop_window.txt
echo "Experiment 3 \n"

python probaspil_early_stop.py -f experiments/smokes.lp -mr 5 -mc 3 -w  3 >> results/smokes_early_stop_window.txt

echo "Experiment 4 \n" >> results/smokes_early_stop_window.txt
echo "Experiment 4 \n"

python probaspil_early_stop.py -f experiments/smokes.lp -mr 5 -mc 3 -w  4 >> results/smokes_early_stop_window.txt

echo "Experiment 5 \n" >> results/smokes_early_stop_window.txt
echo "Experiment 5 \n"

python probaspil_early_stop.py -f experiments/smokes.lp -mr 5 -mc 3 -w  5 >> results/smokes_early_stop_window.txt

echo "Experiment 6 \n" >> results/smokes_early_stop_window.txt
echo "Experiment 6 \n"

python probaspil_early_stop.py -f experiments/smokes.lp -mr 5 -mc 3 -w  6 >> results/smokes_early_stop_window.txt

echo "Experiment 7 \n" >> results/smokes_early_stop_window.txt
echo "Experiment 7 \n"

python probaspil_early_stop.py -f experiments/smokes.lp -mr 5 -mc 3 -w  7 >> results/smokes_early_stop_window.txt

echo "Experiment 8 \n" >> results/smokes_early_stop_window.txt
echo "Experiment 8 \n"

python probaspil_early_stop.py -f experiments/smokes.lp -mr 5 -mc 3 -w  8 >> results/smokes_early_stop_window.txt

echo "Experiment 9 \n" >> results/smokes_early_stop_window.txt
echo "Experiment 9 \n"

python probaspil_early_stop.py -f experiments/smokes.lp -mr 5 -mc 3 -w  9 >> results/smokes_early_stop_window.txt

echo "Experiment 10 \n" >> results/smokes_early_stop_window.txt
echo "Experiment 10 \n"

python probaspil_early_stop.py -f experiments/smokes.lp -mr 5 -mc 3 -w  10 >> results/smokes_early_stop_window.txt

echo "Finished running experiments. See results in results/smokes_early_stop_window.txt"