import keyboard
import mouse
from os import system
from time import sleep
import os
from colorama import Fore

def space():
    print()
system("cls") # le clear
def __main__():
    print(Fore.CYAN + """
                    __  __  _____    _____ _____        __  __ __  __ ______ _____  
                   |  \/  |/ ____|  / ____|  __ \ /\   |  \/  |  \/  |  ____|  __ \ 
                   | \  / | |      | (___ | |__) /  \  | \  / | \  / | |__  | |__) |
                   | |\/| | |       \___ \|  ___/ /\ \ | |\/| | |\/| |  __| |  _  / 
                   | |  | | |____   ____) | |  / ____ \| |  | | |  | | |____| | \ \ 
                   |_|  |_|\_____| |_____/|_| /_/    \_\_|  |_|_|  |_|______|_|  \_\\
    """)
    space()
    spammed = input(Fore.RED +"[+] Texte a spam : ")
    msgnumber = int(input("[+] Nombre de messages a spam : "))
    system("cls")
    print(Fore.GREEN + "[+] Le spam va commencé dans 3s")
    sleep(3)
    system("cls")
    print("[+] Le spam va commencé dans 2s")
    sleep(4)
    system("cls")
    print("[+] Le spam va commencé dans 1s")
    sleep(5)
    system("cls")
    print("[~] Spam en cours...")
    for i in range(msgnumber):
        sleep(0.05)
        keyboard.press_and_release('t')
        sleep(0.04)
        keyboard.write(spammed)
        sleep(0.04)
        keyboard.press_and_release('enter')
    system("cls")
    print("[+] Spam fini avec succès !")
    input()
__main__()