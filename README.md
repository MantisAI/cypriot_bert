# Cypriot BERT

The aim of this project is pretrain a Cypriot language model, similar to GreekBERT

# Environment

You should create a virtualenv with the required dependencies by running
```
make virtualenv
```

When a new requirement is needed you should add it to `unpinned_requirements.txt` and run
```
make update-requirements-txt
```
this ensure that all requirements are pinned and work together for ensuring reproducibility

# Tests

You can run tests by running
```
pytest
```

# Adding/getting data using `dvc`
The file `.dvc/config` contains the configuration of the `dvc` tool. In there you can find where the data are stored remotely (in our case `s3://mantisnlp-cybert`)

Adding data to track using `dvc`:

* `dvc add data/raw` adds the entire folder `data/raw` to the tracking list
* this command creates `raw.dvc` in the `data` folder. In there  you can find a hash, the path to the data and the number of files tracked
* this command also creates an additional `.gitignore` in the `data` folder if it does not exist, adding `/raw` to the list of ignored files

Getting data using `dvc`:
* `dvc pull data/raw` to download all the files tracked in `data/raw`

# Accessing HPC system using `ssh` 
```
ssh <username>@<hostname>
```
  
The directory `data_p105` is where all the data needs to be stored (the project id on the system is `p105` and the environment variable `$DATA_p105` points to the project's data directory)
  
# Submitting jobs on HPC system using `SLURM`
When running under the `CPU` partition:
  
You need to specify the number of tasks per node (number of cores per node). If not specified, the default value is 1
  
In your job script or salloc command you need the option `--ntasks-per-node=<number_of_cores_per_node>`

<br>

The table below shows a few examples:  

| Job resources                        | Interactive job                    | Job script                                                    |
| -------------                        |:-------------:                     | -----:                                                        |
| Job using two cores on one node      |  salloc -N1 --ntasks-per-node=2    | #SBATCH<br> --nodes=1<br> #SBATCH<br> --ntasks-per-node-2     |
| Job using a whole node               | salloc -N1 --ntasks-per-node=40    | #SBATCH<br> --nodes=1<br> #SBATCH<br> --ntasks-per-node=40    |
| Job using four nodes                 |    salloc -N4 --ntasks-per-node=40 | #SBATCH<br> --nodes=4<br> #SBATCH<br> --ntasks-per-node=40    |
  
<br>
<br>
       
When running under the `GPU` partition:
  
The default number of cores assigned to each GPU is the total number of cores per node divided by the total number of GPUs per node i.e. for Cyclone 10 cores are assigned to each GPU so a Cyclone job requesting 2 GPUs will also be allocated 20 cores 
  
In your job script or salloc command you need one of the below options:

`--gres=gpu:<number_of_gpus_per_node>`

`--gpus-per-node=<number_of_gpus_per_node>`

`--gpus=<number_of_gpus_per_job>`
  
<br>  
  
The table below shows a few examples:  

| Job resources                        | Interactive job                                                | Job script                                                    |
| -------------                        |:-------------:                                                 | -----:                                                        |
| Job using two GPUs on one node       |  salloc -N1 --gres=gpu:2                                       | #SBATCH<br> --nodes=1<br> #SBATCH<br>  --gres=gpu:2     |
| Job using all GPUs of a whole node   | salloc -N1 --gpus-per-node=4                                   | #SBATCH<br> --nodes=1<br> #SBATCH<br> --gpus-per-node=4  |
| Job using all GPUs on two nodes      |    salloc -N4 --gpus=8<br> or<br>  salloc -N2 --gpus-per-node=4| #SBATCH<br> --nodes=2<br> #SBATCH<br> --gpus=8<br> or<br> #SBATCH<br> --nodes=2<br> #SBATCH<br>  --gpus-per-node=4 |

# Default memory amounts per core and per GPU
A user can ask for less or more memory per core or per GPU but if not explicitly asked, the default amounts will be given to each job

<br>  

The table below shows the default memory amounts per cluster:

| Cluster                              | Default memory per core (MB)       | Default memory per GPU (MB)   |
| -------------                        |:-------------:                     | -----:                        |
| Cyclone                              |  4800                              | 48000                         |

<br> 

The above defaults can change using the  `--mem-per-cpu=<size[units]>` or  `--mem-per-gpu=<size[units]>` options respectively in your salloc command or in your job script

For example, a CPU job on a Cyclone node needing 10 cores and 2000 MB of memory per core, can be allocated as below:  
`salloc -N1 --ntasks-per-node=10 --mem-per-cpu=2000`
