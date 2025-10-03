# Advanced Plotting

**Making publication-quality plots with matplotlib and cartopy**

```{note}
URL to this lesson: https://go.iu.edu/8vCW
```

*Lecture number:* 06

*Target Date:* 10/03/2025

*Length:* 150 mins

## READ | Lecture Objectives:

* manage multiple conda environments using `mamba`
* generate concise, readable multipanel plots
* plot map-based data

### Relation to course goals:

This lesson contributes directly toward the course goal
* generate informative publication-quality plots

There is also a somewhat tangential goal of managing python environments: not exactly a data analysis skill but critical for being able to use python.

## COMPLETE | Reading and Homework:

* COMPLETE | Homework 06

## PREVIEW | Class Overview:

(10 min) [](./06_python_environments.md)

<div style="max-width:720px"><div style="position:relative;padding-bottom:56.25%"><iframe id="kaltura_player" src='https://cdnapisec.kaltura.com/p/1751071/embedPlaykitJs/uiconf_id/55382703?iframeembed=true&amp;entry_id=1_vmhbleei&amp;config%5Bprovider%5D=%7B%22widgetId%22%3A%221_ca2vfw6v%22%7D&amp;config%5Bplayback%5D=%7B%22startTime%22%3A0%7D'  allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" title="EAS-G 690 Lesson 06 - Intro &amp; Conda Environments" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"></iframe></div></div>

Use [this link](https://iu.mediaspace.kaltura.com/media/t/1_vmhbleei) if you have issues viewing the above video.

(30 min) (while the above completes) [](../05_multidimensional_arrays_also_plotting/05_multidimensional_array_exercise.ipynb)

<div style="max-width:720px"><div style="position:relative;padding-bottom:56.25%"><iframe id="kaltura_player" src='https://cdnapisec.kaltura.com/p/1751071/embedPlaykitJs/uiconf_id/55382703?iframeembed=true&amp;entry_id=1_vmhbleei&amp;config%5Bprovider%5D=%7B%22widgetId%22%3A%221_ca2vfw6v%22%7D&amp;config%5Bplayback%5D=%7B%22startTime%22%3A0%7D'  allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" title="EAS-G 690 Lesson 06 - Intro &amp; Conda Environments" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"></iframe></div></div>

Use [this link](https://iu.mediaspace.kaltura.com/media/t/1_bn1zhqc2) if you have issues viewing the above video.


(45 min) [](./06_workalong01_advanced_plotting.ipynb)

<div style="max-width:720px"><div style="position:relative;padding-bottom:56.25%"><iframe id="kaltura_player" src='https://cdnapisec.kaltura.com/p/1751071/embedPlaykitJs/uiconf_id/55382703?iframeembed=true&amp;entry_id=1_pawh17c6&amp;config%5Bprovider%5D=%7B%22widgetId%22%3A%221_chyftbz7%22%7D&amp;config%5Bplayback%5D=%7B%22startTime%22%3A0%7D'  allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" title="EAS-G 690 Lesson 06 - Advanced Plotting 01" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"></iframe></div></div>

Use [this link](https://iu.mediaspace.kaltura.com/media/t/1_pawh17c6) if you have issues viewing the above video.

```{note}
The above video ends with me being confused about why the `seaborn-v0_8` matplotlib plot style is behaving differently from what I expected.  The reason is that I was intending to use `seaborn-v0_8-poster` instead, which is a different style!  At the top of the notebook, change `mpl.style.use('seaborn-v0_8')` to `plt.style.use('seaborn-v0_8-poster')` to get the intended style.
```

(45 min) [](./06_workalong02_mapping.ipynb)

<div style="max-width:720px"><div style="position:relative;padding-bottom:56.25%"><iframe id="kaltura_player" src='https://cdnapisec.kaltura.com/p/1751071/embedPlaykitJs/uiconf_id/55382703?iframeembed=true&amp;entry_id=1_cle46lou&amp;config%5Bprovider%5D=%7B%22widgetId%22%3A%221_494vmbj8%22%7D&amp;config%5Bplayback%5D=%7B%22startTime%22%3A0%7D'  allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" title="EAS-G 690 Lesson 06 - Advanced Plotting 02" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"></iframe></div></div>

Use [this link](https://iu.mediaspace.kaltura.com/media/t/1_cle46lou) if you have issues viewing the above video.

