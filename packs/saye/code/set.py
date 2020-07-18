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
from libnam import files, control, permissions, colors, process

def set (name,value):
    select = files.readall("/proc/info/sel")
    if not select.startswith ("/proc/"):
        if permissions.check(files.output(select),"w",files.readall("/proc/info/su")):
            control.write_record(name, value, select)
            colors.show('', 'ok', "Set '" + name + "' as '"+value+"'.")
        else:
            colors.show ("set","perm","")
    else:
        control.write_record(name,value,select)


if sys.argv[1:] == []:
    colors.show("set", "fail", "no inputs.")
else:
    if sys.argv[2:] == []:
        colors.show("set", "fail", "no inputs.")
    else:
        if sys.argv[1].endswith(":"):
            set(sys.argv[1].replace(":", ""), sys.argv[2])
        else:
            colors.show("set", "fail", "wrong syntax.")