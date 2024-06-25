import requests
import subprocess
import os
import shutil
from dotenv import load_dotenv

load_dotenv()


username = username = os.getenv("GITHUB_USERNAME")
api_url = f"https://api.github.com/users/{username}/repos"

def clone_repo(repo_url, repo_name):
    subprocess.run(["git", "clone", repo_url], cwd="./repos")
    git_dir_path = os.path.join("./repos", repo_name, ".git")
    shutil.rmtree(git_dir_path)


def get_repos(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            repo_url = repo['clone_url']
            repo_name = repo['name']
            print(f"Cloning {repo_name}...")
            clone_repo(repo_url, repo_name)
    else:
        print("Failed to retrieve repositories")

if not os.path.exists("./repos"):
    os.makedirs("./repos")

get_repos(api_url)

print("\n\n     -----finished-----      \n\n")