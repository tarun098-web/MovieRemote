from flask import Flask, request, render_template_string
import keyboard  # to simulate key presses

app = Flask(__name__)

# --- HTML for the remote page ---
REMOTE_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Movie Remote</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 20px;
        }
        h1 {
            margin-bottom: 10px;
        }
        h2 {
            margin-top: 25px;
            margin-bottom: 10px;
            font-size: 20px;
        }
        .btn {
            display: inline-block;
            padding: 18px 20px;
            margin: 8px;
            font-size: 18px;
            border-radius: 12px;
            border: none;
            cursor: pointer;
            min-width: 120px;
        }
        .row {
            margin-bottom: 8px;
        }
        .section {
            margin-bottom: 20px;
            border-top: 1px solid #ddd;
            padding-top: 10px;
        }
    </style>
</head>
<body>
    <h1>Movie Remote</h1>

    <div class="section">
        <h2>Common Controls</h2>
        <div class="row">
            <button class="btn" onclick="sendCommand('rewind_arrow')">⏪ Back (←)</button>
            <button class="btn" onclick="sendCommand('play_pause')">⏯ Play / Pause</button>
            <button class="btn" onclick="sendCommand('forward_arrow')">⏩ Forward (→)</button>
        </div>
        <div class="row">
            <button class="btn" onclick="sendCommand('vol_down')">🔉 Vol -</button>
            <button class="btn" onclick="sendCommand('mute')">🔇 Mute</button>
            <button class="btn" onclick="sendCommand('vol_up')">🔊 Vol +</button>
        </div>
        <div class="row">
            <button class="btn" onclick="sendCommand('fullscreen')">🖵 Fullscreen</button>
        </div>
    </div>

    <div class="section">
        <h2>YouTube Skip (10s)</h2>
        <div class="row">
            <button class="btn" onclick="sendCommand('yt_back_10')">⏪ -10s (J)</button>
            <button class="btn" onclick="sendCommand('yt_forward_10')">⏩ +10s (L)</button>
        </div>
    </div>

    <script>
        function sendCommand(cmd) {
            fetch('/command', {
                method: 'POST',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                body: 'cmd=' + encodeURIComponent(cmd)
            }).catch(err => console.error(err));
        }
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(REMOTE_HTML)

@app.route("/command", methods=["POST"])
def command():
    cmd = request.form.get("cmd")

    # --- Common controls (Netflix + YT where possible) ---
    if cmd == "play_pause":
        # Space works for Netflix and often for YT (when video focused).
        # YouTube also supports 'k', you can change this if you prefer.
        keyboard.send("space")
    elif cmd == "forward_arrow":
        keyboard.send("right")   # 5s/10s forward depending on player
    elif cmd == "rewind_arrow":
        keyboard.send("left")    # 5s/10s back depending on player
    elif cmd == "vol_up":
        keyboard.send("up")
    elif cmd == "vol_down":
        keyboard.send("down")
    elif cmd == "mute":
        keyboard.send("m")
    elif cmd == "fullscreen":
        keyboard.send("f")

    # --- YouTube-specific skip 10s ---
    elif cmd == "yt_forward_10":
        keyboard.send("l")       # YT: +10s
    elif cmd == "yt_back_10":
        keyboard.send("j")       # YT: -10s

    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
