# Deployment Guide — Streamlit Community Cloud

Follow these exact steps to host your dashboard online for free and get a live link to show in your viva/report.

---

## PART 1: Upload Project to GitHub

### Step 1: Create a GitHub account
Go to https://github.com and sign up (skip if you already have an account).

### Step 2: Create a new repository
1. Click the **+** icon (top right) → **New repository**
2. Repository name: `machin-automation-dashboard`
3. Set it to **Public**
4. Do NOT initialize with a README (we already have one)
5. Click **Create repository**

### Step 3: Upload your project files
You have two options:

**Option A: Using GitHub website (easiest, no commands needed)**
1. On your new repository page, click **"uploading an existing file"**
2. Drag and drop these files:
   - `app.py`
   - `requirements.txt`
   - `sample_dataset.csv`
   - `generate_dataset.py`
   - `README.md`
3. Scroll down, write a commit message like "Initial commit"
4. Click **Commit changes**

**Option B: Using Git commands (if Git is installed on your PC)**
Open terminal/command prompt inside your project folder and run:

```bash
git init
git add .
git commit -m "Initial commit - Machin Automation Dashboard"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/machin-automation-dashboard.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your actual GitHub username.

---

## PART 2: Deploy on Streamlit Community Cloud

### Step 1: Sign up
Go to https://share.streamlit.io and sign in using your **GitHub account**.

### Step 2: Create a new app
1. Click **"Create app"** (or "New app")
2. Choose **"Deploy a public app from GitHub"**

### Step 3: Configure the app
- **Repository:** `YOUR-USERNAME/machin-automation-dashboard`
- **Branch:** `main`
- **Main file path:** `app.py`

### Step 4: Deploy
Click **"Deploy!"** and wait 1–3 minutes while Streamlit installs the libraries from `requirements.txt` and launches your app.

### Step 5: Get your live link
Once deployed, you'll get a public URL like:
```
https://machin-automation-dashboard.streamlit.app
```

This is your **live dashboard link** — use this in your internship report and viva.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "ModuleNotFoundError" on deploy | Check `requirements.txt` is uploaded and spelled correctly |
| App shows "File not found: sample_dataset.csv" | Make sure the CSV is uploaded in the same repository as `app.py` |
| App is sleeping / not loading | Streamlit Cloud free apps sleep after inactivity — just reload the page, it wakes up in ~30 seconds |
| Changes not reflecting | Push your updated files to GitHub again; Streamlit Cloud auto-redeploys on every push |

---

## Updating the App Later

Whenever you make changes to `app.py` or the dataset:
1. Upload the updated file to your GitHub repository (overwrite the old one)
2. Streamlit Community Cloud will automatically redeploy within a minute

No need to repeat the entire deployment process.
