# 🔹 Challenge 10: Write a Python program that checks a GitHub repository for new commits and triggers a build job.

import requests
import time
import json

# GitHub repository details
GITHUB_REPO = "owner/repository"  # Replace with your GitHub repo (e.g., "torvalds/linux")
GITHUB_BRANCH = "main"
GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_REPO}/commits/{GITHUB_BRANCH}"
LAST_COMMIT_FILE = "last_commit.json"

# CI/CD build trigger URL (e.g., Jenkins webhook, GitHub Actions, or another service)
BUILD_TRIGGER_URL = "https://ci.example.com/build"

def get_latest_commit():
    """Fetches the latest commit SHA from GitHub API."""
    try:
        response = requests.get(GITHUB_API_URL)
        response.raise_for_status()
        commit_data = response.json()
        return commit_data["sha"]
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching latest commit: {e}")
        return None

def load_last_commit():
    """Loads the last stored commit SHA from a local file."""
    try:
        with open(LAST_COMMIT_FILE, "r") as file:
            return json.load(file).get("last_commit")
    except FileNotFoundError:
        return None

def save_last_commit(commit_sha):
    """Saves the latest commit SHA to a local file."""
    with open(LAST_COMMIT_FILE, "w") as file:
        json.dump({"last_commit": commit_sha}, file)

def trigger_build(commit_sha):
    """Triggers a CI/CD build job when a new commit is detected."""
    try:
        response = requests.post(BUILD_TRIGGER_URL, json={"commit": commit_sha})
        if response.status_code == 200:
            print(f"✅ Build triggered successfully for commit: {commit_sha}")
        else:
            print(f"⚠️ Failed to trigger build. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error triggering build: {e}")

def monitor_github():
    """Monitors the GitHub repository for new commits."""
    print(f"🔍 Monitoring GitHub repository: {GITHUB_REPO}")

    while True:
        latest_commit = get_latest_commit()
        if not latest_commit:
            time.sleep(60)
            continue

        last_commit = load_last_commit()

        if latest_commit != last_commit:
            print(f"🚀 New commit detected: {latest_commit}")
            trigger_build(latest_commit)
            save_last_commit(latest_commit)
        else:
            print("✅ No new commits detected.")

        time.sleep(60)  # Check every 60 seconds

# Start monitoring
monitor_github()