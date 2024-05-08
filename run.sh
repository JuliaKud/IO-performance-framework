#!/bin/bash

if [ "$#" -lt 3 ]; then
    echo "Usage: $0 <binary_file> <filesize_mb> <max_threads> [-i]"
    exit 1
fi

sudo mkdir /dev/cpuset/testCpuSet
sudo /bin/echo 1-7 > mkdir /dev/cpuset/testCpuSet/cpuset.cpus
sudo ps h -eo pid > tasks

programme="$1"
filesize_mb="$2"
max_threads="$3"

path_to_biopattern="src_biopattern/biopattern"

if [ -e "file.txt" ]; then
    rm file.txt
fi

size_bytes=$((filesize_mb * 1024 * 1024))
fallocate -l "$size_bytes" file.txt

> results/time_res.txt

mkdir copies

if [[ "$4" == "-i" ]]; then
    if [ -e "results/iostat_output.txt" ]; then
        > iostat_output.txt
    fi
    iostat -m -d 1 > iostat_output.txt & iostat_pid=$!
fi

if [[ "$4" == "-p" ]]; then
    if [ -e "results/biopattern_output.txt" ]; then
        > biopattern_output.txt
    fi
    $path_to_biopattern -T 1 1000 > results/biopattern_output.txt & biopattern_pid=$!
fi

cgcreate -g cpuset:/cgroupFramework
cgset -r cpuset.cpus=0 /cgroupFramework

for ((threads = 1; threads <= max_threads; threads++)); do
    args1=""
    args2=""
    for ((i = 1; i <= threads; i++)); do
        args1+=" file.txt"
        args2+=" copies/$i.txt"
    done
    echo "Threads: $threads" >> results/time_res.txt
    (sudo cgexec -g cpuset:/cgroupFramework --sticky time parallel "$programme" ::: $args1 ::: $args2) 2>> results/time_res.txt
done

if [[ "$4" == "-i" ]]; then
    kill $iostat_pid
fi

if [[ "$4" == "-p" ]]; then
    kill $biopattern_pid
fi

python3 visualize_time_res.py filesize_mb

rm file.txt
rm -r "copies"
