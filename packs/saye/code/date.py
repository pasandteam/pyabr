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

# https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python

import datetime as d
import sys, pytz ,os, time
from libnam import files

## Show all time and date ##
if sys.argv[1:]==[]:
    os.environ['TZ'] = files.readall("/proc/info/tz") # https://stackoverflow.com/questions/1301493/setting-timezone-in-python
    time.tzset()
    print(d.datetime.now().ctime())

## Show utc now ##
if sys.argv[1:]==['utc']:
    print(d.datetime.utcnow().ctime())