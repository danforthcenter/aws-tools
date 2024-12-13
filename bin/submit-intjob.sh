#!/bin/bash

# Need to decide how to deal with job file created by this script
# put in some temp folder?

source /apps/miniconda3/etc/profile.d/conda.sh

conda activate base

/apps/src/aws-tools/bin/make-int-job.py "$@" -f $HOME/utils/temp/int-job.sh

qsub -I $HOME/utils/temp/int-job.sh

conda deactivate
