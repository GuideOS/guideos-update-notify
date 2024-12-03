#!/bin/bash

# Sicherstellen, dass die Verzeichnisse existieren
mkdir -p debian/guideos-update-notify/etc/xdg/autostart


# Erstellen der Autostart .desktop-Datei
cat > debian/guideos-update-notify/etc/xdg/autostart/guideos-update-notify.desktop <<EOL
#!/usr/bin/env xdg-open
[Desktop Entry]
Type=Application
Exec=python3 /usr/lib/guideos-update-notify/guideos-update-notify.py
X-GNOME-Autostart-enabled=true
NoDisplay=false
Hidden=false
Name[de_DE]=guideos-update-notify.desktop
Comment[de_DE]=Keine Beschreibung
X-GNOME-Autostart-Delay=0
EOL

