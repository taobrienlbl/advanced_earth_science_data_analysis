# Homework 4b: Get set up with RED Desktop

**Complete all the following steps to get set up for next class.**

```{note}
Read and follow the linked instructions *very carefully*.
```

1. Get set up with IU Research Computing accounts: [instructions here](https://uits.iu.edu/services/accounts-and-email/research/index.html)
  * Set up accounts for Quartz, Slate, slate-project, and Big Red 200
  * Some of the forms will ask you whether you need to store HIPPA data (health-related data); answer "no" to this question, unless you have another role on campus that requires you to handle HIPPA data
2. Download, install, and configure ThinLinc to connect to RED Desktop: [instructions here](https://servicenow.iu.edu/kb?id=kb_article_view&sysparm_article=KB0023162)
3. Read about [RED Desktop](https://servicenow.iu.edu/kb?id=kb_article_view&sysparm_article=KB0023170) and how to use it
  
  <div style="max-width:720px"><div style="position:relative;padding-bottom:56.25%"><iframe id="kaltura_player" src='https://cdnapisec.kaltura.com/p/1751071/embedPlaykitJs/uiconf_id/55382703?iframeembed=true&amp;entry_id=1_cxw3fm5r&amp;config%5Bprovider%5D=%7B%22widgetId%22%3A%221_hsny65u8%22%7D&amp;config%5Bplayback%5D=%7B%22startTime%22%3A0%7D'  allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" title="EAS-G 690 Homework 04b - Setting Up RED Desktop" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"></iframe></div></div>

4. Connect to RED Desktop using ThinLinc
5. Open the Terminal application from the RED Desktop
  * Copy this command and paste it into the Terminal window: `/N/project/easg690_fall2025/.conda/easg690_shared/bin/python -m ipykernel install --user --name easg690_shared --display-name "EASG690 Shared"`
  * (The above command sets up a kernel for Jupyter notebooks that uses the shared conda environment we will use for the rest of the course.)
6. Open JupyterLab from the RED Desktop
7. In JupyterLab, create a new notebook using the "EASG690 Shared" kernel
8. Make a plot of a sine wave in the notebook to verify that everything is working
9. Screenshot your RED Desktop window with the sine wave plot visible in the Jupyter notebook
10. Submit the screenshot to the assignment on Canvas

```{tip}
If you have any trouble with any of the steps, please reach out on the course Slack.
```

```{note}
Due date and submission details can be found in [Canvas](https://iu.instructure.com/courses/2330390/assignments/18106098).
```