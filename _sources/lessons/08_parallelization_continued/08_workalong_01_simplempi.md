# Work-along: Using `simplempi`

<div style="max-width:720px"><div style="position:relative;padding-bottom:56.25%"><iframe id="kaltura_player" src='https://cdnapisec.kaltura.com/p/1751071/embedPlaykitJs/uiconf_id/55382703?iframeembed=true&amp;entry_id=1_7jt0n1ou&amp;config%5Bprovider%5D=%7B%22widgetId%22%3A%221_diojlus4%22%7D&amp;config%5Bplayback%5D=%7B%22startTime%22%3A0%7D'  allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" title="EAS-G 690 - Lesson 08 - simplempi" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"></iframe></div></div>

*Use [this link](https://iu.mediaspace.kaltura.com/media/t/1_7jt0n1ou) if you have issues viewing the embeded video above.*

For this exercise, we will build on the excercise from last class, using the `simplempi` package.

1. Open a terminal
1. Activate your conda environment
    * `module load conda`
    * `conda activate /N/slate/$USER/conda_envs/easg690`
1. Install simplempi: `pip install simplempi`
1. Make a copy of your code from [](../07_parallelization_intro/07_exercise.md)
1. Modify the code to use `simplempi` to loop over timesteps to generate a longer animation