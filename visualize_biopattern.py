import matplotlib.pyplot as plt

rnd = []
seq = []
avg_rnd = 0
avg_seq = 0

avg_count = 0
avg_kb = 0

count = 0

with open("results/biopattern_output.txt", "r") as file:
    for line in file:
        if "DISK" in line:
            continue
        count += 1
        line = line.split()
        avg_rnd += int(line[2])
        avg_seq += int(line[3])
        rnd.append(avg_rnd / (count))
        seq.append(avg_seq / (count))
        avg_count += int(line[-2])
        avg_kb += int(line[-1])

print(avg_count / len(rnd))
print(avg_kb / len(rnd))

time = list(range(1, len(rnd) + 1))

plt.figure()

plt.plot(time, rnd, label='random', color='blue')
plt.xlabel('Time, sec')
plt.ylim(0, 100)
plt.title('% Random I/O')

plt.savefig("plots/random_io_plot.png")

plt.figure()
plt.plot(time, seq, label='sequential', color='green')
plt.xlabel('Time, sec')
plt.ylim(0, 100)
plt.title('% Sequential I/O')

plt.savefig("plots/sequential_io_plot.png")
