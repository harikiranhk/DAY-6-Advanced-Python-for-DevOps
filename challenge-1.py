# 🔹 Challenge 1: Create a Python script that connects to a remote server via SSH using paramiko.

import paramiko

def ssh_connect(hostname, username=None, password=None, key_path=None, command=None):
    """Connects to a remote server via SSH and executes a command."""
    
    try:
        # Create an SSH client
        client = paramiko.SSHClient()
        
        # Automatically accept unknown host keys (Not recommended for production)
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        print(f"🔌 Connecting to {hostname}...")

        if key_path:
            # Connect using SSH key
            client.connect(hostname, username=username, key_filename=key_path, timeout=10)
        else:
            # Connect using username and password
            client.connect(hostname, username=username, password=password, timeout=10)

        print(f"✅ Connected to {hostname}")

        # Execute the command
        stdin, stdout, stderr = client.exec_command(command)

        # Print command output
        print("📜 Command Output:")
        print(stdout.read().decode())

        # Print errors if any
        error = stderr.read().decode()
        if error:
            print(f"❌ Error:\n{error}")

        # Close the connection
        client.close()
        print("🔌 Disconnected.")

    except paramiko.AuthenticationException:
        print("❌ Authentication failed. Check your credentials.")
    except paramiko.SSHException as e:
        print(f"❌ SSH error: {e}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

# User input for authentication method
auth_method = input("Choose authentication method (1: Username & Password, 2: SSH Key): ")

hostname = input("Enter remote server IP or hostname: ")

if auth_method == "1":
    username = input("Enter SSH username: ")
    password = input("Enter SSH password: ")
    key_path = None
elif auth_method == "2":
    username = input("Enter SSH username: ")
    key_path = input("Enter path to SSH private key: ")
    password = None
else:
    print("❌ Invalid selection. Exiting.")
    exit()

command = input("Enter command to execute: ")

ssh_connect(hostname, username, password, key_path, command)