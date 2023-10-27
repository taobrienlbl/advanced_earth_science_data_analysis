# import libraries
from mpi4py import MPI # load MPI
import numpy as np

# get the 'communicator'
comm = MPI.COMM_WORLD

# get the 'rank' of the process
my_rank = comm.rank

# get the total number of processes
total_ranks = comm.size

# print the rank
print(f"I am {my_rank} of {total_ranks}. I am borg.")