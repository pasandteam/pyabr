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


def mv (src,dest):
    if files.isdir (src):
        if files.isfile (dest):
            colors.show("mv", "fail", dest + ": dest is a file.")
        else:
            if permissions.check(files.output(src), "r", files.readall("/proc/info/su")) and permissions.check(files.output(src), "w", files.readall("/proc/info/su")):
                if permissions.check(files.output(dest), "w", files.readall("/proc/info/su")):
                    perm = permissions.get_permissions(files.output(src))
                    control.write_record(files.output(dest), perm, "/etc/permtab")
                    files.copydir (src,dest)
                    files.removedirs(src)
                else:
                    colors.show("mv", "perm", "")
            else:
                colors.show("mv", "perm", "")
    elif files.isfile (src):
        if files.isdir (dest):
            colors.show("mv", "fail", dest + ": dest is a directory.")
        else:
            if permissions.check(files.output(src), "r", files.readall("/proc/info/su")) and permissions.check(files.output(src), "w", files.readall("/proc/info/su")):
                if permissions.check(files.output(dest), "w", files.readall("/proc/info/su")):
                    perm = permissions.get_permissions(files.output(src))
                    control.write_record(files.output(dest), perm, "/etc/permtab")
                    files.copy (src,dest)
                    files.remove(src)
                else:
                    colors.show("mv", "perm", "")
            else:
                colors.show("mv", "perm", "")
    else:
        colors.show ("mv","fail",src+": source not found.")

cmdln = ['']
cmdln[1:] = sys.argv[1:]

if cmdln[1:] == []:
    colors.show("mv", "fail", "no inputs.")
else:
    if cmdln[2:] == []:
        colors.show("mv", "fail", "no inputs.")
    else:
        mv(cmdln[1], cmdln[2])
        colors.show('', 'ok', 'Cut \''+cmdln[1]+" to "+cmdln[2]+".")