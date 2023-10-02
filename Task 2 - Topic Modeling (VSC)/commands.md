# Run Script
## CPU
sbatch -A intro_vsc35175 -M genius -t 8:00:00 --ntasks=1 --cpus-per-task=4 --mem-per-cpu=16G --mail-type=END,FAIL --mail-user=joaopdossena@gmail.com get_bertopic_job.slurm

## GPU
sbatch -A intro_vsc35175 -M genius -t 12:00:00 -N 1 -n 4 --gpus-per-node=1 --mem-per-cpu=20G -p gpu_v100 --mail-type=END,FAIL --mail-user=joaopdossena@gmail.com get_bertopic_job.slurm

# Check queue

squeue

# Statistics

