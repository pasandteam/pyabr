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
import sys, os, hashlib
from libnam import files, control, permissions, colors

def udel (input_username,user):
    ## Check not exists user account ##
    if input_username==user:
        colors.show ("udel","fail",input_username+": cannot remove switched user.")
    else:
        if permissions.check_root(user):
            if not files.isfile("/etc/users/" + input_username):
                colors.show("udel", "fail", input_username + ": user not found.")
            else:
                if input_username == "root":
                    colors.show("udel", "fail", input_username + ": is a permanet user.")
                else:
                    hashname = hashlib.sha3_256(str(input_username).encode()).hexdigest()  ## Create hashname
                    username = control.read_record("username", "/etc/users/" + input_username)

                    if not hashname == username:
                        colors.show("udel", "fail", input_username + ": user not found.")
                    else:
                        files.remove("/etc/users/" + input_username)
                        if files.isdir ('/desk/'+input_username):
                            files.removedirs("/desk/" + input_username)
                        colors.show('', 'ok', "Remove '" + input_username + "' user account.")
        else:
            colors.show ("udel","perm","")

if not sys.argv[1:] == []:
    udel(sys.argv[1],files.readall ("/proc/info/su"))
else:
    colors.show("udel", "fail", "no inputs.")