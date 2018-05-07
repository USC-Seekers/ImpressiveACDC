# ImpressiveACDE
## Pre-process Data
* Run ACDC on the system and take the result
    * e.g. hadoop-0.2.0_relax_clusters.rsf
* Run RELAX on the system and take the result
    * e.g. hadoop-0.2.0_acdc_clustered.rsf, hadoop-0.2.0_deps.rsf
* Run UCC on the system
    * e.g. `UCC -dir hadoop-0.2.0`
* Rename the UCC Java outfile result
    * e.g. `mv Java_outfile.csv hadoop-0.2.0-Java_outfile.csv`

Group these 4 files under the same directory and run `main.py` to pre-process the data. The result will be written in json format and will serve as the input for visualization. 

```shell
$ mkdir data
$ mv hadoop-0.2.0_relax_clusters.rsf hadoop-0.2.0_acdc_clustered.rsf, hadoop-0.2.0_deps.rsf hadoop-0.2.0-Java_outfile.csv data
$ # Run preprocessing script: python3 main.py in_dir sys_version out_dir
$ python3 main.py data hadoop-0.2.0 input
$ # Another example
$ python3 main.py input/hadoop/0.10.1/ hadoop-0.10.1 input
```

## Start Server
```shell
$ cd server
$ npm install
$ npm start
```

## Release
[Visualization Page](http://54.183.64.51/ImpressiveACDC/visualization.html)
