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

def chown (new_owner,name):
    permowner = permissions.check_owner (files.output(name),files.readall ("/proc/info/su"))
    perm = permissions.get_permissions(files.output(name))

    num = permissions.show_number(perm)
    num = str(num)
    user_p = int(num[0])
    others_p = int(num[1])
    guest_p = int(num[2])

    if permowner==True:
        if new_owner=="":
            permissions.create(files.output(name),user_p,others_p,guest_p,files.readall ("/proc/info/su"))
        else:
            permissions.create(files.output(name), user_p, others_p, guest_p, new_owner)
    else:
        colors.show("chown", "perm", "")


if sys.argv[1:] == []:
    colors.show("chown", "fail", "no inputs.")
else:
    if sys.argv[2:] == []:
        chown("", sys.argv[1])
        colors.show('', 'ok',
                    'Change owership of \'' + sys.argv[1] + '\' to ' +  files.readall("/proc/info/su") +'.')
    else:
        chown(sys.argv[1], sys.argv[2])
        colors.show('', 'ok',
                    'Change owership of \'' + sys.argv[1] + '\' to ' + sys.argv[2] + '.')