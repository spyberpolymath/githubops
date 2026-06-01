# 🐙 GitHub Ops Protocol & Organization Manager

<div align="center">

**An immersive, cyberpunk-styled terminal application and organization automation suite designed to streamline multi-repository operations, selective batch pushing, and large-scale organization synchronization.**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub API](https://img.shields.io/badge/GitHub--API-v3-blue?style=flat&logo=github)](https://docs.github.com/en/rest)

*Streamline massive workspace Git operations with neon-hued aesthetics, responsive glitch UI indicators, and robust multi-repo handlers.*

[Features](#-features) • [Workspace Architecture](#%EF%B8%8F-workspace-architecture) • [Prerequisites](#-prerequisites) • [Installation](#-installation) • [Usage Guide](#-usage-guide) • [Configuration](#-configuration) • [Technical Reference](#-technical-reference)

</div>

---

## 🎯 Project Overview

Managing multiple independent projects or massive organizational portfolios on GitHub often results in operational overhead—requiring repetitive directory hopping, tedious staging routines, and manual credentials configurations.

**GitHub Ops Protocol** simplifies this workflow by bundling two automated systems:
1. **`githubops.py` (The Interactive Protocol)**: A cyberpunk-themed CLI dashboard equipped with live ANSI text rendering, glitch animations, and batch processing mechanisms. It scans workspace paths, tracks file changes, presents structured public/private trees, and allows selective or bulk staging, committing, and pushing.
2. **`github_org_manager.py` (The Org Manager)**: A specialized, background synchronization utility that uses `PyGithub` to manage all repositories under a target GitHub Organization (e.g. `lovosistechnology`). It automatically pulls changes, handles private token cloning, removes corrupted or incomplete clones, and manages connection retries natively.

---

## ✨ Features

### 🌈 Cyberpunk Terminal Engine (`githubops.py`)
- **Immersive Glitch UI**: Uses `CyberColors` ANSI sequences to draw glowing neon loading loops, text animations, and terminal layouts.
- **Dynamic Workspace Scanning**: Recursively scans paths (e.g., your username folder) to locate active `.git` tracking indicators.
- **Smart Stash & Selection**: Allows pushing to a single repo, multiple comma-separated IDs (e.g., `1,3,5`), all checked repositories, or only repositories with modified working files.
- **Interactive Staging**: Choose between bulk commit messages or individual commit logs per repository before pushing.

### 🏢 Org Portfolio Automator (`github_org_manager.py`)
- **PyGithub Direct Binding**: Securely queries the GitHub API using Personal Access Tokens (classic classic-auth) to fetch organization inventories.
- **Resilient Retry Framework**: Retries interrupted actions (up to `MAX_RETRIES` times) with dynamic sleep increments to survive network fluctuations.
- **Corrupted Clone Healing**: Inspects directories; if a directory exists but its internal `.git` database is corrupted or missing, the tool automatically purges the directory and starts a fresh clone.
- **Shallow Clone Processing**: Clones repositories with a `--depth 1` shallow command to dramatically speed up initial synchronization across vast directories.

---

## ⚙️ Workspace Architecture

```mermaid
graph TD
    A["User Bootstraps Tools"] --> B{"Choose Dashboard"}
    
    B -->|1. githubops.py| C["Scan local directory trees"]
    B -->|2. github_org_manager.py| D["Connect to GitHub Organization API"]
    
    C -->|Detect changes| E["Interactive Selection Menu"]
    E -->|Select target repos| F["Cyberpunk Staging & Push Engine"]
    F -->|Run git subprocesses| G["Push commits to user repositories"]
    
    D -->|Fetch repo manifest| H["Cloning & Sync Loop"]
    H -->|Directory has folder but no .git| I["Purge Broken Folder"]
    H -->|New remote repository| J["Shallow Clone via Token Authorization"]
    H -->|Existing active repository| K["Execute git pull updates"]
    
    I & J & K --> L["Save under Organization Root Folder"]
```

---

## 🚀 Installation & Prerequisites

### 📋 Prerequisites
- **Python 3.8+**
- **Git** command-line tools configured on your system's global environment variables (**PATH**).
- A GitHub **Personal Access Token (PAT)** with full `repo` scopes.

---

### 🛠️ Setup

**1️⃣ Clone the repository:**
```bash
git clone https://github.com/spyberpolymath/githubops.git
cd githubops
```

**2️⃣ Install Dependencies:**
```bash
pip install -r requirements.txt
```

> [!NOTE]
> Major python dependencies include:
> - `requests` (Handling general HTTP protocols)
> - `PyGithub` (Object-oriented GitHub API bindings for Python)
> - `python-dotenv` (Local environment variable configurations)

---

## 📖 Usage Guide

### Protocol 1: Cyberpunk Interactive CLI (`githubops.py`)

Launch the hacker UI:
```bash
python githubops.py
```

```text
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
▌                     GITHUB OPS PROTOCOL v2.0                      ▐
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
[SYS_BOOT] >> Protocol initialized

Select operation:
  1. Clone repositories
  2. Push repositories

>>> 
```

- **Selection Option 1 (Clone)**: Authenticates with your token, fetches your remote lists, checks their privacy states, formats them neatly into `username/public/` or `username/private/` trees on your disk, and clones them.
- **Selection Option 2 (Push)**: Scans folders, finds altered files, prompts you to select repositories via numbers, inputs your commit logs, and pushes everything in parallel-safe order.

---

### Protocol 2: Organization Synchronizer (`github_org_manager.py`)

Run the background synchronizer:
```bash
python github_org_manager.py
```

- **Selection Option 1 (Clone New)**: Queries the Target Organization (`lovosistechnology`), matches local files, filters new items, removes broken fragments, and shallow-clones updates.
- **Selection Option 2 (Update All)**: Loops through all folders inside the organization root directory, executing `git pull` across all active codebases sequentially.

---

## ⚙️ Configuration

Set up your `.env` configuration file in the project's root folder:

```env
GITHUB_USERNAME=spyberpolymath
GITHUB_TOKEN=ghp_yourSecureGitHubAccessTokenClassicOrFineGrained
```

> [!IMPORTANT]
> The classic access token MUST have the `repo` scope enabled. To generate one:
> 1. Log in to GitHub and visit [Settings > Developer Settings > Personal Access Tokens (Classic)](https://github.com/settings/tokens).
> 2. Click **Generate new token (classic)**.
> 3. Check the **repo** scopes (enables control over private and public repositories).
> 4. Copy the generated string directly into your `.env` or the script prompt.

---

## 🏗️ Project Structure

```text
githubops/
│
├── githubops.py            # Cyberpunk-styled interactive push & clone CLI
├── github_org_manager.py   # Bulk PyGithub organization crawler and synchronizer
├── requirements.txt        # Package dependencies (requests, PyGithub, python-dotenv)
├── .gitignore              # Patterns to prevent staging environment secrets
├── LICENSE                 # MIT License
└── README.md               # Advanced project instructions and reference sheet
```

---

## 🛠️ Technical Reference

### CyberColors Palette Class (`githubops.py`)
ANSI color palettes are mapped manually inside the script for lightweight, dependency-free rendering:

```python
class CyberColors:
    NEON_CYAN = '\033[96m'
    NEON_MAGENTA = '\033[95m'
    NEON_GREEN = '\033[92m'
    NEON_PINK = '\033[38;5;205m'
    NEON_YELLOW = '\033[93m'
    NEON_RED = '\033[91m'
    DARK_CYAN = '\033[38;5;23m'
    DARK_GRAY = '\033[38;5;240m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
```

### Core Functions
- `glitch_effect(text, color, iterations)`: Renders glitched ASCII strings by temporarily swapping random letters with block symbols (`█`, `▓`) using a dynamic clock delay.
- `get_local_repositories(base_path)`: Scans subdirectories for valid `.git` configuration trees, executing status validations to check if they have uncommitted file changes.
- `clone_new_repos()`: Utilizes token insertion in URL sequences (`https://<token>@github.com/<org>/<repo>.git`) to clone private repositories securely.

---

## 🤝 Contributing

1. Fork the project.
2. Create your branch (`git checkout -b feature/amazing-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a Pull Request.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🏷️ Footer

<div align="center">

**👨‍💻 Aman Anil** (aka **SpyberPolymath**)

*Crafting digital experiences with passion and precision*

[![GitHub](https://img.shields.io/badge/GitHub-spyberpolymath-black?style=for-the-badge&logo=github)](https://github.com/spyberpolymath)
[![Kaggle](https://img.shields.io/badge/Kaggle-spyberpolymath-orange?style=for-the-badge&logo=kaggle)](https://kaggle.com/spyberpolymath)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-spyberpolymath-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/spyberpolymath)
[![Telegram](https://img.shields.io/badge/Telegram-spyberpolymath-blue?style=for-the-badge&logo=telegram)](https://t.me/spyberpolymath)

**📧 [aman@spyberpolymath.com](mailto:aman@spyberpolymath.com)** | **🌐 [spyberpolymath.com](https://spyberpolymath.com)**

---

*Made with ❤️ by Aman Anil aka (SpyberPolymath)* ✨

</div>