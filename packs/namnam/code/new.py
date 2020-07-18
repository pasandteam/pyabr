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

boot = files.readall("/proc/info/boot")

def new (user,code):
    colors.show('', 'ok', 'Switching a new process ...')
    if files.isfile("/proc/selected"): files.remove("/proc/selected")
    if user=="guest":
        sub.call(['./'+boot,'user','guest'])
    else:
        sub.call(['./'+boot,'user',user,code])

new (control.read_record ("username","/tmp/su.tmp"),control.read_record ("code","/tmp/su.tmp"))
if files.isfile ("/tmp/su.tmp"): files.remove ("/tmp/su.tmp")