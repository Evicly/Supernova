import os
import requests
import time
import tkinter as tk
from tkinter import messagebox

webhook_url = 'http://10.17.65.66:5000/student'

def check_shutdown_command():
    try:
        response = requests.post(webhook_url)
        if response.status_code == 200:
            os.system("shutdown /s /t 0")
    except Exception as e:
        print(f"Error checking shutdown: {e}")

if __name__ == "__main__":
    while True:
        check_shutdown_command()
        time.sleep(10)
