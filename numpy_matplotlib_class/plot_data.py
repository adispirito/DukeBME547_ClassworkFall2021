import numpy as np
import matplotlib.pyplot as plt


def input_data(filename):
    with open(filename, 'r') as in_file:
        in_lines = in_file.readlines()
    return in_lines


def parse_data(in_lines):
    list_no_return = in_lines.strip("\n")
    list_split = list_no_return.split(",")
    list_int = [int(x) for x in list_split]
    return list_int

def plot_single_trace(in_data):
    time = np.arange(0, len(in_data), 1)
    print(in_data)
    plt.plot(time, in_data)
    plt.show()


def main():
    in_data = input_data("overall_data.dat")
    data_0 = parse_data(in_data[0])
    # print(data_0)
    plot_single_trace(data_0)
    plt.plot([1,2,3])
    plt.show()


if __name__ == "__main__":
    main()
