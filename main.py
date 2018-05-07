from preprocess import read_cluster, read_deps, anal_cluster_deps, write_cluster_json, read_ucc_output
from consistent import generate
from class_generator import generate_class_json
import sys

try:
    _, path, name, outdir = sys.argv
except:
    print(" - Usage: python3 main.py pathToInput systemName outDir")
    sys.exit(1)

path += "/"
outdir += "/"
acdc  = path + name + "_acdc_clustered.rsf"
dep   = path + name + "_deps.rsf"
relax = path + name + "_relax_clusters.rsf"
ucc   = path + name + "-Java_outfile.csv"

ucc_size = read_ucc_output(ucc)
generate_class_json(acdc, relax, ucc_size, outdir + name + "-class.json")

m, _, cnt = read_cluster(acdc)
d = read_deps(dep)
adj = anal_cluster_deps(m, d)
write_cluster_json(outdir + name + ".json", cnt, adj)

generate(acdc, relax, dep, outdir + name + "-consistent.json")
