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

def cd (path):
    if permissions.check(files.output(path),"r",files.readall("/proc/info/su")):
        if path=='..':
            pwd = files.readall('/proc/info/pwd')
            pwd = pwd.split ('/')
            lens = len(pwd)-1
            pwd.pop(lens)

            strv = ''

            for i in pwd:
                strv += "/"+i

            pwd = files.output_shell(strv)
            files.write("/proc/info/pwd",pwd)
        elif files.isdir(path):
            files.write("/proc/info/pwd", files.output_shell(path))
        else:
            colors.show("cd", "fail", path + ": directory not found.")
    else:
        colors.show ("cd","perm","")


if not sys.argv == []:
    cd(sys.argv[1])
else:
    colors.show("cd", "fail", "no inputs.")