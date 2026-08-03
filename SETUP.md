# Course Repository Setup

Complete these steps before beginning the course exercises.

The goal is to confirm that you can access the course repository, edit its files, and submit your work through GitHub.

Detailed Protégé installation and ontology configuration instructions are provided separately in `exercises/day-1/protege-setup.md`.

## 1. Create a GitHub Account

Create a free GitHub account if you do not already have one:

https://github.com/signup

Remember the email address and username associated with the account. You will use this account throughout the course.

## 2. Open the Course Repository

Navigate to the course repository using the link provided by the instructors.

Make sure you are signed in to GitHub before continuing.

## 3. Fork the Repository

A fork is your own copy of the course repository.

1. Select **Fork** near the upper-right corner of the repository page.
2. Keep the default repository name.
3. Select your personal GitHub account as the owner.
4. Select **Create fork**.

After GitHub creates the fork, the repository address should include your GitHub username.

For example:

```text
https://github.com/YOUR-USERNAME/COURSE-REPOSITORY
```

You should make your changes in this fork rather than in the original course repository.

## 4. Choose How You Will Edit the Files

You may work using one of the following methods.

### Option A: GitHub Codespaces

Codespaces provides a browser-based version of Visual Studio Code and does not require a local installation.

From your fork:

1. Select the green **Code** button.
2. Select the **Codespaces** tab.
3. Select **Create codespace on main**.
4. Wait for the development environment to open.

You may then edit files directly in the browser.

Codespaces usage may be subject to limits established by GitHub for your account.

### Option B: Visual Studio Code on Your Computer

Install the following software:

* Git: https://git-scm.com/downloads
* Visual Studio Code: https://code.visualstudio.com/

From your fork:

1. Select the green **Code** button.
2. Copy the HTTPS repository address.
3. Open Visual Studio Code.
4. Open the Command Palette:

   * Windows or Linux: `Ctrl+Shift+P`
   * macOS: `Command+Shift+P`
5. Select **Git: Clone**.
6. Paste the repository address.
7. Choose a folder on your computer.
8. Open the cloned repository when prompted.

You may also clone the repository from a terminal:

```bash
git clone https://github.com/YOUR-USERNAME/COURSE-REPOSITORY.git
```

Replace `YOUR-USERNAME` and `COURSE-REPOSITORY` with the correct values.

## 5. Confirm That You Can Edit the Repository

Locate the participant setup or test file identified by the instructors.

If no specific file has been designated, create a file in the appropriate participant or submissions directory using your GitHub username:

```text
YOUR-USERNAME.md
```

Add the following information:

```markdown
# Setup Confirmation

- Name:
- GitHub username:
- Participation: In person or online
- Setup completed: Yes
```

Save the file.

Do not include private information, passwords, phone numbers, or personal addresses.

## 6. Commit Your Changes

A commit records a set of changes in the repository.

### In GitHub Codespaces or Visual Studio Code

1. Open the **Source Control** panel.
2. Review the changed files.
3. Enter a brief commit message:

```text
Complete repository setup
```

4. Select **Commit**.
5. Select **Sync Changes** or **Push** to send the commit to GitHub.

### In a Terminal

```bash
git add .
git commit -m "Complete repository setup"
git push
```

The first time you push, GitHub may ask you to sign in through your browser.

## 7. Confirm That the Changes Are on GitHub

Return to your fork in a web browser and refresh the page.

Confirm that:

* Your new or edited file appears in the repository.
* The latest commit message is visible.
* The commit was made under your GitHub account.

If you can see the changes on GitHub, your repository setup is complete.

## 8. Submit Your Work

Some exercises will be submitted through a pull request.

A pull request asks the instructors to review changes from your fork.

When instructed to submit:

1. Commit and push all required files.
2. Open your fork on GitHub.
3. Select **Contribute**.
4. Select **Open pull request**.
5. Confirm that:
   * The base repository is the original course repository.
   * The head repository is your fork.
   * The selected branches are correct.
6. Enter a clear title.
7. Briefly describe what you completed.
8. Select **Create pull request**.

Do not open a pull request until the exercise instructions ask you to do so.
