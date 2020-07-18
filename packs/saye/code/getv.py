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

def getv ():
    select = files.readall("/proc/info/sel")
    if not select.startswith ("/proc/"):
        if permissions.check(files.output(select),"w",files.readall("/proc/info/su")):
            listinfo = files.list("/proc/info")
            for i in listinfo:
                control.write_record(i, files.readall("/proc/info/" + i), select)
        else:
            colors.show ("getv","perm","")
    else:
        listinfo = files.list ("/proc/info")
        for i in listinfo:
            control.write_record(i,files.readall("/proc/info/"+i),select)
    colors.show('', 'ok', 'Insert informations into \''+select+"\' controller.")

getv()