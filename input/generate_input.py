from preprocess import read_cluster, read_deps, anal_cluster_deps, write_json
from consistent import generate

files = [
    {"acdc": 'log4j-2.1_acdc_clustered.rsf', "dep": 'log4j-2.1_deps.rsf', "name": 'log4j-2.1',
     "relax": "log4j-2.1_relax_clusters.rsf"},
    {"acdc": 'log4j-2.4_acdc_clustered.rsf', "dep": 'log4j-2.4_deps.rsf', "name": 'log4j-2.4',
     "relax": "log4j-2.4_relax_clusters.rsf"},
    {"acdc": 'hadoop-0.2.0_clusters.rsf', "dep": 'hadoop-0.2.0_class_deps.rsf', "name": 'hadoop-0.2.0'}
]

for version in files:
    acdc = version.get("acdc", None)
    dep = version.get("dep", None)
    relax = version.get("relax", None)
    name = version.get("name", None)

    if acdc is not None and dep is not None and name is not None:
        m, cnt = read_cluster(acdc)
        d = read_deps(dep)
        adj = anal_cluster_deps(m, d)
        write_json(name + ".json", cnt, adj)

    if acdc is not None and dep is not None and name is not None and relax is not None:
        generate(acdc, relax, dep, name + "-consistent.json")
