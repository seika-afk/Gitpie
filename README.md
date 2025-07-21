# 🧠 GitPie – Instantly Create Repo or Push Any Folder to GitHub

GitPie is a simple Python tool that allows you to instantly turn any folder into a GitHub repo and push code with minimal input.

---

## 🚀 To Run (One-Time Setup)

1. **Clone the repository and navigate into it:**

```bash
git clone https://github.com/yourusername/GitPie.git
cd GitPie
```

2. **Install the required Python packages:**

```bash
pip install -r requirements.txt
```

3. **Get your GitHub Personal Access Token:**

Create one from here:  
👉 https://github.com/settings/tokens (enable `repo` scope)
- Put it into main.py

4. **Run the script:**

```bash
python main.py
```

---

## 🌐 To Use GitPie from Anywhere (Global Command)

Once set up, you can run `gitpie` from any directory in your terminal.

### 🐧 Linux / macOS (Zsh, Bash)

1. **Create a launcher script:**

```bash
vim ~/GitPie/gitpie
```

Paste:

```bash
#!/bin/bash
source ~/GitPie/env/bin/activate
python ~/GitPie/main.py
```

2. **Make the script executable:**

```bash
chmod +x ~/GitPie/gitpie
```

3. **Add GitPie to your global PATH:**

```bash
echo 'export PATH="$HOME/GitPie:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

Now you can just type:

```bash
gitpie
```

...from anywhere! 🎉

---

### 🪟 Windows

1. Open Command Prompt or PowerShell as Administrator

2. Add your GitPie folder path to the system `PATH` variable

3. Create a `.bat` file (e.g., `gitpie.bat`) with this content:

```bat
@echo off
call C:\path\to\GitPie\env\Scripts\activate
python C:\path\to\GitPie\main.py
```

Place this `.bat` file inside a folder that’s already in your system PATH or add it manually.

Now you can run `gitpie` from any terminal window.

4. Or just use Chat GPT. 
---

## Issues:
- If any issue ,put them in Issues section.
