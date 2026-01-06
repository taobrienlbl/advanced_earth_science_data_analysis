# Work-along: Installing a new Python environment

<div style="max-width:720px"><div style="position:relative;padding-bottom:56.25%"><iframe id="kaltura_player" src='https://cdnapisec.kaltura.com/p/1751071/embedPlaykitJs/uiconf_id/55382703?iframeembed=true&amp;entry_id=1_vmhbleei&amp;config%5Bprovider%5D=%7B%22widgetId%22%3A%221_ca2vfw6v%22%7D&amp;config%5Bplayback%5D=%7B%22startTime%22%3A0%7D'  allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" title="EAS-G 690 Lesson 06 - Intro &amp; Conda Environments" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"></iframe></div></div>

*Use [this link](https://iu.mediaspace.kaltura.com/media/t/1_vmhbleei) if you have issues viewing the above video.*


We'll use the following steps to create a new `conda` environment.

---
*If you are on a UITS machine like RED*
  1. Open a terminal
  1. Load the conda module: `module load conda`
  1. Create a new conda environment: `conda create -p /N/slate/$USER/conda_envs/easg690 python=3.12 --yes`
      * you can optionally replace `$USER` with your IU username; the $USER variable does that automatically
  1. Activate the new environment: `conda activate /N/slate/$USER/conda_envs/easg690`

---

*If you are on a non-UITS machine (**skip this if you did the above steps**)*
  1. Install [`miniforge`](https://github.com/conda-forge/miniforge?tab=readme-ov-file#install)
  1. Open "Miniforge Prompt" from windows (or open your terminal on a mac operating system)
  1. Create a new conda environment: `conda create --yes -n easg690 python=3.12`
  1. Activate the new environment: `conda activate easg690`

---

1. Download this [requirements.yml](https://raw.githubusercontent.com/taobrienlbl/advanced_earth_science_data_analysis/fall_2025_iub/content/lessons/06_advanced_plotting/requirements.yml) file
    * if you are on a UITS or other type of linux machine, you can type this command in the terminal to download it directly: `wget https://raw.githubusercontent.com/taobrienlbl/advanced_earth_science_data_analysis/fall_2025_iub/content/lessons/06_advanced_plotting/requirements.yml`
1. Verify that `requirements.yml` has all the packages you think you'll need
    * add additional packages as needed (edit with VS Code)
    * if you ever need to create a new conda environment or an environment on a different machine, this is a good starting point!
1. Install the packages into the environment: `conda env update --solver libmamba -f requirements.yml`
    * This may take a while, especially if you are on a UITS machine
1. Install the jupyter kernel into the environment: `ipython kernel install --name easg690 --user`
    * (if you already have a kernel with that name, you can change `easg690` to something else)
1. Test that it works
    * open a new notebook in VS Code
    * change the environment in vscode to `easg690`
    * create a sin wave plot to verify that `numpy` and `matplotlib` are working