import os
import subprocess
import sys
from pathlib import Path

def install_required_packages():
    required_packages = ['requests', 'pystyle']
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"{package} is already installed.")
        except ImportError:
            print(f"{package} not found. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    install_required_packages()
    print(f"Setup complete!")
