start=$(date +%s.%N)
python3 ./app_simulated.py $1 > /dev/null
end=$(date +%s.%N)
#echo "Time taken: $(echo "$end - $start" | bc) seconds"
echo "$end - $start" | bc
