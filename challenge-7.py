# 🔹 Challenge 7: Write a Python program to parse log files and extract failed SSH login attempts.

import re

LOG_FILE = "/var/log/auth.log"  # Modify if using a different log file

def parse_ssh_failures(log_file):
    """Parses the log file and extracts failed SSH login attempts."""
    
    try:
        with open(log_file, "r") as file:
            logs = file.readlines()
        
        failed_attempts = []

        # Regular expression to match failed SSH login attempts
        ssh_fail_pattern = re.compile(r"Failed password for (invalid user )?(\S+) from (\d+\.\d+\.\d+\.\d+) port \d+")

        for line in logs:
            match = ssh_fail_pattern.search(line)
            if match:
                user = match.group(2)
                ip_address = match.group(3)
                failed_attempts.append((user, ip_address))

        # Print extracted failed login attempts
        print("📜 Failed SSH Login Attempts:")
        for user, ip in failed_attempts:
            print(f"🔴 User: {user} | IP: {ip}")

    except FileNotFoundError:
        print(f"❌ Error: Log file '{log_file}' not found!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

# Run the log parsing function
parse_ssh_failures(LOG_FILE)