# Work-along: Basic parallelization

Here is the code for the solution:
```python
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
```

And here a sample of output when it is run; note that the order can--and likely will--change each time this is executed, since MPI doesn't guarantee which rank finishes in what order.

```bash
$ salloc -A r00389 -p debug -N 1 -n 9 -t 30
$ srun -n 9 python3 -u 07_workalong_01_mpi4py_intro.py
I am 7 of 9. I am borg.
I am 2 of 9. I am borg.
I am 0 of 9. I am borg.
I am 3 of 9. I am borg.
I am 5 of 9. I am borg.
I am 4 of 9. I am borg.
I am 1 of 9. I am borg.
I am 6 of 9. I am borg.
I am 8 of 9. I am borg.
```