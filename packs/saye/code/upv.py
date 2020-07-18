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

## import modules ##
import sys
from libnam import permissions, files,control ,colors

## entry ##

## Check root ##
if not permissions.check_root (files.readall("/proc/info/su")):
    colors.show ("upv","perm","")
    sys.exit(0)

sel = files.readall ('/proc/info/sel') ## Get selector

## List all controls ##

listc = control.read_list (sel)

for i in listc:
    if not i.__contains__(':'): pass
    else:
        spliter = i.split (': ')
        files.write ('/proc/info/'+spliter[0],spliter[1])