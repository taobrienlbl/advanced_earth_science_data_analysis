# Exercise: Madhava pi calculation in parallel
Instructions for parallelizing $\pi$:

1. Get the solution to the $\pi$ calculation from lesson 01 [here](../01_fundamentals/01b_madhava_pi_calculation_SOLUTION.ipynb)
1. put the code in a script and verify that you can run the $\pi$ calculation on one processor on BigRed200
1. apply the concepts from [lesson 07](../07_parallelization_intro/07_parallelization_intro.md) to parallelize the loop that iterates over the $\pi$ terms
1. use the `gather` concept from [lecture](./10_bcast_gather.md) to gather all the $\pi$ terms onto rank 0 and finalize the calculation
1. print the solution as well as `numpy.pi` for comparison