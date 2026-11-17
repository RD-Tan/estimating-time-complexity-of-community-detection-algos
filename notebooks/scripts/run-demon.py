import time
from networkx import read_edgelist 
from cdlib.algorithms import demon

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filename",
        help="int edge list filename.",
    )

    parser.add_argument(
        "output",
        help="output file for report."
    )

    parser.add_argument(
        "--epsilon",
        type=float,
        required=False,
        default=0.25,
        help="merging threshold (default = 0.25)",
    )
    parser.add_argument(
        "--min_com_size",
        type=int,
        required=False,
        default=3,
        help="minimum size of a module (default = 3)",
    )

    args = parser.parse_args()

    G = read_edgelist(args.filename)

    start = time.perf_counter()

    demon(G, epsilon=args.epsilon, min_com_size=args.min_com_size)
    
    end = time.perf_counter()
    time_elapsed = end - start
    print(f"Elapsed time: {time_elapsed:.6f} seconds")

    with open(args.output, "w") as f:
        edge_count = G.size()
        node_count = G.order()
        density = edge_count / (node_count * (node_count - 1) // 2)
        f.write(f"{time_elapsed}\t{edge_count}\t{G.order()}\t{density}")