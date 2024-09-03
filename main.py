from pystyle import *
import requests
import ctypes
import os
import sys
import time
import random
import webbrowser
import winreg as reg
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
    bar = Colors.red + Center.XCenter("█" * filled_length + '░' * (length - filled_length))
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

def menu():
    System.Clear()
    print(Colors.red + Center.XCenter(Add.Add(logo, title, 5)))
    print(Colors.red + Center.XCenter("\nMENU:\n"))
    options = """            Type a number to select.

TERMINAL OPTIONS                COMPUTER OPTIONS

1: Clear Terminal               3: Toggle Dark Mode
2: Exit                         4: Install VortexOS
                                5: Change wallpaper
"""
    print(Colors.red + Center.XCenter(Box.DoubleCube(options)))

    while True:
        choice = input("\n> ")
        
        if choice == '1':
            menu()
            break
        elif choice == '2':
            print("\nExiting...")
            System.Clear()
            break
        elif choice == '3':
            darkmode()
        elif choice == '4':
            print("Opening VortexOS...")
            webbrowser.get(using='chrome').open("https://vortexos.onrender.com/")
        else:
            print("\nInvalid option.")
            time.sleep(1)

System.Clear()
System.Title("Supernova")
print(Colorate.Horizontal(Colors.DynamicMIX((Col.red, Col.orange)), Center.XCenter(intro + "\n\n\n")))
print(Colors.red + Center.XCenter(title))
print(Colors.red + Center.XCenter("\n\nLoading...\n\n"))
for i in range(101):
    time.sleep(random.uniform(0, 0.05))
    progress(i, 100)
menu()

