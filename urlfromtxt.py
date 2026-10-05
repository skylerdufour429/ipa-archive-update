import subprocess
import sys

# Read URLs from a text file
try:
    with open('urls.txt', 'r') as file:
        urls = file.readlines()
except FileNotFoundError:
    print("Error: urls.txt not found.")
    sys.exit(1)

# Iterate over each URL and run the command
for url in urls:
    url = url.strip()  # Remove any leading/trailing whitespace or newline characters
    if url:  # Ensure the line isn't empty
        print(f"Adding URL: {url}")
        # Use subprocess.run with a list for safe execution (avoids shell injection)
        try:
            subprocess.run([sys.executable, "main.py", "add", url], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error adding {url}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred with {url}: {e}")
