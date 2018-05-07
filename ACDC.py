from preprocess import read_cluster
class ACDC:
    def __init__(self, filename):
        self.membership, self.clusters, self.cntClass = read_cluster(filename)

    def get_adapted_membership(self):
        return self.membership

    def get_adapted_cnt_class(self):
        return self.cntClass
