#!/usr/bin/python3
import os
import subprocess
import time

def check_updates():
    # Hole den aktuellen Benutzernamen
    user = os.getenv("USER") or os.getenv("USERNAME") or ""
    
    if user.lower() in ["live", "linux"]:
        pass
    else:
        try:
            subprocess.run(["sudo", "apt", "update"], check=True)
            
            result = subprocess.run(["apt", "list", "--upgradable"], capture_output=True, text=True, check=True)
            
            upgradable_lines = result.stdout.strip().split("\n")
            if len(upgradable_lines) > 1:
                num_updates = len(upgradable_lines) - 1
                notify_message = f"{num_updates} Aktualisierungen verfügbar"
                
                # Sende Notification oben rechts mit Aktion
                result = subprocess.run([
                    "notify-send",
                    "GuideOS Updates",
                    notify_message,
                    "--icon=/usr/share/icons/hicolor/scalable/apps/guidos-updater.svg",
                    "--action=update=GuideOS-Updater öffnen",
                    "--wait",
                    "--urgency=critical",
                    "--expire-time=6000"
                ], capture_output=True, text=True)
                
                # Wenn auf "Updater öffnen" geklickt wurde, starte den Updater
                if result.stdout.strip() == "update":
                    subprocess.Popen(["python3", "/usr/lib/guideos-updater/main.py"])
            else:
                print("No updates available.")

        except subprocess.CalledProcessError as e:
            print(f"Error during update check: {e}")

if __name__ == "__main__":
    while True:
        check_updates()
        time.sleep(3 * 60 * 60)