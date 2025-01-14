#!/bin/bash

source /apps/miniconda3/etc/profile.d/conda.sh

conda activate base

python /apps/src/aws-tools/bin/submit-intjob.py "$@" 

conda deactivate
