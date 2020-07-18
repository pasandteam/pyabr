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

def ver():
    bold = colors.color(1, colors.get_bgcolor(), colors.get_fgcolor())

    print("        Static hostname: " + bold + files.readall ("/proc/info/host") + colors.get_colors())
    print("        Clouding System: " + bold + files.readall ("/proc/info/cs") + " " + files.readall ("/proc/info/ver") + " (" + files.readall ("/proc/info/cd") + ")" + colors.get_colors())
    print("             Build date: " + bold + files.readall ("/proc/info/bl") + colors.get_colors())
    print("       Operating System: " + bold + files.readall ("/proc/info/os") + colors.get_colors())
    print("                 Kernel: " + bold + files.readall ("/proc/info/kname") + " " + files.readall ("/proc/info/kver") + colors.get_colors())
    print("          Switched User: " + bold + files.readall ("/proc/info/su") + colors.get_colors())
    print("       Switched Process: " + bold + files.readall ("/proc/info/sp") + colors.get_colors())
    print("           Architecture: " + bold + files.readall ("/proc/info/arch") + colors.get_colors())

ver()