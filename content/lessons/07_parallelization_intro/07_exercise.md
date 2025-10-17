# Work-along: Animating the weather in parallel

In this exercise, we will develop code to generate an animation, taking advantage of parallelization to make the process fast.

<video src="../../_static/videos/tcw_animation.mp4" controls width="600" controls="controls" muted="muted" class="d-block rounded-bottom-2 border-top width-fit" style="max-height:640px; min-height: 200px"></video>

## 2.1 Developing plot code

In [](./07_warmup.md), you created a function called `generate_frame()` that can generate and save a plot for a given timestep index. If you didn't finish that part in the warmup, do so now.

## 2.2 Testing plot code

Now that we have drafted and tested code for generating a single animation frame, make a module for your plotting code called `generate_frame.py`; put your function in that file (and any necessary imports).

Test your function from the command line by typing the following in the terminal:
```bash
conda activate easg690
cd lessons/07_parallelization_intro/
python3 -c 'import generate_frame; generate_frame.generate_frame(11)'
```

It might not work the first time.  If not, look at the error messages and try to understand what is not working; update `generate_frame.py` until the testing process results in the creation of the expected image file without errors.

## 2.3 Parallelize the plot code

Now we can use `mpi4py` to generate animation frames in parallel! Do the following:

1. Make a new script called `parallel_generate_frames.py`
1. import both `mpi4py` and `generate_frame` in your script
1. use the MPI rank to set which frame to plot
1. use `generate_frame.generate_frame()` to generate the requested frame
1. use `salloc` to get an allocation for one node and 20 processors
1. use `srun` to run `parallel_generate_frames.py` on 20 processors

## 2.4 Make an mp4

Now we'll use `ffmpeg` to generate an animation.  We'll first need to install the `ffmpeg` and `openh264` libraries in conda; run `conda install -c conda-forge ffmpeg openh264 --yes` in your terminal (make sure your `easg690` environment is active when you do.)

Run the following command from your animation directory (e.g., do `cd animation_frames` first):

```bash
ffmpeg -framerate 10 -i tcw_%05d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" tcw_animation.mp4
```


Note that my animation frame filenames have five digits in the frame number, hence the `-i tcw_%05d.png` argument.  If yours has fewer, like two digits, you'll need to modify, e.g.,: `-i tcw_%02d.png`

## 2.5 Going beyond

How could you modify `parallel_generate_frames.py` to generate 100 frames while still only using 10 processors? 

How could you modify `parallel_generate_frames.py` to generate N frames using M processors?
