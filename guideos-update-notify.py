#!/usr/bin/python3
import os
import subprocess
import time

def check_updates():
    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        
        result = subprocess.run(["apt", "list", "--upgradable"], capture_output=True, text=True, check=True)
        
        upgradable_lines = result.stdout.strip().split("\n")
        if len(upgradable_lines) > 1:
            package_names = [line.split('/')[0] for line in upgradable_lines[1:]]
            notify_message = f"{len(package_names)} Aktualisierungen verfügbar:\n\n" + "\n".join(package_names)
            subprocess.run(["notify-send", "GuideOS Updates", notify_message])
        else:
            print("No updates available.")

    except subprocess.CalledProcessError as e:
        print(f"Error during update check: {e}")

if __name__ == "__main__":
    while True:
        check_updates()
        time.sleep(3 * 60 * 60)