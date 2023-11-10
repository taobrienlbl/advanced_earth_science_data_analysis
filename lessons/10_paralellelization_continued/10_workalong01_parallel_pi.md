# Madhava pi calculation in parallel
Instructions for parallelizing $\pi$:

1. Get the solution to the $\pi$ calculation from lesson 01 [here](https://github.com/taobrienlbl/advanced_earth_science_data_analysis/blob/4244ad691497d1043f5d82e1b883054da5c582a3/lessons/01_fundamentals/01b_madhava_pi_calculation_SOLUTION.ipynb)
1. put the code in a script and verify that you can run the $\pi$ calculation on one processor on BigRed200
1. apply the concepts from [lesson 09](https://github.com/taobrienlbl/advanced_earth_science_data_analysis/blob/81cca3a98cfa2d0b777d7ccc56716c26877e8de4/lessons/09_parallelization_intro/in_class_solutions/parallel_generate_frames.py) to parallelize the loop that iterates over the $\pi$ terms
1. use the `gather` concept from [lecture](https://github.com/taobrienlbl/advanced_earth_science_data_analysis/blob/spring_2023_iub/lessons/10_paralellelization_continued/gather_example.py) to gather all the $\pi$ terms onto rank 0 and finalize the calculation
1. print the solution as well as `numpy.pi` for comparison