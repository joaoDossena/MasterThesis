#!/usr/bin/env bash

module purge

echo -e "Exporting miniconda3/bin to PATH environment variable...\n"
export PATH="${VSC_DATA}/miniconda3/bin/:${PATH}"
source ${VSC_DATA}/miniconda3/bin/activate
conda init bash
source ${VSC_HOME}/.bashrc
echo -e "\n\nConda environment list BEFORE activating rapids-23.04\n"
conda env list
conda activate rapids-23.04
echo -e "\n\nConda environment list AFTER activating rapids-23.04\n"
conda env list
echo -e "\n\nPackages in rapids-23.04:\n"
conda list -n rapids-23.04



echo -e "\n\nRunning python script...\n\n\n"
python gpu_bertopic_full.py
