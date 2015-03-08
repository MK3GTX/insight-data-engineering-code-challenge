apt-get update
apt-get install python3 

chmod a+x ./src/word_count.py
chmod a+x ./src/running_median.py

python3 ./src/word_count.py ./wc_input ./wc_output/wc_result.txt
python3 ./src/running_median.py ./wc_input ./wc_output/med_result.txt
