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

from libnam import files, control, colors
import sys

## Processor of kernel ##
def processor ():
    j = 0
    if not files.isfile ("/proc/"+str(0)):
        files.create ("/proc/"+str(0))
        j = j + 1
    else:
        list = files.list ("/proc")
        list.remove ('id')
        list.remove ('info')

        for i in list:
            if files.isfile ("/proc/"+i):

                files.create("/proc/" + str(int(i)+1))
                j = j + 1
            else:
                files.create ("/proc/"+i)

    if files.isfile ("/proc/1"):
        files.write ("/proc/info/sp",str(j))
        return j
    else:
        files.write("/proc/info/sp", str(j-1))
        return j-1

## Check switched process ##
def check (switch):
    if not files.isfile ("/proc/"+str(switch)):
        colors.show ("/proc/"+str(switch),"ok-endswitch","")
        colors.show ("","poweroff","")
        sys.exit(0)
    else:
        if files.isfile ("/proc/info/sp"): files.remove ("/proc/info/sp")
        files.write ("/proc/info/sp",str(switch))

## End switched process ##
def end (switch):
    if files.isfile("/proc/info/sp"): files.remove("/proc/info/sp")
    if files.isfile("/proc/" + str(switch)):
        files.remove("/proc/" + str(switch))
        sys.exit(0)

## Endall all switched processes ##
def endall ():
    if files.isfile("/proc/info/sp"): files.remove("/proc/info/sp")
    list = files.list ("/proc")
    list.remove ("id")
    list.remove ("info")
    for i in list:
        files.remove("/proc/" + str(i))