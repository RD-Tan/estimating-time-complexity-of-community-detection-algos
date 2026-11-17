configfile: "config.yaml"

rule all:
    input:
        expand("out/{algo_param}/scale_free/report-n-{n}-m-{m}.txt",
                n=[1024, 2048, 4096, 8192, 16384],
                m=[8, 16, 32, 64, 128, 256, 512],
                algo_param=[f"{algo}/{p}" for algo, ps in config["module_detection_params"].items() for p in ps])

rule make_barabasi_albert:
    output:
        "synthetic/scale_free/n-{n}-m-{m}.csv"
    shell:
        "python notebooks/scripts/generate_barabasi_albert.py "
        "{wildcards.n} {wildcards.m} {output}"

rule run_coach_scale_free:
    input:
        "synthetic/scale_free/n-{n}-m-{m}.csv"
    output:
        "out/coach/{p}/scale_free/report-n-{n}-m-{m}.txt"
    params:
        affinity_value = lambda wildcards: config['module_detection_params']['coach'][wildcards.p]
    shell:
        "python notebooks/scripts/run-coach.py "
        "{input} {output} --affinity_threshold {params.affinity_value}"

rule run_demon_scale_free:
    input:
        "synthetic/scale_free/n-{n}-m-{m}.csv"
    output:
        "out/demon/{p}/scale_free/report-n-{n}-m-{m}.txt"
    params:
        epsilon_value = lambda wildcards: config['module_detection_params']['demon'][wildcards.p]
    shell:
        "python notebooks/scripts/run-demon.py "
        "{input} {output} --epsilon {params.epsilon_value}"
