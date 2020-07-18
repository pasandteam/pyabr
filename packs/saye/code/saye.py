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
from libabr import core

if sys.argv[1:]==[]:
    colors.show ("saye","fail","no inputs.")
    sys.exit(0)

filename = sys.argv[1]

if not permissions.check (files.output(filename)+'.sa',"x",files.readall("/proc/info/su")):
    colors.show ("saye","perm","")
    sys.exit(0)

if not files.isfile (filename+'.sa'):
    colors.show ("saye","fail",filename+": script file not found.")
    sys.exit(0)

cmdall = control.read_list (filename+'.sa')

k = 0

for cmd in cmdall:
    k = k + 1
    ## Create cmdln with variables ##
    cmdln = cmd.split (" ")

    strcmdln = ""

    for i in cmdln:
        if str(i).startswith("$"):
            select = files.readall("/proc/info/sel")
            var = control.read_record(str(i).replace("$", ""), select)
            if var == None:
                strcmdln = strcmdln + " " + i
            else:
                strcmdln = strcmdln + " " + var
        else:
            strcmdln = strcmdln + " " + i

    cmdln = strcmdln.split(" ")
    cmdln.remove('')

    cmd = ""
    for j in cmdln:
        cmd = cmd + " " + j

    if (cmdln == [] or
            cmdln[0] == "" or
            cmdln[0] == " " or
            cmd.startswith("#") or
            cmd.startswith("//") or
            (cmd.startswith("/*") and cmd.endswith("*/")) or
            (cmd.startswith("\'\'\'") and cmd.endswith("\'\'\'")) or
            cmd.startswith(";")
    ):
        continue
    else:
        core.system (cmd)