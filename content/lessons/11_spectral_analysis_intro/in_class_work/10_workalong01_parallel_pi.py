""" This cell calculates pi via the Madhava-Leibniz series: https://en.wikipedia.org/wiki/Approximations_of_%CF%80#Middle_Ages """

# import MPI
from mpi4py import MPI

# get the communicator
comm = MPI.COMM_WORLD

# get the mpi rank
rank = comm.rank

# set the number of terms per rank
terms_per_rank = int(1e8)

# set the indices for this rank
# set the start and end indices for each rank
start_ind = int(rank * terms_per_rank) + 1
end_ind = int((rank + 1)*terms_per_rank - 1) + 1

# initialize pi to 0
pi_local = 0

# loop from 1 to N, adding terms to pi
# such that pi ~= 4*(1 - 1/3 + 1/5 - 1/7 + 1/9 ... -(-1)**n / (2n - 1))
for n in range(start_ind,end_ind):
    if n == 1:
        term = 1
    else:
        term = -((-1)**n) / (2*n - 1)
    pi_local = pi_local + term

# gather the pi terms on rank 0
pi_parts = comm.gather(pi_local, root = 0)
    
if rank == 0:
    # multiply pi by four to get the final answer
    pi = 4 * sum(pi_parts)

    # print the answer
    print(f"pi = {pi:2.7f}")
    import numpy as np
    print(f"np.pi = {np.pi}")