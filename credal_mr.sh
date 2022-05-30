echo "Starting Experiments \n"

source /home/kriti/anaconda3/etc/profile.d/conda.sh

conda activate potassco

echo "Experiment 1 \n" > results/credal_walk_example_mr.txt
echo "Experiment 1 \n"

python creadal_semantics_prob_aspal.py -f experiments/credal/credal_walk_example.lp -mr 1 >> results/credal_walk_example_mr.txt

echo "Experiment 2 \n" >> results/credal_walk_example_mr.txt
echo "Experiment 2 \n"

python creadal_semantics_prob_aspal.py -f experiments/credal/credal_walk_example.lp -mr 2 >> results/credal_walk_example_mr.txt

echo "Experiment 3 \n" >> results/credal_walk_example_mr.txt
echo "Experiment 3 \n"

python creadal_semantics_prob_aspal.py -f experiments/credal/credal_walk_example.lp -mr 3 >> results/credal_walk_example_mr.txt

echo "Experiment 4 \n" >> results/credal_walk_example_mr.txt
echo "Experiment 4 \n"

python creadal_semantics_prob_aspal.py -f experiments/credal/credal_walk_example.lp -mr 4 >> results/credal_walk_example_mr.txt

echo "Experiment 5 \n" >> results/credal_walk_example_mr.txt
echo "Experiment 5 \n"

python creadal_semantics_prob_aspal.py -f experiments/credal/credal_walk_example.lp -mr 5 >> results/credal_walk_example_mr.txt

echo "Experiment 6 \n" >> results/credal_walk_example_mr.txt
echo "Experiment 6 \n"

python creadal_semantics_prob_aspal.py -f experiments/credal/credal_walk_example.lp -mr 6 >> results/credal_walk_example_mr.txt

echo "Experiment 7 \n" >> results/credal_walk_example_mr.txt
echo "Experiment 7 \n"

python creadal_semantics_prob_aspal.py -f experiments/credal/credal_walk_example.lp -mr 7 >> results/credal_walk_example_mr.txt

echo "Experiment 8 \n" >> results/credal_walk_example_mr.txt
echo "Experiment 8 \n"

python creadal_semantics_prob_aspal.py -f experiments/credal/credal_walk_example.lp -mr 8 >> results/credal_walk_example_mr.txt

echo "Experiment 9 \n" >> results/credal_walk_example_mr.txt
echo "Experiment 9 \n"

python creadal_semantics_prob_aspal.py -f experiments/credal/credal_walk_example.lp -mr 9 >> results/credal_walk_example_mr.txt

echo "Experiment 10 \n" >> results/credal_walk_example_mr.txt
echo "Experiment 10 \n"

python creadal_semantics_prob_aspal.py -f experiments/credal/credal_walk_example.lp -mr 10 >> results/credal_walk_example_mr.txt
