# secure-password-generator-2025-v1

A robust and secure Python script designed for the automated generation and management of strong, unique credentials. It safely stores passwords in a timestamped, traceable file, serving as a foundational tool for credential rotation practices.

## ✨ Features
🔒 **Secure Password Generation:** Utilizes Python's secrets module to generate cryptographically strong passwords from a comprehensive pool of letters, numbers, and symbols.

📁 **Unique File Management:** Employs a robust filename generation strategy to prevent overwriting previous password lists.

🛡️ **Safe File Handling:** Uses a context manager ```(with open())``` for secure and reliable file operations, preventing data corruption and resource leaks.

📝 **Automated Metadata:** Includes a detailed metadata footer in each output file for full traceability, containing a timestamp, author, tool version, and purpose.

⚙️ **Highly Customizable:** Easily configurable list of accounts and password length.

## 🛠️ Technical Breakdown
The script is modular and follows a clear, sequential logic for credential generation and storage.

### 1. Secure Password Generation (generate_password)
This function is the security core of the application.

**Character Pool:** Combines character sets from ```string.ascii_letters```, ```string.digits```, and ```string.punctuation```.

**Cryptographic Randomness:** Uses ```secrets.choice()``` to select each character, drawing from the operating system's most secure source of randomness. This makes the passwords highly unpredictable and resilient against brute-force attacks.

### 2. Unique Filename Generation (get_next_filename)
This function ensures each run creates a new file, preventing data loss.

Employs a loop that increments a counter to check for existing filenames (e.g., **acc_pass.txt**, **acc_pass1.txt**).

Uses ```os.path.exists()``` to verify a filename is available before returning it.

### 3. Secure File Handling & Metadata
**Context Manager:** The ```with open()``` statement automatically ensures the file is properly closed after execution, even if an error occurs.

**Self-Contained Files:** Each generated file includes a metadata footer with:

**Timestamp:** Generation time in ISO format with timezone (SAST).

**Tool Version:** The Python version used.

**Author & Purpose:** Context for the file's origin and intended use.

## 🚀 Installation & Usage

### Prerequisites

Python 3.6+ (Required for the secrets module and zoneinfo).

### Steps

**Clone the repository:**

bash

```
git clone https://github.com/codebyangelo/secure-password-generator-2025-v1
cd secure-password-generator-2025-v1
```

**Run the script:**

bash

```python3 passgen.py```

**Output:**

The script will generate a new file (e.g., acc_pass.txt) and print its name to the terminal upon completion.

bash

```✅ Passwords saved to: acc_pass.txt```

### 📁 Example Output

A generated password file (acc_pass.txt) will look like this:

text
```
Facebook: 7hG$g@2!L8pV+sT4qW1*
GitHub: f#k5M@b9K3%pR6vN2&dL
Instagram: P8m@x!S5$vT3qW7zL2&
Google: 2@9L!pX8$sT4qW7zV1*
Microsoft: 5&hG@k9M!pR6vN2$dL8
TikTok: 7$vT3qW!zL2&pX8sT4gH
Reddit: k9M!pR6vN2$dL8&hG@k5
Roblox: 2!L8pV+sT4qW1*7hG$g@

--- Metadata ---
Generated: 2023-10-27T14:32:15.123456+02:00
Tool: Python 3.10.12
Author: Angelo Ayton - Security Systems Architect
Purpose: Password list for provisioning and rotating credentials
```


## 🔧 Configuration

The tool is easily configured by modifying the constants at the top of the passgen.py script:

python
```
# Configuration Constants
ACCOUNTS = ["Facebook", "GitHub", "Instagram", "Google", "Microsoft", "TikTok", "Reddit", "Roblox"]
DEFAULT_PASSWORD_LENGTH = 18
BASE_FILENAME = "acc_pass"
FILE_EXTENSION = ".txt"
TIMEZONE = ZoneInfo("Africa/Johannesburg")
```

## 🔮 Future Improvements

This tool is designed to be expanded. Potential enhancements include:

**Command-Line Interface (CLI):** Integrate the argparse module to allow users to specify password length, output filename, and accounts directly from the terminal.

**Password Manager Integration:** Explore using APIs (e.g., Bitwarden, 1Password) to automatically push generated credentials.

**File Encryption:** Implement encryption (e.g., using cryptography library) to protect the password list at rest.

**File Integrity Checks:** Add a cryptographic hash (e.g., SHA-256) of the file contents to the metadata for integrity verification.

## 📄 License

Licensed under the Apache License, Version 2.0 (the "License"). See the LICENSE file for details.

## 👨‍💻 Author

Angelo Ayton - Security Systems Architect

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
