import subprocess
import shutil
import time
from pathlib import Path
from github import Github, Auth  # type: ignore

# =========================
# CONFIGURATION
# =========================

# GitHub Personal Access Token
GITHUB_TOKEN = "#"

# GitHub Organization Name
ORG_NAME = "lovosistechnology"

# Base Folder
BASE_PATH = Path.cwd() / ORG_NAME

# Maximum Retry Attempts
MAX_RETRIES = 3

# =========================
# GITHUB AUTH
# =========================

auth = Auth.Token(GITHUB_TOKEN)
g = Github(auth=auth)

try:
    org = g.get_organization(ORG_NAME)

except Exception as e:
    print(f"\n❌ Failed to access organization: {e}")
    exit()

# Create organization folder
BASE_PATH.mkdir(parents=True, exist_ok=True)

# =========================
# FUNCTIONS
# =========================

def clone_new_repos():

    print("\n🚀 Checking for new repositories...\n")

    repos = org.get_repos()

    for repo in repos:

        repo_path = BASE_PATH / repo.name
        git_folder = repo_path / ".git"

        # =========================
        # ALREADY CLONED
        # =========================

        if repo_path.exists() and git_folder.exists():

            print(f"⚡ Already Exists: {repo.name}")
            continue

        # =========================
        # BROKEN / PARTIAL CLONE
        # =========================

        if repo_path.exists() and not git_folder.exists():

            print(f"🗑️ Removing Broken Repo: {repo.name}")

            try:
                shutil.rmtree(repo_path, ignore_errors=True)

            except Exception as e:
                print(f"❌ Failed to remove broken repo: {repo.name}")
                print(e)
                continue

        clone_url = repo.clone_url

        # Add token for private repo access
        auth_clone_url = clone_url.replace(
            "https://",
            f"https://{GITHUB_TOKEN}@"
        )

        print(f"\n📥 Cloning: {repo.name}")

        # =========================
        # RETRY SYSTEM
        # =========================

        try_count = 0
        clone_success = False

        while try_count < MAX_RETRIES:

            try:

                result = subprocess.run(
                    [
                        "git",
                        "clone",
                        "--depth",
                        "1",
                        auth_clone_url,
                        str(repo_path)
                    ],
                    capture_output=True,
                    text=True
                )

                # =========================
                # SUCCESS
                # =========================

                if result.returncode == 0:

                    print(f"✅ Cloned Successfully: {repo.name}")

                    clone_success = True
                    break

                # =========================
                # FAILED
                # =========================

                else:

                    try_count += 1

                    print(
                        f"\n⚠️ Retry {try_count}/{MAX_RETRIES} "
                        f"for {repo.name}"
                    )

                    if result.stderr:

                        print("\n🔴 ERROR:")
                        print(result.stderr)

                    if result.stdout:

                        print("\n🟡 OUTPUT:")
                        print(result.stdout)

                    # Remove broken folder before retry
                    if repo_path.exists():

                        shutil.rmtree(repo_path, ignore_errors=True)

                    time.sleep(5)

            except KeyboardInterrupt:

                print("\n\n⛔ Process interrupted by user.")
                print(f"❌ Clone Terminated: {repo.name}")
                return

            except Exception as e:

                try_count += 1

                print(f"\n❌ Unexpected Error in {repo.name}")
                print(e)

                # Remove broken folder
                if repo_path.exists():

                    shutil.rmtree(repo_path, ignore_errors=True)

                time.sleep(5)

        # =========================
        # FINAL FAILURE
        # =========================

        if not clone_success:

            print(f"\n❌ Final Failed: {repo.name}")

    print("\n🎉 Clone operation completed.\n")


def update_all_repos():

    print("\n🔄 Updating all repositories...\n")

    if not BASE_PATH.exists():

        print("❌ Organization folder does not exist.")
        return

    for repo_folder in BASE_PATH.iterdir():

        if not repo_folder.is_dir():
            continue

        git_folder = repo_folder / ".git"

        # Skip invalid repos
        if not git_folder.exists():

            print(f"⚠️ Skipping Invalid Repo: {repo_folder.name}")
            continue

        print(f"\n⬇️ Updating: {repo_folder.name}")

        try:

            result = subprocess.run(
                [
                    "git",
                    "-C",
                    str(repo_folder),
                    "pull"
                ],
                capture_output=True,
                text=True
            )

            # =========================
            # SUCCESS
            # =========================

            if result.returncode == 0:

                print(f"✅ Updated: {repo_folder.name}")

                if result.stdout.strip():

                    print(result.stdout)

            # =========================
            # FAILED
            # =========================

            else:

                print(f"❌ Failed Update: {repo_folder.name}")

                if result.stderr:

                    print("\n🔴 ERROR:")
                    print(result.stderr)

                if result.stdout:

                    print("\n🟡 OUTPUT:")
                    print(result.stdout)

        except KeyboardInterrupt:

            print("\n\n⛔ Update process interrupted by user.")
            print(f"❌ Update Terminated: {repo_folder.name}")
            return

        except Exception as e:

            print(f"\n❌ Unexpected Error in {repo_folder.name}")
            print(e)

    print("\n🎉 Update operation completed.\n")


# =========================
# MENU
# =========================

while True:

    print("\n==============================")
    print(" GitHub Organization Manager ")
    print(f" Organization: {ORG_NAME}")
    print("==============================")
    print("1. Clone New Repositories")
    print("2. Update All Cloned Repositories")
    print("3. Exit")

    choice = input("\nEnter your choice: ").strip()

    # =========================
    # OPTION 1
    # =========================

    if choice == "1":

        clone_new_repos()

    # =========================
    # OPTION 2
    # =========================

    elif choice == "2":

        update_all_repos()

    # =========================
    # OPTION 3
    # =========================

    elif choice == "3":

        print("\n👋 Exiting...")
        break

    # =========================
    # INVALID OPTION
    # =========================

    else:

        print("\n❌ Invalid Option")