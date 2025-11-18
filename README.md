🎬 Movie Remote (Control your laptop from your phone)

A simple Flask-based app that lets you control Netflix, YouTube, and any web player on your laptop using your phone.
Features include:

Play / Pause

Forward / Rewind

Volume Up / Down

Mute

Fullscreen

YouTube 10s Skip (using J / L keys)

🛠️ How it Works

Your laptop runs a small Flask server.
Your phone opens a webpage (on the same Wi-Fi).
The phone sends commands → laptop simulates key presses → controls the video.

🚀 How to Run (Development)

Install Python 3

Install dependencies:

pip install -r requirements.txt


Run the app:

python app.py


Open this on your phone (same Wi-Fi):

http://<your-laptop-ip>:5000

📦 Build EXE (Optional)

To generate a Windows executable:

pip install pyinstaller
pyinstaller --onefile app.py


The EXE will appear in dist/app.exe.

⚠️ Firewall Note

Windows will ask to allow the app through the firewall.
Choose Private networks → Allow Access.
