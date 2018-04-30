import json


def output(path, clusters):
    # clusters = [(x, y, s, n, t)]
    # x: horizontal position
    # y: vertical position
    # s: relative radius
    # n: cluster name
    # t: type

    json_root = {"nodes": [], "links": []}
    for (x, y ,s, n, t) in clusters:
        json_root["nodes"].append({"id": n, "label": n, "level": s, "x": x, "y": y, "type": t})

    f = open(path, 'w')
    json.dump(json_root, f)
