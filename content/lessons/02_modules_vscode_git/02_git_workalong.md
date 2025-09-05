 # Git workalong

```{tip}
You may need to install `git`: https://git-scm.com/downloads
```

## Getting started with git

 * setup github and setup your computer for github
    * install [git](https://git-scm.com/downloads)
    * [Signup for a github account](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home) if you don't already have one

      **or** 
    
    * sign in to [github.iu.edu](https://github.iu.edu/) if you do not want to upload your course work to a public github account

    * [add an SSH key to your github account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) if you haven't already
 * Initialize your directory, from the last step, as a git repository: (e.g., run `git init` in a terminal in that folder)
 * Add the two files to the repository: `git add custom_trig.py test_trig.py`
 * Commit the changes and add a log message, e.g.,: `git commit -m "Initial commit; tests of trig functions work as expected"`
 * Create a new private git repository from your github home page (don't click anything below the **Initialize this repository with:** heading)
 ![screenshot of creating a new repository](github_new_repo_screenshot.png)
 * Follow the instructions on github to add the repository and push your commit

## Adding files

 * Add a README.md to your repository, commit it, and push it
 * Download the jupyter notebooks from last class, add them to the repository and push it to github: view the sound notebook on github.com

## Reorganize your repository

 * Reorganize your repository. Make subdirectories for lessons 01 and 02: e.g., `lesson01` and `lesson02` and use `git mv` to move files as appropriate.  Commit and push. (We'll use this repository for in-course work from now on.)
