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
1. Using a job script where `#SBATCH -A p105` need to be added to our job script
2. Using an interactive job where `-A p105` will need to be added to our salloc command (e.g. `salloc -A p105 -N1 --ntasks-per-node=40` for a job to use a whole node, all its 40 cores)


