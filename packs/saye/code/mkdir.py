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

def mkdir (names):
    for i in names:
        if files.isfile (i):
            colors.show("mkdir", "fail", i + ": is a file.")
        elif files.isdir (i):
            colors.show("mkdir", "warning", i + ": directory exists.")
        else:
            if permissions.check (files.output(i),"w",files.readall("/proc/info/su")):
                files.makedirs (i)
                colors.show('', 'ok', 'Create \''+i+"' directory.")
            else:
                colors.show ("mkdir","perm","")
mkdir(sys.argv[1:])
