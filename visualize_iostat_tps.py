import matplotlib.pyplot as plt


def parse_iostat_output(output_file):
    bw = []
    tps = []

    max_bw = 0
    avg_bw = 0

    max_tps = 0
    avg_tps = 0

    with open(output_file, 'r') as f:
        lines = f.readlines()
        count = -1
        for line in lines:
            if 'sda' in line:
                count += 1

                values = line.split()

                tps_val = float(values[1])
                max_tps = max(max_tps, tps_val)
                avg_tps += tps_val
                if count != 0:
                    tps.append(avg_tps / count)
                else:
                    tps.append(avg_tps)

                bw_val = float(values[3])
                max_bw = max(max_bw, bw_val)
                avg_bw += bw_val
                if count != 0:
                    bw.append(avg_bw / count)
                else:
                    bw.append(avg_bw)

    avg_bw /= len(bw)
    avg_tps /= len(tps)
    print(f"avg_bandwidth: {avg_bw} MB/s")
    print(f"avg_tps: {str(avg_tps)} t/s")

    print()

    print(f"max_bandwidth: {str(max_bw)} MB/s")
    print(f"max_tps: {str(max_tps)} t/s")
    return bw, tps


def plot_bw(bw):
    plt.figure()
    x_values = list(range(len(bw)))

    plt.plot(x_values, bw, label='bandwidth')

    plt.xlabel('Time')
    plt.ylabel('MB/s')
    plt.legend()

    plt.savefig('plots/bw_plot.png')


def plot_tps(tps):
    plt.figure()
    x_values = list(range(len(tps)))

    plt.plot(x_values, tps, label='I/O per second')

    plt.xlabel('Time')
    plt.ylabel('tps')
    plt.legend()

    plt.savefig('plots/tps_plot.png')


bw_values, tps_values = parse_iostat_output('results/iostat_output.txt')
plot_bw(bw_values)
plot_tps(tps_values)
