from ACDC import ACDC
from RELAX import RELAX
import json


def generate_class_json(acdc_cluster, relax_cluster, ucc_size, out_file):
    acdc = ACDC(acdc_cluster)
    relax = RELAX(relax_cluster)

    rv = {}

    for cluster_name in acdc.clusters:
        rv[cluster_name] = []
        cluster_packages = acdc.clusters[cluster_name]
        for package in cluster_packages:
            package_rv = {}
            package_rv["name"] = package
            package_type = relax.packages.get(package, None)
            package_rv["type"] = package_type
            package_rv["complexity"] = ucc_size.get(package, None)
            rv[cluster_name].append(package_rv)

    f = open(out_file, "w")
    json.dump(rv, f)
    f.close()