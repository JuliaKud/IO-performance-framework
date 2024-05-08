import matplotlib.pyplot as plt
import sys

threads = []
execution_time = []
bandwidth = []

total_time = 0
file_size = int(sys.argv[1])  # MB

with open('results/time_res.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    if line.startswith('Threads: '):
        threads.append(int(line.split(':')[1].strip()))
    elif line.startswith('real'):
        line = line.split()[1].split('m')
        minutes = int(line[0])
        seconds = float(line[1][:-1])
        execution_time.append(float(minutes) * 60 + seconds)
        bandwidth.append(file_size * threads[-1] / execution_time[-1])
        total_time += execution_time[-1]

plt.plot(threads, execution_time, marker='o')
plt.xlabel('Number of Threads')
plt.ylabel('Execution Time (s)')
plt.grid(True)

plt.savefig('plots/execution_time_plot.png')

print(f"Total time: ${total_time}")
