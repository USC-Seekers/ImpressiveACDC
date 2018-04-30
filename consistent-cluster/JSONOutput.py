import json


def output(path, clusters, adj_list):
    # clusters = [(x, y, s, n, t)]
    # x: horizontal position
    # y: vertical position
    # s: relative radius
    # n: cluster name
    # t: type

    json_root = {"nodes": [], "links": []}
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
