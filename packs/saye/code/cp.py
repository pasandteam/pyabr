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

def cp (src,dest):
    ## check src ##
    if files.isdir (src):
        if files.isfile (dest):
            colors.show("cp", "fail", dest + ": dest is a file.")
        else:
            if permissions.check(files.output(src), "r",files.readall ("/proc/info/su")):
                if permissions.check(files.output(dest), "w", files.readall ("/proc/info/su")):
                    perm = permissions.get_permissions(files.output(src))
                    control.write_record(files.output(dest), perm, "/etc/permtab")
                    files.copydir (src,dest)

                else:
                    colors.show ("cp","perm","")
            else:
                colors.show("cp","perm","")
    elif files.isfile (src):
        if files.isdir (dest):
            colors.show("cp", "fail", dest + ": dest is a directory.")
        else:
            if permissions.check(files.output(src), "r", files.readall ("/proc/info/su")):
                if permissions.check(files.output(dest), "w", files.readall ("/proc/info/su")):
                    perm = permissions.get_permissions(files.output(src))
                    control.write_record(files.output(dest), perm, "/etc/permtab")
                    files.copy (src,dest)
                else:
                    colors.show ("cp","perm","")
            else:
                colors.show ("cp","perm","")
    else:
        colors.show ("cp","fail",src+": source not found.")

cmdln = ['']
cmdln[1:] = sys.argv[1:]

if cmdln[1:] == []:
    colors.show("cp", "fail", "no inputs.")
else:
    if cmdln[2:] == []:
        colors.show("cp", "fail", "no inputs.")
    else:
        cp(cmdln[1], cmdln[2])
        colors.show('', 'ok', 'Copy \'' + cmdln[1] + '\' to \'' + cmdln[2] + '\'.')