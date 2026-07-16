#!/usr/bin/env python3
"""Diagnostic script to check project setup."""
import os
import sys

print("=" * 50)
print("QuantForex Pro - Setup Diagnostic")
print("=" * 50)
print(f"Working directory: {os.getcwd()}")
print(f"Python version: {sys.version}")
print()

files_to_check = [
    "requirements.txt",
    "Dockerfile",
    "docker-compose.yml",
    "app/main.py",
    "app/static/index.html",
    ".env.example",
]

all_good = True
for f in files_to_check:
    exists = os.path.exists(f)
    status = "✅ FOUND" if exists else "❌ MISSING"
    if not exists:
        all_good = False
    print(f"{status}: {f}")

print()
if all_good:
    print("✅ All required files present!")
    print("
To start the server, run:")
    print("  pip install -r requirements.txt")
    print("  uvicorn app.main:app --reload")
else:
    print("❌ Some files are missing. Make sure you're in the project root.")
    print(f"
Current directory contents:")
    for item in os.listdir("."):
        print(f"  {item}")
