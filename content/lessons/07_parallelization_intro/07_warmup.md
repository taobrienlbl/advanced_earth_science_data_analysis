# WARMUP | Advanced Plotting & Functions

<video src="../../_static/videos/tcw_animation.mp4" controls width="600" controls="controls" muted="muted" class="d-block rounded-bottom-2 border-top width-fit" style="max-height:640px; min-height: 200px"></video>

In the next 60 minutes, you will create a function that can generate frames for an animation like the one above.  Later in the lesson, we'll use this function to demonstrate parallelization with `mpi4py`.

For context, the plot shows total atmospheric water (*precipitable water* is the technical term), which is a good way to look at [atmospheric rivers](https://www.noaa.gov/stories/what-are-atmospheric-rivers).

## 1. Make a nice plot

1. Create a notebook in your lesson 07 folder.
2. Make a plot that looks as close as possible to the above plot.
   * Use `xarray` to read the data file `/N/project/easg690_fall2025/data/ERA5/ds633.0/e5.oper.an.sfc/202106/e5.oper.an.sfc.128_136_tcw.ll025sc.2021060100_2021063023.nc`
    * the variable name in the file is `TCW`
    * select a specific timestep by index using `xarray`'s `isel()` method
   * Use `matplotlib`, `cartopy`, and `cmocean` to make the plot pretty
   * Save the figure as a 300 dpi PNG file
   * *Hint: the plot uses an Orthographic projection, and the center latitude and longitude correspond to Bloomington, IN* 
3. Make sure to comment your code thoroughly!

## 2. Make a plotting function

Now you're going to write a function that can generate and save an image, like the one you just created, for an arbitrary timestep in the file.

1. In the same notebook, create a function called `generate_frame()` that takes three arguments:
    * `i` - the timestep index to plot
    * `input_file` - the file from which to get data
    * `output_dir` - the directory to which to save the image
2. Copy the code that you wrote into the function as a starting point
3. Test that the function works as expected; revise the function until it does
    * *Hints:*
        * You can use a command like `os.makedirs(output_dir, exist_ok=True)` to ensure that the output directory exists before you try to save files to it.
        * Add `plt.ioff()` at the start of your function to prevent figures from displaying in the notebook when the function is called.
        * Add `plt.close()` at the end of your function (after `plt.savefig()` is called) to prevent memory issues when generating many figures.
4. Commit and push the notebook to your GitHub repo