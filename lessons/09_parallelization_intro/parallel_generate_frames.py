from mpi4py import MPI # load the MPI library
import generate_frame # load the generate_frame function

# get the MPI communicator
comm = MPI.COMM_WORLD

# get the rank of the current process
rank = comm.rank

# run the generate_frame function on each process
generate_frame.generate_frame(rank)