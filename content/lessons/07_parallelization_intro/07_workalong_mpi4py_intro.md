# Work-along: Basic parallelization

## Installing `mpi4py` properly

When we installed `mpi4py` in our conda environment, it was built in a way inappropriate for Quartz; we need to reinstall it.  Open a terminal and do the following:

1. Open a terminal 
1. Make conda available: `module load conda`
1. Activate your environment: `conda activate /N/slate/$USER/conda_envs/easg690`
1. Force reinstallation of `mpi4py`: `MPICC="mpicc" pip install --force-reinstall --no-cache-dir --no-binary=mpi4py mpi4py`

## Drafting the parallel code

First we will draft code that shows the most basic use of the `mpi4py` library, which is one of the primary libraries for coarse-grained parallelism in Python.  Here's a skeleton of the code that we will draft:

```python
# import libraries

# get the 'communicator'

# get the 'rank' of the process

# get the total number of processes

# print the rank

```

In your lesson 07 folder, create a new Python script called `07_workalong.py`.

Paste the code above into the script and follow along; we'll explain each part as we go.


## Running the code on a compute node

Once we draft the code above code, we will need to run on a *compute node* of Quartz. Follow these steps, which assume that you are running VS Code on Quartz already.

1. Open a terminal
1. Activate your class conda environment: `conda activate easg690`
1. Change directory to the location of your script.  For me, my script is in the `lessons/07_parallelization_intro` subdirectory of my repository, so I need to type: `cd lessons/07_parallelization_intro`.  It will be different for you; the important thing is the `cd` command, which changes your directory.
1. Get an interactive allocation:
`salloc -A c01837 -p debug -N 1 -n 9 -t 30`
    * Explanation:
        * `salloc`: command to request an interactive allocation of one or more compute nodes
        * `-A c01837`: use account number c01837 (this is the class's group account; you'll be removed from this at the end of the semester)
        * `-p debug`: use the 'debug' partition
        * `-N 1`: ask for one compute node
        * `-n 9`: ask for exclusive access to up to 9 processors
        * `-t 30`: request a 30 minute allocation
1. Reactivate your conda environment: `conda activate /N/slate/$USER/conda_envs/easg690`
1. Run your code in parallel: `I_MPI_FABRICS=shm srun -n 9 python3 -u 07_workalong.py`
    * Explanation:
        * `I_MPI_FABRICS=shm`: a workaround I had to add...unclear why
        * `srun`: command to execute code on one or more processors
        * `-n 9`: run on 9 processors
        * `python3 07_workalong.py`: use python to execute your script (substitute with your actual script name).
1. Release your allocation (so others can use the node/cpus you requested): `exit`


