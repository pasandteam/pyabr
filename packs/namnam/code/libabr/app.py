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

from libnam import process, files, permissions, colors, control, modules
import os, importlib, getpass, sys
from libabr import core


lang = control.read_record('locale','/etc/gui')

## Graphical application library ##

## Start ID Process ##
def start (id):

    ## Check exists ##
    if files.isfile ('/proc/id/'+id):
        pass

    colors.show (id,'ok-start','')

    ## Create id ##
    files.create ("/proc/id/"+id)


    ## Check desktop shortcut ##
    if files.isfile ("/usr/share/applications/"+id):
        files.copy ("/usr/share/applications/"+id+".desk","/proc/id/"+id) # Copy all informations about this GUI application

    ## Set default id ##
    files.write ("/proc/info/id",id)


## Check id ##
def check(id):
    if not files.isfile ('/proc/id/'+id):
        return False
    else:
        return True

## End id ##
def end (id):

    if files.isfile ('/proc/id/'+id):
        ## Remove id ##
        colors.show(id,'ok-end','')
        files.remove ("/proc/id/"+id)

## Shut id ##
def shut ():
    default = files.readall("/proc/info/id")
    if files.isfile ("/proc/id/"+default):
        end(default)

## Endall id ##
def endall():
    files.remove('/proc/id/desktop')
    colors.show('desktop','ok-endid','')
    colors.show('kernel',"poweroff","")
    listid = files.list ("/proc/id")
    for i in listid:
        if files.isfile('/proc/id/'+i):
            files.remove('/proc/id/'+i)

## Switch id process ##
def switch (id):
    if files.isfile ('/proc/id/'+id):
        colors.show (id,'ok-id','')
        files.write ("/proc/info/id",id)