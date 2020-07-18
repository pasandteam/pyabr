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

import sys
from libnam import files

def help(helpfile):
    if helpfile=="":
        print (files.readall("/usr/share/helps/cmdall.txt"))
    else:
        if files.isfile ("/usr/share/helps/commands/"+helpfile+".txt"):
            print (files.readall("/usr/share/helps/commands/"+helpfile+".txt"))
        else:
            print(files.readall("/usr/share/helps/cmdall.txt"))

if sys.argv[1:]==[]:
    help("")
else:
    help(sys.argv[1])

