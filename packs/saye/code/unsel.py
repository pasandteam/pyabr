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

def unsel ():
    select = files.readall("/proc/info/sel")
    if select == "/proc/"+files.readall("/proc/info/sp"):
        colors.show ("unsel","warning","controller has already selected.")
    else:
        files.write("/proc/info/sel", "/proc/"+files.readall("/proc/info/sp"))
        if files.isfile ("/proc/selected"): files.remove("/proc/selected")
        colors.show('', 'ok', 'Select the switched process as a controller.')

unsel()