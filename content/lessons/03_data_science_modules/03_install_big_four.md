# Install the `big_four` conda environment

**Objective:** Set up a conda environment on your own computer with specific python modules installed.

In this step, you will create a new anaconda environment named `big_four` that contains the four major data science modules: `numpy`, `scipy`, `pandas`, and `matplotlib`.  We'll also install the packages needed to run Jupyter notebooks in Visual Studio Code.

## COMPLETE | Instructions:

 1. Open a terminal in Visual Studio Code (View > Terminal)
 2. Create a new conda environment named `big_four` with Python 3.12; type these lines into the terminal:
    ```bash
    mamba create -n big_four python=3.12
    conda activate big_four
    mamba install numpy scipy pandas matplotlib notebook ipykernel
    ```
```{note}
If you get an error that `mamba` is not found, try replacing `mamba` with `conda` in the above commands.
```
```{note}
It may ask you to confirm the installation after those commands; type `Y` and hit Enter to proceed.
```
```{note}
On Windows machines, the above may not work in the terminal, depending on how you installed miniforge.  If so, try the [Miniforge Prompt or Conda Prompt](https://github.com/conda-forge/miniforge?tab=readme-ov-file#condamamba-usable-in-any-terminals) from your Start Menu instead of using the Visual Studio Code terminal.
```
 3. Download the [](03_warmup.ipynb) notebook
 ![Download Notebook](warmup_download.png)
 4. Create a folder named `lesson03` in your course folder in Visual Studio Code, and move the notebook you just downloaded into that folder.
 5. Open the notebook in Visual Studio Code.
    * In the upper right corner of the notebook, you should see a kernel selector that probably says "Select Kernel" or "Python 3" or "base".
    * Click that and select the `big_four` environment you just created.
    ![Kernel Selector](kernel_selector.gif)
 6. Follow the instructions in [](03_warmup.ipynb) to complete the warmup exercise.


These instructions will work if you need to install a new conda environment with different modules at some point; just use a different name and different modules!