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
import sys, os, time
from libnam import colors

if sys.argv[1:]==[]:
    colors.show('', 'ok', "Wait about 3 seconds ...")
    time.sleep(3)
else:
    timeout = float(sys.argv[1])
    colors.show('', 'ok', "Wait about "+str(timeout)+" seconds ...")
    time.sleep(int(timeout))
