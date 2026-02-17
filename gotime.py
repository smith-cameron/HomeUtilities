import subprocess
import webbrowser
from pathlib import Path
# import os
import time

webbrowser.open("https://mail.google.com/mail/u/1/?ogbl#inbox", new=1)
webbrowser.open("https://github.com/smith-cameron", new=2)
webbrowser.open("http://localhost:5173/", new=3)
webbrowser.open("https://react-bootstrap.netlify.app/docs/components/modal/", new=4)
time.sleep(0.5)

OBSIDIAN_SHORTCUT = Path.home() / "Desktop" / "Obsidian.lnk"
CHATGPT_SHORTCUT = Path.home() / "Desktop" / "ChatGPT.lnk"
MYSQL_WORKBENCH_SHORTCUT = Path.home() / "Desktop" / "MySQL Workbench 8.0 CE.lnk"
if OBSIDIAN_SHORTCUT.exists():
    subprocess.Popen(['cmd', '/c', 'start', '', str(OBSIDIAN_SHORTCUT)])
time.sleep(0.5)

if CHATGPT_SHORTCUT.exists():
    subprocess.Popen(['cmd', '/c', 'start', '', str(CHATGPT_SHORTCUT)])
time.sleep(0.5)

if MYSQL_WORKBENCH_SHORTCUT.exists():
    subprocess.Popen(['cmd', '/c', 'start', '', str(MYSQL_WORKBENCH_SHORTCUT)])
time.sleep(0.5)

subprocess.Popen([
    r"C:\Users\Reverend Ruckus\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    r"C:\Users\Reverend Ruckus\PostCatering.code-workspace"
])
