import time
from networkx import read_edgelist 
from cdlib.algorithms import coach

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
        "--density_threshold",
        type=float,
        required=False,
        default=0.7,
        help="minimum core density (default = 0.7)",
    )
    parser.add_argument(
        "--affinity_threshold",
        type=float,
        required=False,
        default=0.225,
        help="maximum core affinity (default = 0.225)",
    )
    parser.add_argument(
        "--closeness_threshold",
        type=float,
        required=False,
        default=0.5,
        help="minimum neighbor closeness (default = 0.5)",
    )

    args = parser.parse_args()

    G = read_edgelist(args.filename)

    start = time.perf_counter()

    coach(
        G,
        density_threshold=args.density_threshold,
        affinity_threshold=args.affinity_threshold,
        closeness_threshold=args.closeness_threshold,
    )

    end = time.perf_counter()
    time_elapsed = end - start
    print(f"Elapsed time: {time_elapsed:.6f} seconds")

    with open(args.output, "w") as f:
        edge_count = G.size()
        node_count = G.order()
        density = edge_count / (node_count * (node_count - 1) // 2)
        f.write(f"{time_elapsed}\t{edge_count}\t{G.order()}\t{density}")