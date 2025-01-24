# PBS-builder

A simplified version of workflow management system for scalable data analysis.

# Change log

- Version 0.4.9: fixed bug in resolving dependencies, and update default parameters
- Version 0.4.8: add skip option & update progressbar
- Version 0.4.7: consistent behaviour in mu02 and mu04
- Version 0.4.6: add suport for escape character in variable names
- Version 0.4.5: add progress bar and verbose output options

# Usage

`pbs-builder` include the following commands:

1. [`qbatch`](https://bioinfo.ioz.ac.cn/git/zhangjy/pbs-builder/wiki/01.qbatch+-+building+automated+and+reproducible+pipelines)for batch submission of TORQUE/SLURM jobs

2. [`pestat`](https://bioinfo.ioz.ac.cn/git/zhangjy/pbs-builder/wiki/02.pestat+-+monitor+node+status) for monitoring cluster & nodes status 

3. [`pushover`](https://bioinfo.ioz.ac.cn/git/zhangjy/pbs-builder/wiki/03.pushover+-+get+nofications+from+compute+nodes+using+Pushover+service) for get noficiations from compute nodes

Please refer to our [wiki](https://bioinfo.ioz.ac.cn/git/zhangjy/pbs-builder/wiki/_pages) for detailed instructions.

# Installation

pbs-builder runs in **python3.7+** with the `tqdm` and `tomli` package installed, no other dependencies are required.

Install pbs-builder using the following command:

```bash
pip install pbs-builder
```
