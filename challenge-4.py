# 🔹 Challenge 4: Use Python subprocess to execute system commands and capture output.

import subprocess

def run_command(command):
    """Executes a system command and captures its output."""
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print("✅ Command executed successfully!\n")
        print("📜 Output:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed with error:\n{e.stderr}")

# Get user input for a command
command = input("Enter a system command to run: ")
run_command(command)