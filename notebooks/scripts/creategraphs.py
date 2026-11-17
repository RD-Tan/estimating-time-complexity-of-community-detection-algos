import random
import math
import bisect
import csv

def dict_value_or_key( dict, key ):
    return dict[ key ] if key in dict else key

def virtual_shuffle( max_length, quantity, seed = None ):
    swap_map = {}
    if( seed != None ): random.seed( seed )

    if quantity > max_length: quantity = max_length
    if quantity < 0: quantity = 0

    start = max_length - 1
    end = start - quantity

    for pointer_index in range( start, end, -1 ):
        random_index = random.randint( 0, pointer_index )
        yield dict_value_or_key( swap_map, random_index )
        swap_map[ random_index ] = dict_value_or_key( swap_map, pointer_index )
        if pointer_index in swap_map:
            del swap_map[ pointer_index ]

def create_graph(node_count, density, output_file):
    edge_ids = []
    total_edges = node_count * (node_count - 1) // 2
    edge_count = math.ceil(total_edges * density)
    for edge in virtual_shuffle(total_edges, edge_count):
        edge_ids.append(edge)
    
    lookup_range = [node_count - 2]
    for i in range(node_count - 2):
        lookup_range.append(lookup_range[i] + (node_count - i - 2))

    X = [bisect.bisect_left(lookup_range, edge_id) for edge_id in edge_ids]
    y = []
    for i in range(edge_count):
        dividend = edge_ids[i] - (lookup_range[X[i] - 1] + 1) if X[i] > 0 else edge_ids[i] 
        y.append((X[i] + 1) + dividend % (total_edges - 1 - X[i]))

    edge_list = zip(X,y)
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=" ")
        writer.writerows(edge_list)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "node_count",
        type=int,
        help="number of nodes to create in the graph.",
    )
    parser.add_argument(
        "density",
        type=float,
        help="how dense the graph will be made. in [0, 1].",
    )

    parser.add_argument(
        "output_file",
        help="the filename (optionally including directory) of the output file."
    )

    args = parser.parse_args()
    create_graph(args.node_count, args.density, args.output_file)
