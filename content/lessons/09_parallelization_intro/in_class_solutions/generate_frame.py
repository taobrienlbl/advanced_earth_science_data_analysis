# use the agg backend (no need for display)
import matplotlib
matplotlib.use('agg')

# import libraries
import matplotlib.pyplot as plt
import xarray as xr
import pandas as pd
import cartopy
import cmocean
import os

def generate_frame(
        i : int,
        input_file = "/N/project/obrienta_startup/datasets/ERA5/ds633.0/e5.oper.an.sfc/202106/e5.oper.an.sfc.128_136_tcw.ll025sc.2021060100_2021063023.nc",
        output_dir = "./animation_frames/"):

        # make sure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # load the data file (chunks=-1 prevents the whole file from loading at once)
        ds_in = xr.open_dataset(input_file, chunks = -1)

        # get the variable at the requested timestep
        tcw = ds_in['TCW'].isel(time = i)

        # turn off inline plotting
        plt.ioff()

        # plot the variable on an orthographic projection centered on
        # Bloomington, IN
        clat = 39.1653
        clon = -86.5264
        projection = cartopy.crs.Orthographic(central_latitude=clat, central_longitude=clon)
        transform = cartopy.crs.PlateCarree()
        fig, ax = plt.subplots(1,1, subplot_kw = dict(projection = projection))

        # plot the data
        tcw.plot(
        ax = ax,
        cmap = cmocean.cm.rain,
        transform = transform,
        vmin = 0,
        vmax = 60,
        )

        # get the time of the timestep
        time = tcw.time

        # convert it to a datetime object
        time_dt = pd.to_datetime(time.values)

        # add a title with a nicely formatted date
        ax.set_title(time_dt.strftime("%Y-%m-%d %H:%M UTC"))

        # add coastlines
        ax.coastlines(alpha = 0.3)

        # save the plot
        output_file = os.path.join(output_dir,f"tcw_{i:05}.png")
        plt.savefig(output_file, dpi = 300, bbox_inches = 'tight')

        # close the plot
        plt.close()
