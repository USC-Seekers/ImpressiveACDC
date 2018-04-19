from collections import defaultdict, Counter
import sys
import re

try:
    _, clusterFile, dependencyFile = sys.argv
except:
    print " - Usage: python dep.py cluster_file_name dependency_file_name"
    sys.exit(1)
pattern = re.compile("[^_]*_")
version = pattern.search(sys.argv[1]).group()
print version
# Read cluster file
membership = {}
cntClass = Counter()
with open(clusterFile, 'r') as fd:
    for line in fd:
        row = line.strip().split()
        membership[row[2]] = row[1]
        cntClass[row[1]] += 1
# Read dependency file
deps = []
with open(dependencyFile, 'r') as fd:
    for line in fd:
        row = line.strip().split()
        deps.append((row[1], row[2]))
# Analyze cluster dependencies
adjList = defaultdict(Counter)
for classA, classB in deps:
    clusterA, clusterB = membership[classA], membership[classB]
    if clusterA != clusterB:
        adjList[clusterA][clusterB] += 1
# Write cluster complexity file
with open(version + "cluster_complexity.rsf", 'w') as fd:
    for cluster in cntClass:
        fd.write("%s\t%d\n" % (cluster, cntClass[cluster]))
# Write cluster dependency file
with open(version + "cluster_deps.rsf", 'w') as fd:
    for clusterA in adjList:
        for clusterB in adjList[clusterA]:
            fd.write("%s\t%s\t%d\n" % \
                    (clusterA, clusterB, adjList[clusterA][clusterB]))
