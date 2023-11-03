import generate_frame
from mpi4py import MPI

# get the 'communicator'
comm = MPI.COMM_WORLD

# get the 'rank' of the process
my_rank = comm.rank

# get the total number of processes
total_ranks = comm.size

# set the amount of work
total_work = 720

# get the amount of work per worker
work_per_worker =  total_work / total_ranks

# set the start and end indices for each rank
start_ind = int(my_rank * work_per_worker)
end_ind = int((my_rank + 1)*work_per_worker - 1)

# print what items we're working on 
print(f"rank {my_rank}/{total_ranks}: [{start_ind}...{end_ind}]")

# loop over this rank's items
for i in range(start_ind, end_ind + 1):
    print(f"rank {my_rank}/{total_ranks}: working on {i}")
    generate_frame.generate_frame(i)