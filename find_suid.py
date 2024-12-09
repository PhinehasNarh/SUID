import os

def find_suid_binaries():
    """
    Searches the system for SUID binaries and prints them.
    """
    print("[+] Searching for SUID binaries...\n")
    suid_binaries = []
    
    for root, dirs, files in os.walk("/"):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                if os.path.islink(file_path):  # Skip symbolic links
                    continue
                # Check if the file has SUID permissions
                if os.stat(file_path).st_mode & 0o4000:
                    suid_binaries.append(file_path)
            except Exception as e:
                continue
    
    if suid_binaries:
        print("[+] Found SUID binaries:")
        for binary in suid_binaries:
            print(f"    {binary}")
    else:
        print("[-] No SUID binaries found.")
    
    print("\n[!] Remember to check these binaries for known privilege escalation vulnerabilities.")

if __name__ == "__main__":
    find_suid_binaries()
