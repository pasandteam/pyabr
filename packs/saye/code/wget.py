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
import sys, shutil, os, requests
from libnam import files, permissions, colors

# https://www.tutorialspoint.com/downloading-files-from-web-using-python

## Check params ##

if sys.argv[1:]==[] and sys.argv[2:]: colors.show('wget','fail','no inputs.')

## Download ##

colors.show ('','ok','Download \''+sys.argv[2]+"\' from ("+sys.argv[1]+") ...")
url = sys.argv[1]
r = requests.get(url, allow_redirects=True)

## Check permissions ##
if permissions.check(files.output(sys.argv[2]), "w", files.readall("/proc/info/su")):
    open(files.input(sys.argv[2]), 'wb').write(r.content)
else:
    colors.show("wget", "perm", "")