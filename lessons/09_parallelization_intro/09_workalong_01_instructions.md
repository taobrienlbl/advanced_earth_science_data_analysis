Once we draft the code or the first workalong in this lesson, we will need to run on a *compute node* of BigRed200. Follow these steps, which assume that you are running VS Code on BigRed200 already.

1. Open a terminal
1. Activate your class conda environment: `conda activate easg690`
1. Get an interactive allocation:
`salloc -A r00389 -p debug -N 1 -n 10 -t 30`
    * Explanation:
        * `salloc`: command to request an interactive allocation of one or more compute nodes
        * `-A r00389`: use account number r00389 (this is Travis's research group account; you'll be removed from this at the end of the semester)
        * `-p debug`: use the 'debug' partition
        * `-N 1`: ask for one compute node
        * `-n 10`: ask for exclusive access to up to 10 processors
        * `-t 30`: request a 30 minute allocation
1. Run your code in parallel: `srun -n 10 python3 -u MY_SCRIPT_NAME.py`
    * Explanation:
        * `srun`: command to execute code on one or more processors
        * `-n 10`: run on 10 processors
        * `python3 MY_SCRIPT_NAME.py`: use python to execute your script (substitute with your actual script name).
1. Release your allocation (so others can use the node/cpus you requested): `exit`


