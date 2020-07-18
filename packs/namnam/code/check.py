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

def check (filename):
    perm = permissions.get_permissions(files.output(filename))
    numperm = permissions.show_number(perm)
    r = permissions.check (files.output(filename), "r", files.readall("/proc/info/su"))
    w = permissions.check (files.output(filename), "w",  files.readall("/proc/info/su"))
    x = permissions.check (files.output(filename), "x",  files.readall("/proc/info/su"))

    bold = colors.color(1, colors.get_bgcolor(), colors.get_fgcolor())

    print    ("   Seleted path: "+bold+files.output(filename) + colors.get_colors())
    print    ("     Permission: "+bold+perm + colors.get_colors())
    print    (" Permission Num: "+bold+str(numperm) + colors.get_colors())
    if r==True:
        print("           Read: " + bold +colors.get_ok()+ "Yes" + colors.get_colors())
    else:
        print("           Read: " + bold +colors.get_fail()+ "No" + colors.get_colors())

    if w==True:
        print("          Write: " + bold +colors.get_ok()+ "Yes" + colors.get_colors())
    else:
        print("          Write: " + bold +colors.get_fail()+ "No" + colors.get_colors())

    if x==True:
        print("        Execute: " + bold +colors.get_ok()+ "Yes" + colors.get_colors())
    else:
        print("        Execute: " + bold +colors.get_fail()+ "No" + colors.get_colors())


if not sys.argv[1:]==[]:
    check(sys.argv[1])
else:
    colors.show("check", "fail", "no inputs.")