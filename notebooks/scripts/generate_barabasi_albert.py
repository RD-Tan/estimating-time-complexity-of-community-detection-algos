from networkx import Graph, write_edgelist, barabasi_albert_graph
import os
import pickle

def generate_barabasi_albert(n, m, seed = 42):
    if(m > n):
        print("hello?")
        raise ValueError

    return barabasi_albert_graph(n, m, seed)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "n",
        type=int,
        help="number of nodes",
    )

    parser.add_argument(
        "m",
        type=int,
        help="number of edges to attach to new node. strictly 1 <= m < n",
    )

    parser.add_argument(
        "output_file",
        help="output file name. Can include path.",
    )

    parser.add_argument(
        "-s",
        "--seed",
        type=int,
        default=42,
        help="seed random value."
    )

    args = parser.parse_args()
    print(args)
    write_edgelist(generate_barabasi_albert(args.n, args.m, args.seed), args.output_file)


