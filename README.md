# About this repository

This is the source for [Advanced Earth Science Data Analysis](https://obrienta.pages.iu.edu/courses/adv_eart_sci_data_analysis_fall_2025/); information about the course can be found there.  Instructions below are for getting started with adapting/modifying the course (e.g., for the instructor or for someone who wants to duplicate and build on these course materials).

# Building the course website

1. Clone this repository: `git clone https://github.com/taobrienlbl/advanced_earth_science_data_analysis`
2. Obtain and install [uv](https://docs.astral.sh/uv/getting-started/installation/) (a lightweight python package manager)
3. Enter the repo directory and run `uv sync` to set up the python environment: `cd advanced_earth_science_data_analysis && uv sync`
4. Build the html for the course: `uv run jb build content`; follow the instructions in the terminal to open the course html in a browser
5. Edit source files in content (see `content/_toc.yml` for a list of the files currently in the ebook; add files to `_toc.yml` as needed) and then rebuild the html source (step 4) when files are updated

The course presently uses [jupyter {book}](https://jupyterbook.org/en/stable/start/your-first-book.html) to manage rendering content; there is extensive documentation on the site about the MyST markdown language, which is used for the `*.md` files.  Course sections also utilize `*.ipynb` files, which are jupyter notebooks.  Instructions for using/running those notebooks will be added to the course content as it is developed.

# The python environment

The `uv` package manager is used to ensure that all python libraries needed to run code in the course's notebooks are installed.  Usually you shouldn't need to worry about this. The `uv.lock` file contains the list of all python pacakges needed, and as long as that is kept up to date, any time the `uv run` command is used, `uv` ensures that all required packages are installed (and installs them as needed).