#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Pasand team. GNU General Public License v3.0
#
#  Offical website:         http://itpasand.com
#  Telegram or Gap channel: @pyabr
#  Telegram or Gap group:   @pyabr_community
#  Git source:              github.com/pasandteam/pyabr
#
#######################################################################################

# This script would install Pyabr in PyBoot mode #

import shutil, os, hashlib, getpass,sys

if not input ("Do you want to install Pyabr? (Y/n): ").lower()=='y':
    exit()

rootcode = getpass.getpass ("Enter a new root code: ")
username = input ("Enter a new username: ")
password = getpass.getpass ("Enter new "+username+"'s password: ")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
email = input ("Enter your email address: ")
phone = input ("Enter your phone number: ")
if input("Do you want to enable guest user? (Y/n): ").lower()=='y':
    guest = 'Yes'
else:
    guest = 'No'
if input ("Choose your interface (GUI/GLI): ").upper()=="GUI":
    interface = "GUI"
else:
    interface = "CLI"

## Compile Pyabr ##
os.system("\"" + sys.executable + "\" pre-build.py")
os.system("\"" + sys.executable + "\" build.py")
os.system("\"" + sys.executable + "\" -m pip install getmac pyqtconsole wget gitpython getmac py-cpuinfo")

## Setting up Root user ##
file = open("stor/etc/users/root", "w")
file.write("username: " + hashlib.sha3_256("root".encode()).hexdigest() + "\n")
file.write("code: " + hashlib.sha3_512(rootcode.encode()).hexdigest() + "\n")
file.close()

## Setting up Standard user ##
file = open("stor/etc/users/" + username, "w")
file.write("username: " + hashlib.sha3_256(username.encode()).hexdigest() + "\n")
file.write("code: " + hashlib.sha3_512(password.encode()).hexdigest() + "\n")
file.write("first_name: " + first_name + "\n")
file.write("last_name: " + last_name + "\n")
file.write("email: " + email + "\n")
file.write("phone: " + phone + "\n")
file.close()

file = open("stor/etc/permtab", "a")
file.write("/desk/" + username + ": drwxr-x---/" + username + "\n")
file.close()

## Setting up Guest user ##
file = open("stor/etc/guest", "w")
file.write("enable_cli: "+guest+"\n")
file.write("enable_gui: "+guest+"\n")
file.close()

## Setting up interface ##
file = open("stor/etc/interface", "w")
file.write(interface)
file.close()

## Setting up administor ##
file = open("stor/etc/sudoers", "w")
file.write(username)
file.close()

input ("Pyabr has alreay installed in stor folder; Press Enter key to exit.")