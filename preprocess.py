from collections import defaultdict, Counter
import sys
import re
import json

# Read cluster file
def read_cluster(fileName):
    membership = {}
    clusters = defaultdict(list)
    cntClass = Counter()
    with open(fileName, 'r') as fd:
        for line in fd:
            row = line.strip().split()
            membership[row[2]] = row[1]
            clusters[row[1]].append(row[2])
            cntClass[row[1]] += 1
        maximum = max(cntClass.values())
        for cluster in cntClass:
            cntClass[cluster] /= float(maximum)
    return membership, clusters, cntClass

# Read dependency file
def read_deps(fileName):
    deps = []
    with open(fileName, 'r') as fd:
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

# Write json file for cluster view
def write_cluster_json(fileName, cntClass, adjList):
    data = {}
    data["nodes"] = [{"id": key, "label": key, "level": cntClass[key]} \
            for key in cntClass]
    data["links"] = [{"target": dest, "source": src, "strength": adjList[src][dest]} \
            for src in adjList for dest in adjList[src]]
    #print(json.dumps(data))
    with open(fileName, 'w') as fd:
        fd.write(json.dumps(data, indent=2))

# Write json file for class view
def write_class_json(fileName, clusters, deps):
    adjList = defaultdict(list)
    for classA, classB in deps:
        adjList[classA].append(classB)
    data = clusters
    with open(fileName, 'w') as fd:
        fd.write(json.dumps(data, indent=2))

# Read ucc output for code complexity information
def read_ucc_output(fileName):
    sloc = {}
    pattern = re.compile("test")
    with open(fileName, 'r') as fd:
        for i, line in enumerate(fd):
            # Maybe not search for test pattern here
            if i > 10 and not re.search(pattern, line):
                if len(line) < 10:
                    break
                row = line.strip().split(",")
                objName = re.sub(r'/', r'.', row[-1])
                objName = re.sub(r'^.*org', r'org', objName)
                objName = re.sub(r'.java$', r'', objName)
                sloc[objName] = int(row[7])
    return sloc

if __name__=="__main__":
    try:
        _, clusterFile, dependencyFile = sys.argv
    except:
        print(" - Usage: python dep.py cluster_file_name dependency_file_name")
        sys.exit(1)
    pattern = re.compile("[^_]*_")
    version = pattern.search(sys.argv[1]).group()
    membership, clusters, cntClass = read_cluster(clusterFile)
    deps = read_deps(dependencyFile)
    adjList = anal_cluster_deps(membership, deps)
    write_cluster_json("Mygraph.json", cntClass, adjList)
    write_class_json("Myclass.json", clusters, deps)
