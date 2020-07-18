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

def chmod (mod,filename):
    perm_user = int(mod[0])
    perm_others = int(mod[1])
    perm_guest = int(mod[2])
    if permissions.check_owner (files.output(filename),files.readall("/proc/info/su")):
        owner = permissions.get_owner (files.output(filename))
        permissions.create (files.output(filename),perm_user,perm_others,perm_guest,owner)
        colors.show ('','ok','Change mode of \''+filename+'\' to '+mod+'.')
    else:
        colors.show ("chmod","perm","")

if sys.argv[1:] == []:
    colors.show("chmod", "fail", "no inputs.")
else:
    if sys.argv[2:] == []:
        colors.show("chmod", "fail", "no inputs.")
    else:
        chmod(sys.argv[1], sys.argv[2])