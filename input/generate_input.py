from preprocess import read_cluster, read_deps, anal_cluster_deps, write_cluster_json, read_ucc_output
from consistent import generate
from class_generator import generate_class_json

files = [
    {"acdc": 'log4j-2.1_acdc_clustered.rsf', "dep": 'log4j-2.1_deps.rsf', "name": 'log4j-2.1',
     "relax": "log4j-2.1_relax_clusters.rsf", "ucc": "log4j-2.1-Java_outfile.csv"},
    {"acdc": 'log4j-2.4_acdc_clustered.rsf', "dep": 'log4j-2.4_deps.rsf', "name": 'log4j-2.4',
     "relax": "log4j-2.4_relax_clusters.rsf"},
    {"acdc": 'hadoop-0.2.0_acdc_clustered.rsf', "dep": 'hadoop-0.2.0_deps.rsf', "name": 'hadoop-0.2.0',
     "relax": 'hadoop-0.2.0_relax_clusters.rsf', "ucc": "hadoop-0.2.0-Java_outfile.csv"}
]

for version in files:
    acdc = version.get("acdc", None)
    dep = version.get("dep", None)
    relax = version.get("relax", None)
    name = version.get("name", None)
    ucc = version.get("ucc", None)

    if acdc is not None and relax is not None and name is not None and ucc is not None:
        ucc_size = read_ucc_output(ucc)
        generate_class_json(acdc, relax, ucc_size, name + "-class.json")
    if acdc is not None and dep is not None and name is not None:
        m, _, cnt = read_cluster(acdc)
        d = read_deps(dep)
        adj = anal_cluster_deps(m, d)
        write_cluster_json(name + ".json", cnt, adj)

    if acdc is not None and dep is not None and name is not None and relax is not None:
        generate(acdc, relax, dep, name + "-consistent.json")


