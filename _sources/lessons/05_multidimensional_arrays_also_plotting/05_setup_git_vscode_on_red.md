# Set up GitHub and VS Code on RED Desktop

1. Log into RED Desktop
2. Open a terminal window
3. Create an SSH key by typing the following into the terminal:
   ```bash
   ssh-keygen -t ed25519
   ```
4. [Add the SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account#adding-a-new-ssh-key-to-your-account)
```{tip}
You can get the text of your public key by typing the following into the terminal:

`cat ~/.ssh/id_ed25519.pub`
```

5. Go to your user directory in the terminal (replacing `YOUR_IU_USERNAME` with your actual IU username):
    ``` bash
    cd /N/project/easg690_fall2025/student_work_dirs/YOUR_IU_USERNAME
    ```
6. Clone your course GitHub repository (replacing `YOUR_GITHUB_URL` with the SSH URL of your GitHub repository):
    ``` bash
    git clone YOUR_GITHUB_URL
    ```
7. Open VSCode (Applications->Coding and Editing->VS Code)
8. Complete the initial setup of VSCode
9. Open the folder you just cloned in VSCode (File->Open Folder) and enter `/N/project/easg690_fall2025/student_work_dirs/YOUR_IU_USERNAME/YOUR_REPO_NAME`
10. Create a new directory for Lesson 05.
11. Go to [](./05_warmup.ipynb), download the notebook, and save it in your new Lesson 05 directory; start working on the warmup.

```{tip}
You might want to open this lesson page in Firefox in RED Desktop to make downloading easier.
```




