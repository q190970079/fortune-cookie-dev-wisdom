#!/usr/bin/env python3
"""Write one fortune-cookie line for a software developer to /output/entry.txt."""

import os

TEXT = "You will inherit code from a stranger who shares your name, your habits, and all your worst shortcuts."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
