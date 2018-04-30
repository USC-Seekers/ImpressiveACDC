from functools import reduce


class UnionFindNode:
    def __init__(self, package):
        self.package = package
        self.parent = None
        self.height = 1

    def get_root(self):
        root = self
        if self.parent:
            root = self.parent.get_root()
            self.parent = root
        return root

    def union(self, node):
        cur_root = self.get_root()
        node_root = node.get_root()
        if cur_root.height > node_root.height:
            node_root.parent = cur_root
        elif node_root.height > cur_root.height:
            cur_root.parent = node_root
        else:
            cur_root.height += 1
            node_root.parent = cur_root


class ACDC:
    def __init__(self, filename):
        self.clusters = {}
        with open(filename) as f:
            while True:
                cluster_file_line = f.readline()
                if not cluster_file_line:
                    break
                (_, cluster_name, package) = map(lambda x: x.strip(), cluster_file_line.split(' '))
                if not cluster_name in self.clusters:
                    self.clusters[cluster_name] = []
                self.clusters[cluster_name].append(package)

    def get_adapted_membership(self):
        rv = {}
        for cluster_name in self.clusters:
            for package in self.clusters[cluster_name]:
                rv[package] = cluster_name
        return rv

    def get_adapted_cnt_class(self):
        rv = {}
        max_count = reduce(lambda prev, item: max(prev, len(item)), self.clusters, 0)
        for cluster_name in self.clusters:
            rv[cluster_name] = len(cluster_name) / max_count
        return rv



