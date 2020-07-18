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

def unset (name):
    select = files.readall("/proc/info/sel")
    if not select.startswith ("/proc/"):
        if permissions.check(files.output(select),"w",files.readall("/proc/info/su")):
            control.remove_record (name,select)
            colors.show('', 'ok', "Unset '" + name + "' in '"+select+' controller.')
        else:
            colors.show ("unset","perm","")
    else:
        control.remove_record (name,select)

for i in sys.argv[1:]:
    unset (i)