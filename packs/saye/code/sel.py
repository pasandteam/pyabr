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

def sel (database_name):
    if files.isfile(database_name):
        if permissions.check (files.output(database_name),"r",files.readall("/proc/info/su")):
            files.write("/proc/info/sel", database_name)
            files.create("/proc/selected")
            colors.show('', 'ok', "Select '" + database_name + "' controller.")
        else:
            colors.show ("sel","perm","")
    else:
        colors.show("sel", "fail", database_name + ": controller not found.")

if not sys.argv[1:] == []:
    sel(sys.argv[1])
else:
    colors.show("sel", "fail", "no inputs.")