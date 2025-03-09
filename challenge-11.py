# 🔹 Challenge 11: Package your Python script as a CLI tool using argparse and click.

import argparse

def greet(name, uppercase):
    """Prints a greeting message."""
    message = f"Hello, {name}!"
    if uppercase:
        message = message.upper()
    print(message)

def main():
    parser = argparse.ArgumentParser(description="Simple CLI tool to greet users.")
    
    parser.add_argument("name", type=str, help="Name of the person to greet")
    parser.add_argument("-u", "--uppercase", action="store_true", help="Convert the greeting to uppercase")
    
    args = parser.parse_args()
    greet(args.name, args.uppercase)

if __name__ == "__main__":
    main()