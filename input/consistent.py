from ACDC import ACDC
from RELAX import RELAX
from PIL import Image, ImageDraw
from preprocess import anal_cluster_deps, read_deps
import math
import json


def output(path, clusters, adj_list, categories_vectors):
    # clusters = [(x, y, s, n, t)]
    # x: horizontal position
    # y: vertical position
    # s: relative radius
    # n: cluster name
    # t: type

    json_root = {"nodes": [], "links": [], "axis": categories_vectors}
    for (x, y, s, n, t) in clusters:
        json_root["nodes"].append({"id": n, "label": n, "level": s, "x": x, "y": y, "type": t})
    for cluster_name in adj_list:
        cluster = adj_list[cluster_name]
        for dest_cluster in cluster:
            json_root["links"].append({
                "target": dest_cluster,
                "source": cluster_name,
                "strength": cluster[dest_cluster]
            })

    f = open(path, 'w')
    json.dump(json_root, f)

def calc_type(pos, categories_vector):
    # pos: (pos_y, pos_x)
    max_pro = -1
    cluster_type = None

    for category_name in categories_vector:
        val = pos[0] * categories_vector[category_name][0] + pos[1] * categories_vector[category_name][1]
        if val > max_pro:
            cluster_type = category_name
            max_pro = val
    return cluster_type


def generate(acdc_cluster, relax_cluster, dep, out_file):
    acdc = ACDC(acdc_cluster)
    relax = RELAX(relax_cluster)

    membership = acdc.get_adapted_membership()
    class_cnt = acdc.get_adapted_cnt_class()

    clusters_pos = []
    categories_vectors = {}
    interval = math.pi * 2 / len(relax.categories)
    cur_radian = -math.pi
    for category in relax.categories:
        categories_vectors[category] = (math.sin(cur_radian), math.cos(cur_radian))
        cur_radian += interval

    total = 0
    available = 0
    n_cluster = 0
    for cluster_name in acdc.clusters:
        n_cluster += 1
        pos_x = 0
        pos_y = 0

        cluster = acdc.clusters[cluster_name]
        for package in cluster:
            total += 1
            category = relax.packages.get(package, None)
            if not category:
                continue
            available += 1
            vector = categories_vectors[category]
            pos_y += vector[0]
            pos_x += vector[1]

        clusters_pos.append(
            (pos_x, pos_y,
             class_cnt[cluster_name],
             cluster_name,
             calc_type((pos_y, pos_x), categories_vectors))
        )
        deps = read_deps(dep)
        adj_list = anal_cluster_deps(membership, deps)
        output(out_file, clusters_pos, adj_list, categories_vectors)


if __name__ == "__main__":
    generate("log4j-2.1_acdc_clustered.rsf", "log4j-2.1_relax_clusters.rsf", "../input/log4j-2.1_deps.rsf", "consistent.json")
