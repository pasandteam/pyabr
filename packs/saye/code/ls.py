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

def ls (path,options):
    if options=="":
        if files.isdir(path):
            if permissions.check(files.output(path),"r",files.readall("/proc/info/su")):
                list = files.list(path)
                list.sort()
                for i in list:
                    if files.isdir(path + "/" + i):
                        print(colors.get_path() + i + "/" + colors.get_colors())
                    else:
                        print(i)
            else:
                colors.show ("ls","perm","")
        else:
            colors.show("ls", "fail", path + ": directory not found.")
    elif options=="-p":
        if files.isdir(path):
            if permissions.check(files.output(path), "r", files.readall("/proc/info/su")):
                list = files.list(path)
                list.sort()
                for i in list:
                    if files.isdir(path + "/" + i):
                        perm = permissions.get_permissions(path + "/" + i)
                        print(perm + "\t" + colors.get_path() + i + "/" + colors.get_colors())
                    else:
                        perm = permissions.get_permissions(path + "/" + i)
                        print(perm + "\t" + i)
            else:
                colors.show("ls", "perm", "")
        else:
            colors.show("ls", "fail", path + ": directory not found.")
    elif options=="-n":
        if files.isdir(path):
            if permissions.check(files.output(path), "r", files.readall("/proc/info/su")):
                list = files.list(path)
                list.sort()
                for i in list:
                    if files.isdir(path + "/" + i):
                        perm = permissions.get_permissions(path + "/" + i)
                        perm = str(permissions.show_number(perm))
                        print(perm + "\t" + colors.get_path() + i + "/" + colors.get_colors())
                    else:
                        perm = permissions.get_permissions(path + "/" + i)
                        perm = str(permissions.show_number(perm))
                        print(perm + "\t" + i)
            else:
                colors.show("ls", "perm", "")
        else:
            colors.show("ls", "fail", path + ": directory not found.")

if not sys.argv[1:] == [] and sys.argv[2:]==[]:
    ls(files.output(sys.argv[1]),"")
elif not sys.argv[1:]==[] and not sys.argv[2:]==[]:
    ls(files.output(sys.argv[1]), sys.argv[2])
elif sys.argv[1:]==[]:
    ls(files.readall("/proc/info/pwd"),"")