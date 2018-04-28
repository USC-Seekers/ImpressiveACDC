from collections import defaultdict, Counter
import sys
import re
import json

# Read cluster file
def read_cluster(fileName):
    membership = {}
    cntClass = Counter()
    with open(fileName, 'r') as fd:
        for line in fd:
            row = line.strip().split()
            membership[row[2]] = row[1]
            cntClass[row[1]] += 1
        maximum = max(cntClass.values())
        for cluster in cntClass:
            cntClass[cluster] /= float(maximum)
    return membership, cntClass

# Read dependency file
def read_deps(fileName):
    deps = []
    with open(dependencyFile, 'r') as fd:
        for line in fd:
            row = line.strip().split()
            deps.append((row[1], row[2]))
    return deps

# Analyze cluster dependencies
def anal_cluster_deps(membership, deps):
    adjList = defaultdict(Counter)
    maximum = 0
    for classA, classB in deps:
        clusterA, clusterB = membership[classA], membership[classB]
        if clusterA != clusterB:
            adjList[clusterA][clusterB] += 1
            if adjList[clusterA][clusterB] > maximum:
                maximum = adjList[clusterA][clusterB]
    for classA in adjList:
        for classB in adjList[classA]:
            adjList[classA][classB] /= float(maximum)
    return adjList

def write_simple_output(version, cntClass, adjList):
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

def write_json(fileName, cntClass, adjList):
    data = {}
    data["nodes"] = [{"id": key, "label": key, "level": cntClass[key]} \
            for key in cntClass]
    data["links"] = [{"target": dest, "source": src, "strength": adjList[src][dest]} \
            for src in adjList for dest in adjList[src]]
    #print(json.dumps(data))
    with open(fileName, 'w') as fd:
        fd.write(json.dumps(data, indent=2))

if __name__=="__main__":
    try:
        _, clusterFile, dependencyFile = sys.argv
    except:
        print(" - Usage: python dep.py cluster_file_name dependency_file_name")
        sys.exit(1)
    pattern = re.compile("[^_]*_")
    version = pattern.search(sys.argv[1]).group()
    membership, cntClass = read_cluster(clusterFile)
    deps = read_deps(dependencyFile)
    adjList = anal_cluster_deps(membership, deps)
    write_json("Mygraph.json", cntClass, adjList)
