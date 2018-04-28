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
        self.packages = {}
        self.clusters = {}
        with open(filename) as f:
            while True:
                cluster_file_line = f.readline()
                if not cluster_file_line:
                    break
                (_, package1, package2) = map(lambda x: x.strip(), cluster_file_line.split(' '))
                if package1 not in self.packages:
                    self.packages[package1] = UnionFindNode(package1)
                if package2 not in self.packages:
                    self.packages[package2] = UnionFindNode(package2)
                self.packages[package1].union(self.packages[package2])

        for package in self.packages:
            root_node = self.packages[package].get_root()
            if root_node.package not in self.clusters:
                self.clusters[root_node.package] = []
            self.clusters[root_node.package].append(package)