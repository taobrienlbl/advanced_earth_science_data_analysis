# Final Project Proposal

## What do I need to do?

Submit a 3--5 page proposal describing your final project, written in [markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) (e.g., the file should be called something like `project_proposal.md`) and placed in a `final_project` folder in your github repository.  The target audience should be your peers in class.  

The proposal should include:

1. an introduction to the problem, similar to what you would find in a peer-reviewed paper: including background information, context, references, a statement of what has been done, etc.
2. an overview of what your final project will accomplish
3. a timeline for completing the various stages of the project, both within class time and outside of class time
    * assume that the last 6 weeks of lab (at least) will have an hour or more of time devoted to working on your project
    * include parts that have already been accomplished as well as parts that need to be done and the dates by which you will target completing them
4. a mockup (e.g., sketch) of your main publication-quality figure


For the timeline, use markdown's checkbox feature so that you can mark items as 'complete' as you progress, i.e.:

```markdown
## Example project timeline
- [x] (Oct 13) write code to read in seismometer data files
- [ ] (Oct 20) write and test function `extract_earthquakes()` to extract individual earthquakes from data
- [ ] (Oct 27) write and test function `estimate_magnitude()` to estimate the magnitude of each earthquake
- [ ] (Nov 4) write code to run magnitude estimation in paralell on multiple seismometer data files
... etc.
```

This will render in github as:
## Example project timeline
- [x] (Oct 13) write code to read in seismometer data files
- [ ] (Oct 20) write and test function `extract_earthquakes()` to extract individual earthquakes from data
- [ ] (Oct 27) write and test function `estimate_magnitude()` to estimate the magnitude of each earthquake
- [ ] (Nov 4) write code to run magnitude estimation in paralell on multiple seismometer data files


## What is the final project?
As a reminder, for your [final project](https://iu.instructure.com/courses/2166341/assignments/15482432), you will need to submit a link to your github repository containing one or more notebooks documenting a final project.  Quoting from the final project description, the projects will: 

> * use pervasive comments throughout
> * use markdown cells to orient a viewer to the analysis and to explain steps along the way
> * use python cells to demonstrate to the viewer that the various sections of the notebook (e.g., reading of the data) are doing what is expected
> * use custom python modules that you write or custom functions
> * demonstrate proficiency in common data analysis tasks
> * document the custom code with docstrings and pervasive comments; somebody else should be able to understand how to use the code
> * use machine learning and/or parallelization in the analysis
> * contain at least one publication-quality plot along with caption & analysis in a markdown cell
> * if you submit multiple notebooks, your final project folder should contain a README.md markdown file that explains the contents of each file

Assignments that receive high grades will have the following attributes:

* is clear, error-free, readable, and well-commented
* demonstrates modular and reusable coding (custom functions, modules, etc.)
* demonstrates proficiency in common data analysis tasks: reading/writing data, diagnostic plots, etc.
* incorporates machine learning or parallelization
* contains at least one publication quality plot displaying multiple types of information
