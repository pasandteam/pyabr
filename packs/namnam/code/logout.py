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

import sys, os, hashlib, subprocess as sub
from libnam import files, control, permissions, colors, process

def logout():
    colors.show('', 'ok','Logging out from all users ...')
    if files.isfile("/proc/selected"): files.remove("/proc/selected")
    process.endall()
    sub.call (['./'+files.readall("/proc/info/boot"),'login'])

logout()