# GitPie

GitPie is a small Python CLI that lets you create a GitHub repository and push any local folder to it with minimal setup.

## Setup

Clone the repo:

```bash
git clone https://github.com/yourusername/GitPie.git
cd GitPie
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a GitHub Personal Access Token with the **repo** scope:

https://github.com/settings/tokens

Add the token to `main.py`.

Run:

```bash
python main.py
```

---

## Optional: Use it as a global command

### Linux / macOS

Create a launcher script:

```bash
#!/bin/bash
source ~/GitPie/env/bin/activate
python ~/GitPie/main.py
```

Save it as `gitpie`, make it executable:

```bash
chmod +x gitpie
```

Move it somewhere in your `PATH` (or add its directory to your `PATH`):

```bash
sudo mv gitpie /usr/local/bin/
```

Now you can run:

```bash
gitpie
```

from anywhere.

### Windows

Create a `gitpie.bat` file:

```bat
@echo off
call C:\path\to\GitPie\env\Scripts\activate
python C:\path\to\GitPie\main.py
```

Place it in a directory that's included in your system `PATH`.

---

## Issues

If you run into a bug or have a feature request, open an issue.
