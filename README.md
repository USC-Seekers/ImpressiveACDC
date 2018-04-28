# ImpressiveACDE
## Pre-process Data
Run `preprocess` to convert ACDC recovery result into json format for visualization input. 

```shell
$ # For hadoop-0.2.0
$ python3 preprocess.py input/hadoop-0.2.0_clusters.rsf input/hadoop-0.2.0_class_deps.rsf
$ # For log4j-2.1
$ python3 preprocess.py consistent-cluster/log4j-2.1_acdc_clustered.rsf consistent-cluster/log4j-2.1_deps.rsf
```
