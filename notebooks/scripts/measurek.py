from collections import Counter
import csv
from networkx import Graph, from_edgelist

def measure_k(network: Graph):
    degrees = [deg for _, deg in network.degree()]
    degree_counts = Counter(degrees)

    x = sorted(degree_counts.keys())
    y_raw = [degree_counts[k] for k in x]

    total_nodes = network.number_of_nodes()
    y = [count / total_nodes for count in y_raw]

    return (x, y, y_raw)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "network_file",
        type=str,
        help="path to edge list network file. edges must be numbered (convert using convert-to-int-edge-list.py).",
    )
    parser.add_argument(
        "output_file",
        help="the filename (optionally including directory) of the output file."
    )

    args = parser.parse_args()
    try:
        with open(args.network_file) as f:
            reader = csv.reader(f)
            network = from_edgelist(reader)
            k = measure_k(network)
            
    except FileExistsError:
        print("bru h no file.")
        exit()
    