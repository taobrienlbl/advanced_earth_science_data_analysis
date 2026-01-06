# Workalong: Madhava pi calculation in parallel
<div style="max-width:720px"><div style="position:relative;padding-bottom:56.25%"><iframe id="kaltura_player" src='https://cdnapisec.kaltura.com/p/1751071/embedPlaykitJs/uiconf_id/55382703?iframeembed=true&amp;entry_id=1_bq9y97lx&amp;config%5Bprovider%5D=%7B%22widgetId%22%3A%221_ebfxdkcs%22%7D&amp;config%5Bplayback%5D=%7B%22startTime%22%3A0%7D'  allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" title="EAS-G 690 - Lesson 08 Parallel Madhava Pi" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"></iframe></div></div>

*Use [this link](https://iu.mediaspace.kaltura.com/media/t/1_bq9y97lx) if you have issues with the above embeded video.*

Instructions for parallelizing $\pi$:

1. Get the solution to the $\pi$ calculation from lesson 01 [here](../01_fundamentals/01b_madhava_pi_calculation_SOLUTION.ipynb)
1. put the code in a script and verify that you can run the $\pi$ calculation on one processor on BigRed200
1. apply the concepts from [lesson 07](../07_parallelization_intro/07_parallelization_intro.md) to parallelize the loop that iterates over the $\pi$ terms
1. use the `gather` concept from [](./08_collective_communications.md) to gather all the $\pi$ terms onto rank 0 and finalize the calculation
1. print the solution as well as `numpy.pi` for comparison