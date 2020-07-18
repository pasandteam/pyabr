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

def shut ():
    colors.show('', 'ok', 'Closing the switched process ...')
    if files.isfile("/proc/selected"): files.remove("/proc/selected")
    process.end (int(files.readall ("/proc/info/sp")))

    if files.readall("/proc/info/su") == "0":
        if files.isdir("/desk/guest"):
            files.removedirs("/desk/guest")
        if files.isdir("/tmp"):
            files.removedirs("/tmp")
            files.mkdir("/tmp")
        if files.isfile("/proc/selected"): files.remove("/proc/selected")
        process.endall()

shut()