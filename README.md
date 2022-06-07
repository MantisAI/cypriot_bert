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

Each user is being given a separate user directory. In the home directory there is a project folder with the name `data_PROJECTID`
which only you have access and has generous quota for saving data and models Your work should be placed there. Thus clone this
repo inside the project folder and create the virtualenv by running
```
module load Python/3.8.6-GCCcore-10.2.0
make virtualenv
```

To queue a job for training run
```
sbatch job.sub
```

You can see the output of the logs in `train.log`

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
