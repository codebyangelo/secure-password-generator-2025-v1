import secrets
import string
import os
from datetime import datetime
from zoneinfo import ZoneInfo
import platform

# Configuration Constants
ACCOUNTS = ["Facebook", "GitHub", "Instagram", "Google", "Microsoft", "TikTok", "Reddit", "Roblox"]
DEFAULT_PASSWORD_LENGTH = 18
BASE_FILENAME = "acc_pass"
FILE_EXTENSION = ".txt"
TIMEZONE = ZoneInfo("Africa/Johannesburg")

def generate_password(length: int = DEFAULT_PASSWORD_LENGTH) -> str:
    """Generate a cryptographically strong random password."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

def get_next_filename(base_name: str = BASE_FILENAME, extension: str = FILE_EXTENSION) -> str:
    """Generate a unique filename by appending a number if the base name exists."""
    i = 0
    while True:
        filename = f"{base_name}{i}{extension}" if i > 0 else f"{base_name}{extension}"
        if not os.path.exists(filename):
            return filename
        i += 1

if __name__ == "__main__":
    # Determine unique filename
    filename = get_next_filename()

    # Generate and save passwords
    with open(filename, "w") as f:
        for account in ACCOUNTS:
            password = generate_password()
            f.write(f"{account}: {password}\n")

        # === Metadata Footer ===
        f.write("\n--- Metadata ---\n")
        f.write(f"Generated: {datetime.now(TIMEZONE).isoformat()}\n")
        f.write(f"Tool: Python {platform.python_version()}\n")
        f.write(f"Author: Angelo Ayton - Security Systems Architect\n")
        f.write(f"Purpose: Password list for provisioning and rotating credentials\n")

    print(f"✅ Passwords saved to: {filename}")
