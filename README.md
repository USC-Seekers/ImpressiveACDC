# ImpressiveACDE
<!-- org.apache.logging.log4j.core.util.datetime.ss -->
## Pre-process Data
Run `preprocess` to convert ACDC recovery result into json format for visualization input. 

```shell
$ # For hadoop-0.2.0
$ python3 preprocess.py input/hadoop-0.2.0_acdc_clustered.rsf input/hadoop-0.2.0_deps.rsf
$ # For log4j-2.1
$ python3 preprocess.py input/log4j-2.1_acdc_clustered.rsf input/log4j-2.1_deps.rsf
$ # For log4j-2.4
$ python3 preprocess.py input/log4j-2.4_acdc_clustered.rsf input/log4j-2.4_deps.rsf
```

## Release
[Visualization Page](http://54.183.64.51/ImpressiveACDC/visualization.html)
