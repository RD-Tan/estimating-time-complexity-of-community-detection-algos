
import itertools
from .creategraphs import create_graph

if __name__ == "__main__":
    nodes = [20_000]
    densities = [0.0025, 0.003, 0.00625, 0.0075, 0.00875]
    for node, density in itertools.product(nodes, densities):
        create_graph(node, density, f"synthetic/node-{node}-density-{density}.csv")