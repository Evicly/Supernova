from pystyle import *
import requests
import ctypes
import os
import sys
import time
import random
import webbrowser
import winreg as reg
import platform
import shutil

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
if not os.path.exists(chrome_path):
    print("Chrome executable not found at specified path.")
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

intro = """
                                      =                                      
                                      %:                                      
                                      @=                                      
                                      @+                                      
                                     :@#                        ..           
                                     =%@            -===- .--:::..:+         
                                     **@           *=   :@:-----+  %         
                                     %-@.          #:   .@.     +.:+         
                                     @:%-        :==++++*:     .* +          
                                     @.#=     .====:           + -:          
                                    .@ ++   --+--            :+ =-           
                                    -% -*:====.             :-               
                         -.         -# :%:=-       -       =-                
                         .#*:       =* .#       .=%-     .+                  
                           -%#-    -#+  %     .*@+      =-                   
                             =%%=--.+=  %   -*@+.     :=. =:                  
                               #@#*:*=  %.+##*.     .=: -=                   
                             == .***%=  @*+#-      .-  =:                    
              ...:::---===++%*++++#%:   .#%++++++++===%=--::...              
      .+**#%%%@@%%##*+==--::.......       .......::-#+=+**#%%@@%%%#**+-      
                     ..-*=:::----=%#=.  =*@+----:-*-:....                    
                      +-=-      =#**#=  @****.  =-                           
                    :=-=      :%%*: +=  % .+#%*=                             
                   :-+.     .*@*.   ++  %   =*@%-                            
                   -=      +@+.     ++  %.=-   =%#:                          
                 .=.     -*-        =* -%:       :++                         
              .:-=              :=- -%==*                                    
             -==:             -=: .=+@ =+                                    
            =-+:           .==. -=: .@ +=                                    
           =:+.          -=: :=-     @.#-                                    
          -:=:       :---*==*=       @:@:                                    
         .+ #    .---.:--#  -@       #=@.                                    
         =:  ----::---.  -+++.       +*@                                     
          =-------.                  =@%                                     
                                     :@#                                     
                                      @+                                     
                                      @-                                     
                                      %:                                     
"""
title = """
███████╗██╗   ██╗██████╗ ███████╗██████╗ ███╗   ██╗ ██████╗ ██╗   ██╗ █████╗ 
██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗████╗  ██║██╔═══██╗██║   ██║██╔══██╗
███████╗██║   ██║██████╔╝█████╗  ██████╔╝██╔██╗ ██║██║   ██║██║   ██║███████║
╚════██║██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗██║╚██╗██║██║   ██║╚██╗ ██╔╝██╔══██║
███████║╚██████╔╝██║     ███████╗██║  ██║██║ ╚████║╚██████╔╝ ╚████╔╝ ██║  ██║
╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝
"""
logo = """
              .:              
              --         .    
              -=    -:-:..:   
              -=  .-::. .-    
              -=::.    :      
          -- .==  --  :       
           :+====+  .:.       
   :--=======+  +=======--:.  
        ::  ======:.          
       :. -=  -=..=-          
     ::     .:=+              
    ::   .-:. -=              
   :..::::::  -=              
    ..        --              
              .:              
"""

def progress(iteration, total, length=40):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = Colorate.Horizontal(Colors.DynamicMIX((Col.red, Col.orange)), Center.XCenter("█" * filled_length + '░' * (length - filled_length)))
    sys.stdout.write(f'\r{bar}')
    sys.stdout.flush()

def darkmode():
    personalize_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize"
    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, personalize_path, 0, reg.KEY_READ | reg.KEY_SET_VALUE)
        apps_use_light_theme, _ = reg.QueryValueEx(key, "AppsUseLightTheme")
        new_value = 0 if apps_use_light_theme == 1 else 1
        reg.SetValueEx(key, "AppsUseLightTheme", 0, reg.REG_DWORD, new_value)
        reg.SetValueEx(key, "SystemUsesLightTheme", 0, reg.REG_DWORD, new_value)
        reg.CloseKey(key)
        enabled = "enabled" if new_value == 0 else "disabled"
        print(f"Dark mode {enabled} successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def change_wallpaper():
    image_url = input("Enter the image URL for the new wallpaper: ")
    response = requests.get(image_url)
    file_path = os.path.join(os.getenv('TEMP'), 'new_wallpaper.jpg')
    with open(file_path, 'wb') as f:
        f.write(response.content)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, file_path, 3)
    print("Wallpaper changed successfully.")

def system_info():
    print("Fetching system information...\n")
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")

def disk_usage():
    total, used, free = shutil.disk_usage("/")
    print(f"Total: {total // (2**30)} GB")
    print(f"Used: {used // (2**30)} GB")
    print(f"Free: {free // (2**30)} GB")

def network_info():
    print("Fetching network information...\n")
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip = response.json()['ip']
        print(f"Public IP Address: {ip}")
    except Exception as e:
        print(f"An error occurred: {e}")

def open_url():
    url = input("Enter the URL to open: ")
    webbrowser.open(url)
    print(f"Opening URL: {url}")

def adjust_power_settings():
    print("Adjusting power settings...\n")
    print("1: Set Power Plan to High Performance")
    print("2: Set Power Plan to Balanced")
    print("3: Set Power Plan to Power Saver")
    choice = input("\n> ")
    try:
        if choice == '1':
            os.system('powercfg /s SCHEME_MIN')
            print("Power plan set to High Performance.")
        elif choice == '2':
            os.system('powercfg /s SCHEME_BALANCED')
            print("Power plan set to Balanced.")
        elif choice == '3':
            os.system('powercfg /s SCHEME_POWER')
            print("Power plan set to Power Saver.")
        else:
            print("Invalid option.")
    except Exception as e:
        print(f"An error occurred: {e}")

def manage_startup_programs():
    print("Managing startup programs...\n")
    print("1: List Startup Programs")
    print("2: Add Startup Program")
    print("3: Remove Startup Program")
    choice = input("\n> ")
    if choice == '1':
        startup_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
        try:
            key = reg.OpenKey(reg.HKEY_CURRENT_USER, startup_path, 0, reg.KEY_READ)
            i = 0
            while True:
                try:
                    value_name = reg.EnumValue(key, i)[0]
                    print(f"Startup Program: {value_name}")
                    i += 1
                except OSError:
                    break
            reg.CloseKey(key)
        except Exception as e:
            print(f"An error occurred: {e}")
    elif choice == '2':
        name = input("Enter the name of the program: ")
        path = input("Enter the full path of the program: ")
        try:
            key = reg.OpenKey(reg.HKEY_CURRENT_USER, startup_path, 0, reg.KEY_SET_VALUE)
            reg.SetValueEx(key, name, 0, reg.REG_SZ, path)
            reg.CloseKey(key)
            print(f"Added {name} to startup.")
        except Exception as e:
            print(f"An error occurred: {e}")
    elif choice == '3':
        name = input("Enter the name of the program to remove: ")
        try:
            key = reg.OpenKey(reg.HKEY_CURRENT_USER, startup_path, 0, reg.KEY_SET_VALUE)
            reg.DeleteValue(key, name)
            reg.CloseKey(key)
            print(f"Removed {name} from startup.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid option.")

def terminal_menu():
    System.Clear()
    print(Colorate.Horizontal(Colors.DynamicMIX((Col.red, Col.orange)), Center.XCenter(Add.Add(logo, title, 5))))
    print(Colorate.Horizontal(Colors.DynamicMIX((Col.red, Col.orange)), Center.XCenter("TERMINAL OPTIONS\n")))
    options = """1: Clear Terminal
2: Open URL
3: Back to Main Menu"""
    print(Colorate.Horizontal(Colors.DynamicMIX((Col.red, Col.orange)), Center.XCenter(Box.DoubleCube(options))))
    
    while True:
        choice = input(Colors.red + "\n> ")
        if choice == '1':
            System.Clear()
        elif choice == '2':
            open_url()
        elif choice == '3':
            main_menu()
            break
        else:
            print("\nInvalid option.")
            time.sleep(1)

def computer_menu():
    System.Clear()
    print(Colorate.Horizontal(Colors.DynamicMIX((Col.red, Col.orange)), Center.XCenter(Add.Add(logo, title, 5))))
    print(Colorate.Horizontal(Colors.DynamicMIX((Col.red, Col.orange)), Center.XCenter("COMPUTER OPTIONS\n")))
    options = """1: Toggle Dark Mode
2: Change Wallpaper
3: System Information
4: Disk Usage
5: Network Information
6: Back to Main Menu"""
    print(Colorate.Horizontal(Colors.DynamicMIX((Col.red, Col.orange)), Center.XCenter(Box.DoubleCube(options))))

    while True:
        choice = input(Colors.red + "\n> ")
        if choice == '1':
            darkmode()
        elif choice == '2':
            change_wallpaper()
        elif choice == '3':
            system_info()
        elif choice == '4':
            disk_usage()
        elif choice == '5':
            network_info()
        elif choice == '6':
            main_menu()
            break
        else:
            print("\nInvalid option.")
            time.sleep(1)

def settings_menu():
    System.Clear()
    print(Colorate.Horizontal(Colors.DynamicMIX((Col.red, Col.orange)), Center.XCenter(Add.Add(logo, title, 5))))
    print(Colorate.Horizontal(Colors.DynamicMIX((Col.red, Col.orange)), Center.XCenter("SETTINGS OPTIONS\n")))
    options = """1: Adjust Power Settings
2: Manage Startup Programs
3: Back to Main Menu"""
    print(Colorate.Horizontal(Colors.DynamicMIX((Col.red, Col.orange)), Center.XCenter(Box.DoubleCube(options))))

    while True:
        choice = input(Colors.red + "\n> ")
        if choice == '1':
            adjust_power_settings()
        elif choice == '2':
            manage_startup_programs()
        elif choice == '3':
            main_menu()
            break
        else:
            print("\nInvalid option.")
            time.sleep(1)

def main_menu():
    System.Clear()
    print(Colorate.Horizontal(Colors.DynamicMIX((Col.red, Col.orange)), Center.XCenter(Add.Add(logo, title, 5))))
    print(Colorate.Horizontal(Colors.DynamicMIX((Col.red, Col.orange)), Center.XCenter("\nMAIN MENU:\n")))
    options = """1: Terminal Options
2: Computer Options
3: Settings
4: Exit"""
    print(Colorate.Horizontal(Colors.DynamicMIX((Col.red, Col.orange)), Center.XCenter(Box.DoubleCube(options))))

    while True:
        choice = input(Colors.red + "\n> ")
        if choice == '1':
            terminal_menu()
            break
        elif choice == '2':
            computer_menu()
            break
        elif choice == '3':
            settings_menu()
            break
        elif choice == '4':
            print("\nExiting...")
            System.Clear()
            break
        else:
            print("\nInvalid option.")
            time.sleep(1)

System.Clear()
System.Title("Supernova")
print(Colorate.Horizontal(Colors.DynamicMIX((Col.red, Col.orange)), Center.XCenter(intro + "\n\n\n")))
print(Colorate.Horizontal(Colors.DynamicMIX((Col.red, Col.orange)), Center.XCenter(title)))
print(Colorate.Horizontal(Colors.DynamicMIX((Col.red, Col.orange)), Center.XCenter("\n\nLoading...\n\n")))

for i in range(101):
    time.sleep(random.uniform(0, 0.05))
    progress(i, 100)

main_menu()
