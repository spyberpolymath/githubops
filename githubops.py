import os
import subprocess
from pathlib import Path
import requests
from dotenv import load_dotenv
import time
import random


# Cyberpunk Terminal UI Colors and Formatting
class CyberColors:
    # Neon Colors
    NEON_CYAN = '\033[96m'
    NEON_MAGENTA = '\033[95m'
    NEON_GREEN = '\033[92m'
    NEON_PINK = '\033[38;5;205m'
    NEON_YELLOW = '\033[93m'
    NEON_RED = '\033[91m'
    DARK_CYAN = '\033[38;5;23m'
    DARK_GRAY = '\033[38;5;240m'

    # Formatting
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'


def glitch_effect(text, color=CyberColors.NEON_CYAN, iterations=2):
    """Create a glitch effect with the text"""
    for _ in range(iterations):
        glitched = ''.join(random.choice(
            [c, '█', '▓']) if random.random() > 0.7 else c for c in text)
        print(f"\r{color}{glitched}{CyberColors.RESET}", end='', flush=True)
        time.sleep(0.05)
    print(f"\r{color}{text}{CyberColors.RESET}")


def animate_text(text, delay=0.02, color=None):
    """Animate text character by character"""
    if color is None:
        color = CyberColors.NEON_CYAN
    for char in text:
        print(f"{color}{char}{CyberColors.RESET}", end='', flush=True)
        time.sleep(delay)
    print()


def print_cyber_header(title):
    """Print a cyberpunk-style header with enhanced visuals"""
    width = 70
    print(f"\n{CyberColors.NEON_CYAN}{'▄' * width}{CyberColors.RESET}")
    print(f"{CyberColors.NEON_MAGENTA}▌ {CyberColors.NEON_CYAN}{title.center(width-4)}{CyberColors.NEON_MAGENTA} ▐{CyberColors.RESET}")
    print(f"{CyberColors.NEON_CYAN}{'▀' * width}{CyberColors.RESET}")
    print(
        f"{CyberColors.DARK_GRAY}[SYS_BOOT] {CyberColors.NEON_MAGENTA}>> {CyberColors.RESET}Protocol initialized{CyberColors.RESET}\n")


def print_loading(text, duration=1.5):
    """Print loading animation with progress bar"""
    frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    start = time.time()
    idx = 0
    while time.time() - start < duration:
        progress = int((time.time() - start) / duration * 20)
        bar = '█' * progress + '░' * (20 - progress)
        print(
            f"\r{CyberColors.NEON_GREEN}{frames[idx % len(frames)]} {text} [{bar}]{CyberColors.RESET}", end='', flush=True)
        idx += 1
        time.sleep(0.1)
    print(
        f"\r{CyberColors.NEON_GREEN}✓ {text} [{'█' * 20}]{CyberColors.RESET}")


def print_success(text):
    """Print success message with cyberpunk style"""
    print(f"{CyberColors.NEON_GREEN}◆ ✓ {text}{CyberColors.RESET}")


def print_error(text):
    """Print error message with cyberpunk style"""
    print(f"{CyberColors.NEON_RED}◆ ✗ {text}{CyberColors.RESET}")


def print_warning(text):
    """Print warning message with cyberpunk style"""
    print(f"{CyberColors.NEON_YELLOW}◆ ⚠ {text}{CyberColors.RESET}")


def print_info(text):
    """Print info message with cyberpunk style"""
    print(f"{CyberColors.NEON_CYAN}◆ ℹ {text}{CyberColors.RESET}")


def print_separator():
    """Print a separator line with tech effect"""
    print(f"{CyberColors.DARK_GRAY}{'─' * 70}{CyberColors.RESET}")


def print_status_bar(current, total, label="PROGRESS"):
    """Print a status bar with progress percentage"""
    progress = int((current / total) * 30) if total > 0 else 0
    percentage = int((current / total) * 100) if total > 0 else 0
    bar = '█' * progress + '░' * (30 - progress)
    print(
        f"{CyberColors.NEON_MAGENTA}[{label}] {bar} {percentage}%{CyberColors.RESET}")


def print_footer(brand_name="SpyberPolymath", website="spyberpolymath.com"):
    """Print developer credits and footer"""
    print_separator()
    print(f"{CyberColors.DARK_GRAY}[SYSTEM] {'─' * 50}{CyberColors.RESET}")
    print(f"{CyberColors.NEON_CYAN}▌ GITHUB OPS PROTOCOL{CyberColors.RESET}")
    print(f"{CyberColors.DARK_GRAY}  Designed & Maintained by:{CyberColors.RESET} {CyberColors.NEON_MAGENTA}Aman Anil{CyberColors.RESET} {CyberColors.NEON_GREEN}aka{CyberColors.RESET} {CyberColors.NEON_CYAN}{brand_name}{CyberColors.RESET}")
    print(f"{CyberColors.DARK_GRAY}  Website:{CyberColors.RESET} {CyberColors.NEON_GREEN}{website}{CyberColors.RESET}")
    print(f"{CyberColors.DARK_GRAY}[SYSTEM] {'─' * 50}{CyberColors.RESET}\n")


def run_command(command, cwd=None):
    """Run a shell command and return the output"""
    try:
        result = subprocess.run(command, shell=True, cwd=cwd,
                                check=True, capture_output=True, text=True)
        return result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        print_error(f"Command failed: {e}")
        print_error(f"Error output: {e.stderr}")
        return None, e.stderr


def get_local_repositories(base_path="."):
    """Scan current directory for git repositories"""
    repos = []
    base_path = Path(base_path)

    try:
        for item in base_path.rglob(".git"):
            repo_path = item.parent
            if repo_path.is_dir():
                repos.append({
                    'path': str(repo_path),
                    'name': repo_path.name,
                    'has_changes': check_git_changes(repo_path)
                })
    except (OSError, FileNotFoundError) as e:
        print_error(f"Error scanning repositories: {e}")
        return []

    return repos


def check_git_changes(repo_path):
    """Check if a repository has uncommitted changes"""
    try:
        stdout, _ = run_command("git status --porcelain", cwd=str(repo_path))
        if stdout is not None:
            return bool(stdout.strip())
        return False
    except (OSError, ValueError):
        return False


def display_folder_structure(repositories, username):
    """Display the folder structure of repositories in username/{private or public}/repo format"""
    print_separator()
    print(
        f"\n{CyberColors.BOLD}{CyberColors.NEON_CYAN}Folder Structure:{CyberColors.RESET}\n")

    structure = {}

    for idx, repo in enumerate(repositories, 1):
        repo_path = Path(repo['path'])
        repo_name = repo['name']

        # Determine if private or public by checking git config
        remote_url, _ = run_command(
            "git config --get remote.origin.url", cwd=str(repo_path))
        is_private = "private" in str(
            repo_path).lower() or ".git" in remote_url
        visibility = 'private' if is_private else 'public'

        display_path = f"{username}/{visibility}/{repo_name}"

        if visibility not in structure:
            structure[visibility] = []
        structure[visibility].append(display_path)

        has_changes = " " + CyberColors.NEON_YELLOW + \
            "[CHANGES]" + CyberColors.RESET if repo['has_changes'] else ""
        print(
            f"  {CyberColors.NEON_GREEN}[{idx}]{CyberColors.RESET} {display_path}{has_changes}")

    print()
    return structure


def select_repositories_to_push(repositories):
    """Allow user to select repositories to push"""
    if not repositories:
        return []

    print_separator()
    print()
    print(f"{CyberColors.BOLD}Selection options:{CyberColors.RESET}")
    print(f"  {CyberColors.NEON_GREEN}•{CyberColors.RESET} Single repo:  {CyberColors.NEON_CYAN}1{CyberColors.RESET}")
    print(f"  {CyberColors.NEON_MAGENTA}•{CyberColors.RESET} Multiple:     {CyberColors.NEON_CYAN}1,3,5{CyberColors.RESET}  or  {CyberColors.NEON_CYAN}1 3 5{CyberColors.RESET}")
    print(f"  {CyberColors.NEON_YELLOW}•{CyberColors.RESET} All repos:    {CyberColors.NEON_GREEN}all{CyberColors.RESET}")
    print(f"  {CyberColors.NEON_YELLOW}•{CyberColors.RESET} Only changed: {CyberColors.NEON_MAGENTA}changed{CyberColors.RESET}")
    print(f"  {CyberColors.NEON_RED}•{CyberColors.RESET} Exit:         {CyberColors.NEON_RED}Ctrl+C{CyberColors.RESET}\n")

    while True:
        try:
            selection = input(
                f"{CyberColors.BOLD}{CyberColors.NEON_CYAN}>>> {CyberColors.RESET}").strip().lower()

            if not selection:
                print_warning("Please enter a valid selection")
                continue

            selected_indices = []

            if selection == 'all':
                selected_indices = list(range(len(repositories)))
            elif selection == 'changed':
                selected_indices = [i for i, repo in enumerate(
                    repositories) if repo.get('has_changes', False)]
                if not selected_indices:
                    print_warning("No repositories with changes found")
                    continue
            else:
                # Handle both comma and space separated input
                selection = selection.replace(',', ' ')
                try:
                    indices = [int(x.strip())
                               for x in selection.split() if x.strip()]
                    selected_indices = [
                        i - 1 for i in indices if 1 <= i <= len(repositories)]

                    if not selected_indices:
                        print_warning(
                            f"Please enter numbers between 1 and {len(repositories)}")
                        continue

                    if len(indices) != len(selected_indices):
                        print_warning(
                            f"Some numbers were out of range (valid: 1-{len(repositories)})")

                except ValueError:
                    print_warning(
                        "Please enter valid numbers separated by spaces or commas")
                    continue

            selected_repos = [repositories[i] for i in selected_indices]

            # Show confirmation
            print(
                f"\n{CyberColors.NEON_GREEN}Selected {len(selected_repos)} repository(ies) for push:{CyberColors.RESET}")
            for repo in selected_repos:
                print(
                    f"  {CyberColors.NEON_GREEN}✓{CyberColors.RESET} {repo['name']}")

            print_separator()
            confirm = input(
                f"{CyberColors.BOLD}{CyberColors.NEON_MAGENTA}[?] Proceed with push? (y/n): {CyberColors.RESET}").strip().lower()
            if confirm == 'y':
                return selected_repos
            else:
                print_info("Selection cancelled. Please select again.\n")

        except KeyboardInterrupt:
            print(
                f"\n\n{CyberColors.NEON_RED}[!] Operation cancelled by user{CyberColors.RESET}")
            return []


def get_commit_message(is_bulk=False):
    """Get commit message from user"""
    print_separator()

    if is_bulk:
        print(
            f"\n{CyberColors.BOLD}Enter commit message for bulk push:{CyberColors.RESET}")
        print(f"{CyberColors.DARK_GRAY}This message will be used for all selected repositories{CyberColors.RESET}\n")
    else:
        print(f"\n{CyberColors.BOLD}Enter commit message:{CyberColors.RESET}\n")

    message = input(
        f"{CyberColors.NEON_MAGENTA}[+] Message: {CyberColors.RESET}").strip()

    if not message:
        message = "Update: Bulk push commit"
        print_warning(f"Using default message: {message}")

    return message


def push_repositories(repositories, commit_message, bulk_push=True):
    """Push repositories to GitHub"""
    print_cyber_header("Initiating Push Protocol")

    pushed_repos = []
    failed_repos = []
    total = len(repositories)
    start_time = time.time()

    print_separator()
    print(
        f"{CyberColors.NEON_GREEN}[EXECUTING] Pushing {total} repository(ies)...{CyberColors.RESET}\n")

    try:
        for idx, repo in enumerate(repositories, 1):
            repo_path = repo['path']
            repo_name = repo['name']

            print(
                f"\n{CyberColors.BOLD}{CyberColors.NEON_MAGENTA}[{idx}/{total}]{CyberColors.RESET} {CyberColors.NEON_CYAN}Processing {repo_name}...{CyberColors.RESET}")
            print(
                f"    {CyberColors.DARK_GRAY}→ {repo_path}{CyberColors.RESET}")

            try:
                # Check for changes
                status_stdout, _ = run_command(
                    "git status --porcelain", cwd=repo_path)
                if status_stdout and not status_stdout.strip():
                    print_warning(f"No changes to commit in {repo_name}")
                    pushed_repos.append(repo_path)
                    print_status_bar(idx, total, "PUSH_PROGRESS")
                    continue

                # Stage all changes
                run_command("git add -A", cwd=repo_path)
                print_info("Staged all changes")
                # Create commit
                commit_msg = commit_message if bulk_push else get_commit_message(
                    is_bulk=False)
                stdout, stderr = run_command(
                    f'git commit -m "{commit_msg}"', cwd=repo_path)

                if stdout is not None or "nothing to commit" in str(stderr):
                    print_success(f"Committed: {commit_msg}")

                    # Push to remote
                    push_stdout, push_stderr = run_command(
                        "git push", cwd=repo_path)
                    if push_stdout is not None or "Everything up-to-date" in str(push_stderr):
                        print_success("Pushed successfully")
                        pushed_repos.append(repo_path)
                    else:
                        print_error(f"Failed to push: {push_stderr}")
                        failed_repos.append(
                            {'name': repo_name, 'error': push_stderr})
                else:
                    print_error(f"Failed to commit: {stderr}")
                    failed_repos.append({'name': repo_name, 'error': stderr})

            except (subprocess.CalledProcessError, OSError, ValueError) as e:
                print_error(f"Error processing {repo_name}: {e}")
                failed_repos.append({'name': repo_name, 'error': str(e)})

            print_status_bar(idx, total, "PUSH_PROGRESS")

    except KeyboardInterrupt:
        print(
            f"\n\n{CyberColors.NEON_RED}[!] Push interrupted by user{CyberColors.RESET}")
        print_warning(
            f"Pushed {len(pushed_repos)} out of {total} repositories before interruption")

    elapsed = time.time() - start_time
    print(
        f"\n{CyberColors.DARK_GRAY}[TIMING] Operation completed in {elapsed:.2f}s{CyberColors.RESET}")

    return pushed_repos, failed_repos


def list_local_repositories(base_path="."):
    """List available local repositories"""
    repositories = get_local_repositories(base_path)

    if not repositories:
        print_warning("No git repositories found in current directory")
        return []

    print_cyber_header("Found Local Repositories")
    print(f"{CyberColors.BOLD}Total repositories found: {len(repositories)}{CyberColors.RESET}\n")

    for idx, repo in enumerate(repositories, 1):
        status = f"{CyberColors.NEON_YELLOW}[HAS CHANGES]{CyberColors.RESET}" if repo[
            'has_changes'] else f"{CyberColors.NEON_GREEN}[CLEAN]{CyberColors.RESET}"
        print(
            f"  {CyberColors.NEON_GREEN}[{idx}]{CyberColors.RESET} {repo['name']:30} {status}  {CyberColors.DARK_GRAY}({repo['path']}){CyberColors.RESET}")

    print()
    return repositories


def get_repos_from_github(username, token):
    """Fetch all repositories for the authenticated user from GitHub API"""
    url = "https://api.github.com/user/repos"
    headers = {'Authorization': f'token {token}'}
    params = {'per_page': 100, 'sort': 'updated',
              'direction': 'desc', 'type': 'all'}

    try:
        response = requests.get(url, headers=headers,
                                params=params, timeout=10)
        response.raise_for_status()
        repos = response.json()

        print(
            f"\n{CyberColors.NEON_GREEN}[DEBUG]{CyberColors.RESET} {CyberColors.DARK_GRAY}Total repos from API: {CyberColors.NEON_CYAN}{len(repos)}{CyberColors.RESET}")
        print(
            f"{CyberColors.NEON_GREEN}[DEBUG]{CyberColors.RESET} {CyberColors.DARK_GRAY}Token scope check - API returned repos successfully{CyberColors.RESET}")

        filtered_repos = [
            repo for repo in repos if repo['owner']['login'] == username]
        print(
            f"{CyberColors.NEON_GREEN}[DEBUG]{CyberColors.RESET} {CyberColors.DARK_GRAY}Repos owned by {CyberColors.NEON_MAGENTA}{username}{CyberColors.DARK_GRAY}: {CyberColors.NEON_CYAN}{len(filtered_repos)}{CyberColors.RESET}")

        public_count = sum(1 for repo in filtered_repos if not repo['private'])
        private_count = sum(1 for repo in filtered_repos if repo['private'])
        print(
            f"{CyberColors.NEON_GREEN}[DEBUG]{CyberColors.RESET} {CyberColors.DARK_GRAY}Public: {CyberColors.NEON_GREEN}{public_count}{CyberColors.DARK_GRAY}, Private: {CyberColors.NEON_MAGENTA}{private_count}{CyberColors.RESET}")

        for repo in filtered_repos:
            visibility = f'{CyberColors.NEON_MAGENTA}PRIVATE{CyberColors.RESET}' if repo[
                'private'] else f'{CyberColors.NEON_GREEN}public{CyberColors.RESET}'
            print(
                f"{CyberColors.NEON_GREEN}[DEBUG]{CyberColors.RESET} {CyberColors.DARK_GRAY}  - {CyberColors.NEON_CYAN}{repo['name']}{CyberColors.DARK_GRAY} ({visibility}{CyberColors.DARK_GRAY}){CyberColors.RESET}")

        result = [{'name': repo['name'], 'private': repo['private']}
                  for repo in filtered_repos]
        print()
        return result
    except requests.RequestException as e:
        print_error(f"Failed to fetch repositories: {e}")
        print_info(
            "Make sure your token has 'repo' scope to access private repositories.")
        print_info("Generate a new token at: https://github.com/settings/tokens")
        return None


def select_repositories(repositories):
    """Allow user to select repositories by number or multiple numbers"""
    if not repositories:
        return []

    print_separator()

    print()
    print(f"{CyberColors.BOLD}Selection options:{CyberColors.RESET}")
    print(f"  {CyberColors.NEON_GREEN}•{CyberColors.RESET} Single repo:  {CyberColors.NEON_CYAN}1{CyberColors.RESET}")
    print(f"  {CyberColors.NEON_MAGENTA}•{CyberColors.RESET} Multiple:     {CyberColors.NEON_CYAN}1,3,5{CyberColors.RESET}  or  {CyberColors.NEON_CYAN}1 3 5{CyberColors.RESET}")
    print(f"  {CyberColors.NEON_YELLOW}•{CyberColors.RESET} All repos:    {CyberColors.NEON_GREEN}all{CyberColors.RESET}")
    print(f"  {CyberColors.NEON_YELLOW}•{CyberColors.RESET} Private only: {CyberColors.NEON_MAGENTA}private{CyberColors.RESET}")
    print(f"  {CyberColors.NEON_GREEN}•{CyberColors.RESET} Public only:  {CyberColors.NEON_GREEN}public{CyberColors.RESET}")
    print(f"  {CyberColors.NEON_RED}•{CyberColors.RESET} Exit:         {CyberColors.NEON_RED}Ctrl+C{CyberColors.RESET}\n")

    while True:
        try:
            selection = input(
                f"{CyberColors.BOLD}{CyberColors.NEON_CYAN}>>> {CyberColors.RESET}").strip().lower()

            if not selection:
                print_warning("Please enter a valid selection")
                continue

            selected_indices = []

            if selection == 'all':
                selected_indices = list(range(len(repositories)))
            elif selection == 'private':
                selected_indices = [i for i, repo in enumerate(
                    repositories) if repo.get('private', False)]
            elif selection == 'public':
                selected_indices = [i for i, repo in enumerate(
                    repositories) if not repo.get('private', False)]
            else:
                # Handle both comma and space separated input
                selection = selection.replace(',', ' ')
                try:
                    indices = [int(x.strip())
                               for x in selection.split() if x.strip()]
                    selected_indices = [
                        i - 1 for i in indices if 1 <= i <= len(repositories)]

                    if not selected_indices:
                        print_warning(
                            f"Please enter numbers between 1 and {len(repositories)}")
                        continue

                    if len(indices) != len(selected_indices):
                        print_warning(
                            f"Some numbers were out of range (valid: 1-{len(repositories)})")

                except ValueError:
                    print_warning(
                        "Please enter valid numbers separated by spaces or commas")
                    continue

            selected_repos = [repositories[i] for i in selected_indices]

            # Show confirmation
            print(
                f"\n{CyberColors.NEON_GREEN}Selected {len(selected_repos)} repository(ies):{CyberColors.RESET}")
            for repo in selected_repos:
                print(
                    f"  {CyberColors.NEON_GREEN}✓{CyberColors.RESET} {repo['name']}")

            print_separator()
            confirm = input(
                f"{CyberColors.BOLD}{CyberColors.NEON_MAGENTA}[?] Proceed with cloning? (y/n): {CyberColors.RESET}").strip().lower()
            if confirm == 'y':
                return selected_repos
            else:
                print_info("Selection cancelled. Please select again.\n")

        except KeyboardInterrupt:
            print(
                f"\n\n{CyberColors.NEON_RED}[!] Operation cancelled by user{CyberColors.RESET}")
            return []


def list_repositories(gh_username):
    """List repositories manually by asking the user"""
    print_cyber_header("Manual Repository Selection")
    print(f"{CyberColors.BOLD}User: {CyberColors.NEON_CYAN}{gh_username}{CyberColors.RESET}\n")
    print(f"{CyberColors.BOLD}How would you like to list repositories?{CyberColors.RESET}\n")
    print("  1. Enter repository names manually")
    print("  2. Enter repository URLs manually")
    print("  3. Use current directory repositories")
    print()

    try:
        choice = input(
            f"{CyberColors.BOLD}{CyberColors.NEON_CYAN}>>> {CyberColors.RESET}").strip()

        repositories = []

        if choice == "1":
            print(
                f"\n{CyberColors.BOLD}Enter repository names (type 'done' when finished){CyberColors.RESET}\n")
            while True:
                repo_name = input(
                    f"{CyberColors.NEON_MAGENTA}[+] Repo name: {CyberColors.RESET}").strip()
                if repo_name.lower() == 'done':
                    break
                if repo_name:
                    repositories.append({'name': repo_name, 'private': False})
                    print_success(f"Added: {repo_name}")

        elif choice == "2":
            print(
                f"\n{CyberColors.BOLD}Enter repository URLs (type 'done' when finished){CyberColors.RESET}\n")
            while True:
                repo_url = input(
                    f"{CyberColors.NEON_MAGENTA}[+] Repo URL: {CyberColors.RESET}").strip()
                if repo_url.lower() == 'done':
                    break
                if repo_url:
                    repositories.append(repo_url)
                    print_success(f"Added: {repo_url}")

        elif choice == "3":
            current_dir = Path.cwd()
            for item in current_dir.iterdir():
                if item.is_dir() and (item / ".git").exists():
                    repositories.append(
                        {'name': str(item.name), 'private': False})
            print_success(f"Found {len(repositories)} local repositories")

        return repositories

    except KeyboardInterrupt:
        print(
            f"\n\n{CyberColors.NEON_RED}[!] Operation cancelled by user{CyberColors.RESET}")
        return []


def clone_repositories(repositories, username):
    """Clone repositories into organized folder structure"""
    print_cyber_header("Initiating Clone Protocol")

    cloned_repos = []
    total = len(repositories)
    start_time = time.time()

    print_separator()
    print(
        f"{CyberColors.NEON_GREEN}[EXECUTING] Cloning {total} repository(ies)...{CyberColors.RESET}\n")

    try:
        for idx, repo in enumerate(repositories, 1):
            if isinstance(repo, dict):
                repo_name = repo['name']
                is_private = repo.get('private', False)
            else:
                repo_name = repo
                is_private = False

            visibility = 'private' if is_private else 'public'
            clone_path = f"{username}/{visibility}/{repo_name}"

            print(
                f"\n{CyberColors.BOLD}{CyberColors.NEON_MAGENTA}[{idx}/{total}]{CyberColors.RESET} {CyberColors.NEON_CYAN}Cloning {repo_name}...{CyberColors.RESET}")

            if isinstance(repo, str) and (repo.startswith("http") or repo.startswith("git@")):
                clone_url = repo
            else:
                clone_url = f"https://github.com/{username}/{repo_name}.git"

            if os.path.exists(clone_path):
                print_warning(f"Already exists: {clone_path}")
                cloned_repos.append(clone_path)
                print_status_bar(1, 1, "CLONE_PROGRESS")
                continue

            os.makedirs(os.path.dirname(clone_path), exist_ok=True)

            print(
                f"    {CyberColors.DARK_GRAY}→ {clone_path}{CyberColors.RESET}")

            stdout, stderr = run_command(f"git clone {clone_url} {clone_path}")
            if stdout is not None:
                print_success(f"Cloned to: {clone_path}")
                cloned_repos.append(clone_path)
                print_status_bar(1, 1, "CLONE_PROGRESS")
            else:
                print_error(f"Failed to clone {repo_name}")
                if stderr:
                    print(
                        f"  {CyberColors.NEON_RED}{stderr.strip()}{CyberColors.RESET}")
                print(
                    f"{CyberColors.NEON_YELLOW}⚠ Skipping to next repository...{CyberColors.RESET}")
                continue

    except KeyboardInterrupt:
        print(
            f"\n\n{CyberColors.NEON_RED}[!] Cloning interrupted by user{CyberColors.RESET}")
        print_warning(
            f"Cloned {len(cloned_repos)} out of {total} repositories before interruption")

    elapsed = time.time() - start_time
    print(
        f"\n{CyberColors.DARK_GRAY}[TIMING] Operation completed in {elapsed:.2f}s{CyberColors.RESET}")
    return cloned_repos


def main():
    try:
        load_dotenv()
        start_time = time.time()

        glitch_effect("GITHUB OPS PROTOCOL v2.0", CyberColors.NEON_CYAN)
        print_cyber_header("GITHUB OPS PROTOCOL v2.0")
        print_footer()
        print(
            f"{CyberColors.DARK_GRAY}[SYSTEM] Initializing hacker interface...{CyberColors.RESET}\n")
        time.sleep(0.5)

        print(f"{CyberColors.BOLD}Select operation:{CyberColors.RESET}")
        print("  1. Clone repositories")
        print("  2. Push repositories")
        print()

        operation = input(
            f"{CyberColors.BOLD}{CyberColors.NEON_CYAN}>>> {CyberColors.RESET}").strip()

        if operation == "1":
            # Clone logic
            username = os.getenv('GITHUB_USERNAME')
            if not username:
                print(
                    f"{CyberColors.NEON_MAGENTA}[?]{CyberColors.RESET} Enter your GitHub username: ", end='')
                username = input(f"{CyberColors.NEON_CYAN}").strip()
                print(CyberColors.RESET, end='')
                if not username:
                    print_error("Username is required. Exiting.")
                    return

            print_success(f"Username authenticated: {username}")
            print_separator()

            token = os.getenv('GITHUB_TOKEN')
            if not token:
                print(
                    f"{CyberColors.NEON_MAGENTA}[?]{CyberColors.RESET} Enter your GitHub personal access token: ", end='')
                token = input(f"{CyberColors.NEON_CYAN}").strip()
                print(CyberColors.RESET, end='')

            repositories = []

            if token:
                print_loading("Fetching repositories from GitHub", duration=2)
                repos = get_repos_from_github(username, token)
                if repos:
                    print_success(f"Fetched {len(repos)} repositories")

                    selected = select_repositories(repos)
                    if selected:
                        repositories = selected
                    else:
                        print_warning("No repositories selected")
                        return
                else:
                    print_warning(
                        "Failed to fetch repositories. Proceeding to manual selection.")

            if not repositories:
                repositories = list_repositories(username)

            if not repositories:
                print_error("No repositories selected. Exiting...")
                return

            cloned_repos = clone_repositories(repositories, username)

            if not cloned_repos:
                print_error("No repositories were cloned. Exiting...")
                return

            print_separator()
            print_cyber_header("Operation Completed Successfully")
            total_time = time.time() - start_time
            print_success(f"Total repositories cloned: {len(cloned_repos)}")
            print(
                f"{CyberColors.DARK_GRAY}[TIMING] Total execution time: {total_time:.2f}s{CyberColors.RESET}")
            print(f"\n{CyberColors.BOLD}Cloned locations:{CyberColors.RESET}")
            for idx, repo in enumerate(cloned_repos, 1):
                print(
                    f"  {CyberColors.NEON_GREEN}[{idx:2d}]✓{CyberColors.RESET} {repo}")
            print(
                f"\n{CyberColors.DARK_GRAY}[SYSTEM] All operations completed successfully{CyberColors.RESET}\n")

        elif operation == "2":
            # Push logic
            username = os.getenv('GITHUB_USERNAME')
            if not username:
                print_error("GITHUB_USERNAME not found in .env file. Exiting.")
                return
            project_folder = f'./{username}'

            print_success(f"Username authenticated: {username}")
            print_separator()

            # Get base path for scanning repositories
            print(
                f"\n{CyberColors.BOLD}User: {CyberColors.NEON_CYAN}{username}{CyberColors.RESET}")
            print(f"\n{CyberColors.BOLD}Select scan location:{CyberColors.RESET}")
            print("  1. Current directory (.)")
            print(f"  2. {username} folder ({project_folder})")
            print("  3. Custom path")

            scan_choice = input(
                f"{CyberColors.NEON_MAGENTA}[?] Choice (1-3): {CyberColors.RESET}").strip()

            if scan_choice == "2":
                base_path = project_folder
            elif scan_choice == "3":
                base_path = input(
                    f"{CyberColors.NEON_MAGENTA}[?] Enter path: {CyberColors.RESET}").strip()
            else:
                base_path = "."

            print_loading("Scanning for repositories", duration=2)
            repositories = list_local_repositories(base_path)

            if not repositories:
                print_error("No repositories found. Exiting...")
                return

            # Display folder structure
            display_folder_structure(repositories, username)

            # Ask for bulk push mode
            print(f"\n{CyberColors.BOLD}Push mode:{CyberColors.RESET}")
            print("  1. Bulk push (same commit message for all)")
            print("  2. Individual push (custom message per repo)")

            push_mode = input(
                f"{CyberColors.NEON_MAGENTA}[?] Choice (1-2): {CyberColors.RESET}").strip()
            bulk_push = push_mode != "2"

            # Select repositories
            selected_repos = select_repositories_to_push(repositories)

            if not selected_repos:
                print_error("No repositories selected. Exiting...")
                return

            # Get commit message if bulk push
            commit_message = ""
            if bulk_push:
                commit_message = get_commit_message(is_bulk=True)

            # Push repositories
            pushed_repos, failed_repos = push_repositories(
                selected_repos, commit_message, bulk_push)

            # Summary
            print_separator()
            print_cyber_header("Operation Summary")

            print_success(
                f"Successfully pushed: {len(pushed_repos)} repository(ies)")
            if failed_repos:
                print_error(f"Failed: {len(failed_repos)} repository(ies)")
                print(
                    f"\n{CyberColors.BOLD}Failed repositories:{CyberColors.RESET}")
                for repo in failed_repos:
                    print(
                        f"  {CyberColors.NEON_RED}✗{CyberColors.RESET} {repo['name']}")
                    if repo['error']:
                        print(
                            f"    {CyberColors.DARK_GRAY}Error: {repo['error'].strip()[:60]}...{CyberColors.RESET}")

            print(f"\n{CyberColors.BOLD}Pushed repositories:{CyberColors.RESET}")
            for idx, repo in enumerate(pushed_repos, 1):
                print(
                    f"  {CyberColors.NEON_GREEN}[{idx}]✓{CyberColors.RESET} {Path(repo).name}")

            total_time = time.time() - start_time
            print(
                f"\n{CyberColors.DARK_GRAY}[TIMING] Total execution time: {total_time:.2f}s{CyberColors.RESET}")
            print(
                f"{CyberColors.DARK_GRAY}[SYSTEM] Push protocol completed{CyberColors.RESET}\n")

        else:
            print_error("Invalid operation selected. Exiting.")

    except KeyboardInterrupt:
        print(
            f"\n\n{CyberColors.NEON_RED}[!] Program terminated by user{CyberColors.RESET}")
        print(
            f"{CyberColors.DARK_GRAY}[SYSTEM] Shutting down...{CyberColors.RESET}\n")
        return
    except (requests.RequestException, subprocess.CalledProcessError, OSError, EOFError, ValueError) as e:
        print_error(f"Unexpected error: {e}")
        print(
            f"{CyberColors.DARK_GRAY}[DEBUG] {type(e).__name__}{CyberColors.RESET}")
        return


if __name__ == "__main__":
    main()
