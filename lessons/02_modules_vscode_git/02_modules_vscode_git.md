# Modules, VSCode, and Git
# URL to this lesson: https://bit.ly/44IbwEM 

*Lecture number:* 02

*Target Date:* 09/01/2023

*Length:* 150 mins

## READ | Lecture Objectives:

* Install & use Anaconda Python and Visual Studio Code
* Write, import, and use a Python module
* Initialize a git repository, commit to it, and push to github

### Relation to course goals:

These goals focus on creating and using modular Python code as a way to improve reusability and reduce bugs (e.g., bugs stemming from reinventing the wheel).

## COMPLETE | Reading and Homework:

* READ | Chapters 4 and 24
* COMPLETE | Homework 02

## PREVIEW | Class Overview:

(25 min) Warmup & last-class refresher
<a target="_blank" href="https://colab.research.google.com/github/taobrienlbl/advanced_earth_science_data_analysis/blob/spring_2023_iub/lessons/02_modules_vscode_git/02_last_class_refresher.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

(45 min) Download and install the following: 

 2. [Anaconda python](https://www.anaconda.com/download)
 3. [Visual Studio Code](https://code.visualstudio.com/download)

(5 min) break

(20 min) Creating a python module - follow-along

 * Create a new directory (e.g `~/learning/eart_sci_data_analysis/`)
 * Open Visual Studio Code in that directory
 * Create a new file called `custom_trig.py`
 * Copy-paste your trig code from last class into the file
 * Create a new file called `test_trig.py` that imports, uses, and tests/verifies the trig functions

(20 min) Initialize, commit, and push with github - follow-along

 * Initialize your directory, from the last step, as a git repository: (e.g., run `git init` in a terminal in that folder)
 * Add the two files to the repository: `git add custom_trig.py test_trig.py`
 * Commit the changes and add a log message, e.g.,: `git commit -m "Initial commit; tests of trig functions work as expected"`
 * setup github and setup your computer for github
    * install [git](https://git-scm.com/downloads)
    * [Signup for a github account](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home) if you don't already have one
    * [add an SSH key to your github account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) if you haven't already
 * Create a new private git repository (don't click anything below the **Initialize this repository with:** heading)
 * Follow the instructions on github to add the repository and push your commit

(5 min) Add a README.md to your repository, commit it, and push it

(5 min) Download the jupyter notebooks from last class, add them to the repository and push it to github: view the sound notebook on github.com

(5 min) Reorganize your repository. Make subdirectories for lessons 01 and 02: e.g., `lesson01` and `lesson02` and use `git mv` to move files as appropriate.  Commit and push. (We'll use this repository for in-course work from now on.)

(20 min) *looking ahead to next week* using the big-four Python data science libraries: `numpy`, `pandas`, `matplotlib`, and `scipy`

 * Goal: examine the relationship between El Nino and minimum winter (Dec-Jan-Feb) temperatures in Bloomington, IN
 * Method:
    * obtain minimum temperature data from [NOAA NClimDiv](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00005), using the *NCEI Direct Download* method
    * read the dataset using `pandas`, filter out data for southern central Indiana
    * convert the data to timeseries format
    * obtain the [ENSO longitude index](https://cascade.lbl.gov/enso-longitude-index-eli/) Excel file and read with `pandas`; convert to timeseries format
    * make the ENSO and NClimDiv timeseries align (same start and end dates, same period - DJF, etc)
    * plot both timeseries
    * plot a correlation
    * do linear regression and correlation analyses
 * For today: go as far with this during class time as possible!



