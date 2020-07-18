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

def reboot():
    colors.show('', 'ok', 'Rebooting the clouding system ...')
    if files.isfile("/proc/selected"): files.remove("/proc/selected")
    colors.show("kernel", "reboot", "")
    if files.isdir("/desk/guest"):
        files.removedirs("/desk/guest")
    if files.isdir ("/tmp"):
        files.removedirs("/tmp")
        files.mkdir ("/tmp")
    process.endall()
    sub.call(['./'+files.readall("/proc/info/boot")])

reboot()