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

import sys, importlib
from importlib import reload
from libnam import files, colors

## Get modules from /etc/modules ##
def get_modules():
    file = open("etc/modules")
    strv = file.read()
    file.close()
    strv = strv.split("\n")
    for i in strv:
        sys.path.append("./"+i)

## Import module ##
def run_module (module):
    ## split ##
    m = module.split ('/')
    m.pop (0)

    strv = ''

    for i in m:
        strv+=i

    print (strv)
    print (m)

    importlib.import_module(strv)