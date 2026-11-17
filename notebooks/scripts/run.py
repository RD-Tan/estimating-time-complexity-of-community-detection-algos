import itertools
from algos.Demon import Demon

if __name__ == "__main__":
    nodes = [20_000]
    densities = [0.0025, 0.003, 0.00625, 0.0075, 0.00875]
    epsilons = [0, 0.25, 0.5, 0.75]
    for node, density, epsilon in itertools.product(nodes, densities, epsilons):
        print(f"node count: {node}, density: {density}, epsilon: {epsilon}")
        dm = Demon(graph=None,
                    network_filename=f"synthetic/node-{node}-density-{density}.csv",
                    epsilon=epsilon,
                    min_community_size=3,
                    file_output=f"out/node-{node}-density-{density}-epsilon-{epsilon}.tsv")
        dm.execute()

        print("\n\n\n")