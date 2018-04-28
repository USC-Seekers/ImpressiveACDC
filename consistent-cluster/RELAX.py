class RELAX:
    def __init__(self, filename):
        self.categories = {}
        self.packages = {}

        with open(filename) as f:
            while True:
                cluster_file_line = f.readline()
                if not cluster_file_line:
                    break
                (_, category, package) = map(lambda x: x.strip(), cluster_file_line.split(' '))

                if category not in self.categories:
                    self.categories[category] = 1
                else:
                    self.categories[category] += 1

                self.packages[package] = category
