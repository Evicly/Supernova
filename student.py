import requests
import socket
import uuid
import time
import json
import os
import getpass
import platform

current_user = getpass.getuser()

REGISTER_URL = 'https://student-dashboard-webhooks-3.glitch.me/register'
STATUS_URL = 'https://student-dashboard-webhooks-3.glitch.me/status'
HEARTBEAT_URL = 'https://student-dashboard-webhooks-3.glitch.me/heartbeat'

ID_FILE = 'computer_id.txt'

def generate_computer_id():
    return str(uuid.uuid4())

def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

def register_computer(computer_id, ip_address):
    data = {
        'user': current_user,
        'id': computer_id,
        'ip': ip_address
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(REGISTER_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        print("Computer successfully registered!")
    else:
        print(f"Failed to register computer: {response.status_code} {response.text}")

def update_status(computer_id, status):
    data = {
        'id': computer_id,
        'status': status
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(STATUS_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        print("Status updated successfully!")
    else:
        print(f"Failed to update status: {response.status_code} {response.text}")

def send_heartbeat(computer_id):
    data = {
        'id': computer_id
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(HEARTBEAT_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        print("Heartbeat sent successfully!")
    else:
        print(f"Failed to send heartbeat: {response.status_code} {response.text}")

def check_status(computer_id):
    headers = {'Content-Type': 'application/json'}
    response = requests.get(STATUS_URL, headers=headers)
    if response.status_code == 200:
        status_data = response.json()
        if computer_id in status_data:
            return status_data[computer_id].get('status')
    else:
        print(f"Failed to fetch status: {response.status_code} {response.text}")
    return None

def shutdown_computer():
    current_os = platform.system()
    if current_os == 'Windows':
        os.system('shutdown /s /f /t 0') 
    elif current_os == 'Linux' or current_os == 'Darwin':
        os.system('sudo shutdown -h now') 

def get_computer_id():
    if os.path.exists(ID_FILE):
        with open(ID_FILE, 'r') as file:
            return file.read().strip()
    else:
        computer_id = generate_computer_id()
        with open(ID_FILE, 'w') as file:
            file.write(computer_id)
        return computer_id

def main():
    computer_id = get_computer_id()
    ip_address = get_ip_address()
    
    register_computer(computer_id, ip_address)
    
    while True:
        status = check_status(computer_id)
        if status == 'shutting down':
            print(f"Shutdown command received for computer ID: {computer_id}. Shutting down...")
            shutdown_computer()
            break
        time.sleep(5)

        
        send_heartbeat(computer_id)
        update_status(computer_id, 'online')
        
        time.sleep(55)

if __name__ == '__main__':
    main()
