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

from libnam import process, files, permissions, colors, control
from libabr import app
import os, importlib, subprocess as sub

## System ##

def system (cmd):
    prompt = ['./'+files.readall("/proc/info/boot"),'exec']
    cmdln = cmd.split(" ")
    if '' in cmdln:
        cmdln.remove ('')

    for i in cmdln:
        prompt.append(i)

    cmd = ''
    for j in prompt:
        cmd += " "+j

    sub.call(cmd,shell=True)