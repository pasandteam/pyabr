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

## @commands/rm ##

def rm (names):
    for i in names:
        if files.isdir (i):
            if permissions.check(files.output(i), "w", files.readall ("/proc/info/su")):
                files.removedirs(i)
                colors.show('', 'ok', "Remove '"+i+"' directory.")
            else:
                colors.show ("rm","perm","")
                sys.exit(0)
        elif files.isfile (i):
            if permissions.check(files.output(i), "w", files.readall ("/proc/info/su")):
                files.remove(i)
                colors.show('', 'ok', "Remove '" + i + "' file.")
            else:
                colors.show ("rm","perm","")
                sys.exit(0)
        else:
            colors.show("rm", "fail", i + ": file or directory not found.")
            sys.exit(0)

rm(sys.argv[1:])