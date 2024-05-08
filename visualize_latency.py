with open("strace_output.txt", "r") as file:
    lines = file.readlines()

avg_latency = 0
count = 0

for line in lines:
    if line.startswith("write") or line.startswith("read"):
        value = float(line[line.rfind("<") + 1:line.rfind(">")])
        avg_latency += value
        count += 1

if count > 0:
    avg_latency_microseconds = avg_latency / count * 1000000
    print(f"{avg_latency_microseconds:.3f} microseconds")
