# *Collective communications* with MPI

## Embarrassingly parallel algorithms

In the example in [](./08_workalong_01_simplempi.md), no communication was needed among the copies of `parallel_generate_frames.py`.  This type of algorithm (an algorithm being a set of steps to complete a task) is referred to as *embarrassingly parallel*.  The key feature of *embarrassingly parallel* algorithms is that no communication is needed among copies of the code that run in parallel.  In the case of looping over frames, the generation of each frame is independent of the generation of every other frame, so no coordination or communication was needed.  `simplempi` is designed specifically to make it easy to run parallelize embarrassingly parallel `for` loops.

## Collective communications 

But what if an algorithm needs some sort of communication or coordination to complete?  What types of communication or coordination are there?

MPI defines several common types of *collective communication* that can be used to coordinate parts of an algorithms (see [here](https://mpitutorial.com/tutorials/mpi-broadcast-and-collective-communication/) for more detail), two of which we'll focus on here:
* *broadcast* - one copy of the code sends a copy of some data to all other copies of the code
* *gather* - all copies of the code send some copy of data to an individual copy (usually `rank=0`)

## Broadcast and Gather

### Broadcasting data

In the `generate_frame.py` code from [](../07_parallelization_intro/07_exercise.md), the function opened the same file multiple times.  When running with a large number of ranks, that may not be desireable, since each copy will try to access the file at approximately the same time; but to a good approximation, only one rank can access the file at a given time.  That doesn't matter for small parallel jobs, but when the number of ranks is large, there can be delays while individual ranks wait to access the data.

A solution would be to have one copy (e.g., `rank=0`) read the file and then *broadcast* the contents of the file to all the other ranks; that way the file is only read once.

Consider the following example.  Let's pretend that the creation of the variable `full_list` represents reading from a file (e.g., `full_list` is what one would get if they read our hypothetical file).

Only if `rank=0` does the file get 'read'; otherwise the variable `full_list` is simply intiailized to something (in this case I arbitrarily chose `None`).

```python
#!/usr/bin/env python3

# import MPI
from mpi4py import MPI

# get the communicator
comm = MPI.COMM_WORLD

# get the mpi rank
rank = comm.rank

if rank == 0:
    # (represents reading a file from a list like in the example above)
    full_list = list(range(100))
else:
    full_list = None

# broadcast the list; this copies full_list to all the other processes
my_list = comm.bcast(full_list, root=0)

# print the list
print(f"{rank}: {my_list}")
```

Try this example on your own:

1. Copy the code above into a file (e.g., `broadcast_example.py`)
1. Use `salloc` to get on a node (make sure to activate your conda environment)
1. Use `srun` to run the script in parallel

### Gathering data

What about gather; why might this be needed?

Consider, for example, if you were to have each rank read in a unique subset of timesteps from the data file we animated in the last class.  Instead of animating the data, what if we wanted to calculate the global spatial average of the variable and then average that in time?

To calculate the average, you could have one copy (e.g., `rank=0`) gather the spatial averages for each timestep and then calculate the temporal average.

Consider the following example below. Let's pretend that the line `my_number = rank` represents the result of calculating the spatial average for one timestep.  The code then gathers all of the versions of `my_number` to `rank=0`, and then only `rank=0` calculates the average across all versions of `my_number`.


```python
#!/usr/bin/env python3

# import MPI
from mpi4py import MPI

# get the communicator
comm = MPI.COMM_WORLD

# get the mpi rank
rank = comm.rank

# set the individual result for each rank
my_number = rank

# gather the results on rank 0
full_list = comm.gather(my_number, root=0)

# calculate the average rank; only rank 0 can do this
if rank == 0:
    avg_rank = sum(full_list) / len(full_list)
else:
    avg_rank = None

# print the list
print(f"{rank}: {full_list}, avg_rank = {avg_rank}")
```

Again, test this code out on your own.