#!/usr/bin/python3
import os
import subprocess
import time

def check_updates():
    try:
        # Aktualisiere den APT-Cache
        subprocess.run(["sudo", "apt", "update"], check=True)
        
        # Überprüfe verfügbare Updates
        result = subprocess.run(["apt", "list", "--upgradable"], capture_output=True, text=True, check=True)
        
        # Extrahiere die Liste der Updates
        upgradable_lines = result.stdout.strip().split("\n")
        if len(upgradable_lines) > 1:  # Die erste Zeile ist ein Header
            # Updates gefunden
            notify_message = f"{len(upgradable_lines) - 1} Aktualisierungen verfügbar."
            subprocess.run(["notify-send", "GuideOS Updates", notify_message])
        else:
            print("No updates available.")
            # Keine Updates verfügbar
            #subprocess.run(["notify-send", "APT Updates", "No updates available."])
    except subprocess.CalledProcessError as e:
        print(f"Error during update check: {e}")
        #subprocess.run(["notify-send", "APT Updates", "Error checking updates."])

if __name__ == "__main__":
    while True:
        check_updates()
        time.sleep(3 * 60 * 60)  # Warte 3 Stunden
