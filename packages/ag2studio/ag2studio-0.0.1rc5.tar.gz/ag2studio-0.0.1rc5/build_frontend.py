# Copyright (c) 2023 - 2025, Owners of https://github.com/ag2ai
#
# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
import sys
from pathlib import Path

def run_command(command, cwd=None):
    """Run a command and return its result."""
    try:
        subprocess.run(command, cwd=cwd, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command {command}: {e}")
        sys.exit(1)

def build_frontend():
    """Build the frontend assets."""
    # Get the directory where this script is located
    root_dir = Path(__file__).parent.absolute()
    frontend_dir = root_dir / "frontend"
    
    # Check if yarn is installed
    try:
        subprocess.run(["yarn", "--version"], check=True, capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Yarn is not installed. Please install yarn first.")
        sys.exit(1)
    
    # Build frontend
    print("Building frontend...")
    run_command("yarn install", cwd=frontend_dir)
    run_command("yarn build", cwd=frontend_dir)

if __name__ == "__main__":
    build_frontend()