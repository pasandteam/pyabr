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

import sys

from libnam import permissions, files, colors

user = files.readall ("/proc/info/su")
select = files.readall("/proc/info/sel")

if not select.startswith("/proc/"):
    if permissions.check(files.output(select), "w", user):
        files.create(select)
        text = 'Clean the \''+select+"' controller."
        colors.show('', 'ok',text)
    else:
        colors.show("clean", "perm", "")
else:
    files.create(select)