import psutil
import subprocess
import os
import json

# used to load in the config.json file to extract paths
with open("main/config.json", "r") as f:
    config = json.load(f)


def get_path(name):
    """Used to get the path from config.json"""
    name = name.lower()
    path = config[name+"_path"]
    return path


def is_app_running(app):
    """Check if the app is already running."""
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and app + ".exe" in proc.info['name']:
            return True
    return False


def launch_app(app):
    """Launch the app if not already running."""
    if is_app_running(app):
        print("✅ " + app + " is already running.")
        return

    path = get_path(app)

    if os.path.exists(path):
        subprocess.Popen([path])
        print("🚀 " + app + " launched successfully.")
    else:
        print("❌ " + app + " launcher not found.")


def close_app(app):
    """Close all running app processes."""
    closed = False
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and app in proc.info['name']:
            try:
                proc.terminate()
                closed = True
            except Exception as e:
                print("⚠️ Could not close " + app + f": {e}")
    if closed:
        print("🛑 " + app + " closed.")
    else:
        print("ℹ️  " + app + " was not running.")
