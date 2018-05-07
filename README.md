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

## Deploy
### Deploy at localhost
```shell
$ git clone https://github.com/USC-Seekers/ImpressiveACDC
$ cd ImpressiveACDC/server
$ npm install
$ mkdir public
$ cd public
$ git clone https://github.com/USC-Seekers/ImpressiveACDC
$ cd .. 
$ node server.js
```

Note that you may need root privilege to start server at port 80. You can also modify server.js to start server at a different port.

To access visualization page, type following URL in your browser

```url
http://localhost/ImpressiveACDC/index.html
```

## Quick Start

### Select version
You can choose the software version to be visualized using select filed at top left. Whenever a new version is selected, a force view will of that software will be displayed by default.
### Force view
Force view is the default view. You can search certain cluster name by search text filed and search button at top left.
### Consistent view
By clicking Toggle View button, you can enter consistent view from force view. Consistent view also support search function.
### Class view
By clicking any cluster name in either force view or consistent view, you can enter class view, which display a certain cluster in much more detail. Clicking Toggle View button will lead you back to force view or consistent view.