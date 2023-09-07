import os
from colorama import init, Fore
init()
print(Fore.RED + "Please Change To Root Terminal")
duso = input(Fore.CYAN + "App Names In Package apt:")
os.system("apt-get install " + duso)