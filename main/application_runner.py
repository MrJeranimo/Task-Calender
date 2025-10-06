import psutil
import subprocess
import os
import json

# used to load in the config.json file to extract paths
with open("main/config.json", "r") as f:
    config = json.load(f)

# The path of discord
PATH = config["discord_path"]


def is_discord_running():
    """Check if Discord is already running."""
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and "Discord.exe" in proc.info['name']:
            return True
    return False


def launch_discord():
    """Launch Discord if not already running."""
    if is_discord_running():
        print("✅ Discord is already running.")
        return

    if os.path.exists(PATH):
        subprocess.Popen([PATH, "--processStart", "Discord.exe"])
        print("🚀 Discord launched successfully.")
    else:
        print("❌ Discord launcher not found. Check your installation path.")


def close_discord():
    """Close all running Discord processes."""
    closed = False
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and "Discord.exe" in proc.info['name']:
            try:
                proc.terminate()
                closed = True
            except Exception as e:
                print(f"⚠️ Could not close Discord: {e}")
    if closed:
        print("🛑 Discord closed.")
    else:
        print("ℹ️ Discord was not running.")
