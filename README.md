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

# Cyclone

Cyclone is the name of the super computer at the Cyprus Institute. In order to run a job you need to request access by following
this [link](https://hpcfsupport.atlassian.net/servicedesk/customer/portal/3/create/29). Through the process of getting access,
you need to pass over your public key so that you can ssh into the super computer.

Each user is being given a separate user directory. In the home directory there is a project folder with the name `data_p105`, p105
is the project id. This folder is shared among all members of the project. The project folder also has generous quota for saving data
and models so all our work should go there.

If the github repo is not there already, clone and create a virtualenv by running
```
module load Python/3.8.6-GCCcore-10.2.0
make virtualenv
```

You can run your first batch job by running
```
sbatch job.sub
```
you can see the output of the logs in `train.log`

The super has two modes for running jobs

- interactive
- batch

## Interactive

In the interactive model, you connect to a node and run a job by invoking a script as you would normally do. You can connect
to a node using `salloc`, for example
```
salloc --nodes=1 --ntasks-per-node=8 --mem=8000
```
this command connects you to 1 node with 8 cpu codes and 8GB of memory.

Then you can a python script for example,
```
source .env/bin/activate
python cybert/train.py imdb models/ distilbert-base-uncased --max-steps 12
```

You can leave this job running using tmux but this is not recommended for long running jobs. Instead,
it is advised to use a batch job in those cases

## Batch

In batch mode, you need to write a job script that specifies the parameters we passed to `salloc` before
invoking a script. Our `job.sub` script for example is
```
#!/bin/bash

#SBATCH --job-name=test-train
#SBATCH --nodes=1
#SBATCH --gres=gpu:1
#SBATCH --account=p105
#SBATCH --output=train.log

module load Python/3.8.6-GCCcore-10.2.0
source .env/bin/activate
python cybert/train.py imdb models/ distilbert-base-uncased --max-steps 12
```

Since when running batch jobs we lose access to stdout to monitor, we can pass an argument with a filepath
to redirect the output, in this case `train.log`. This script also uses 1 GPU instead of multiple cpus.

More information on how to run jobs here https://hpcf.cyi.ac.cy/documentation/running_jobs.html

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
