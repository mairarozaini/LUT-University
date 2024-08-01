import sys

if len(sys.argv) != 2:
    print("Usage: python read_file.py <filename>")
    exit()

try:
    with open(sys.argv[1], "r") as f:
        print(f"Contents of {sys.argv[1]}:\n{f.read()}")
except FileNotFoundError:
    print(f"Error: File '{sys.argv[1]}' does not exist.")