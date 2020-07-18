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
import sys, hashlib, os,getpass
from libnam import files, colors, control

def su (input_username,user):
    if files.isfile("/proc/selected"): files.remove("/proc/selected")
    if user == input_username:
        colors.show ("su","warning",user+" has already switched.")
    elif input_username=="guest":
        enable_cli = control.read_record("enable_cli", "/etc/guest")
        if enable_cli == "Yes":
            colors.show('', 'ok', "Switching '"+input_username+"' user account.")
            os.system("./"+files.readall("/proc/info/boot")+" user guest")
        else:
            colors.show(input_username, "fail", "user not found.")

    elif files.isfile ("/etc/users/"+input_username):
        hashname = hashlib.sha3_256(str(input_username).encode()).hexdigest()
        username = control.read_record("username","/etc/users/"+input_username)
        if hashname==username:
            input_password = getpass.getpass ('Enter '+input_username+'\'s password: ')
            hashcode = hashlib.sha3_512(str(input_password).encode()).hexdigest()
            password =  control.read_record("code","/etc/users/"+input_username)
            if hashcode == password:
                colors.show('', 'ok', "Switching '" + input_username + "' user account ...")
                os.system("./"+files.readall("/proc/info/boot")+" user "+input_username+" "+input_password)
            else:
                colors.show("su", "fail", input_username + ": wrong password.")
        else:
            colors.show("su", "fail", input_username + " user not found.")
    else:
        colors.show ("su","fail",input_username+" user not found.")

if sys.argv[1:]==[]:
    colors.show("su", "fail", "no inputs.")
else:
    su (sys.argv[1],files.readall("/proc/info/su"))