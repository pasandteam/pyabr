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

## Upgrade the clouding system ##

from libnam import control, files, colors, permissions
import shutil,requests
from libabr import core, archive

## Check root ##
if not permissions.check_root (files.readall("/proc/info/su")):
    colors.show ("upgrade","perm","")
    exit(0)

upgrade_mirror = files.readall ('/app/mirrors/update-mirror')

## Check nulls ##
if upgrade_mirror==None or upgrade_mirror=='' or upgrade_mirror==" ":
    colors.show ("upgrade","fail","cannot upgrade system; upgrade mirror record is none.")
    exit()

    ## Back /etc files ##
colors.show("","ok","Create backup files ...")
files.copy ('/etc/deskdirs','/app/backups/deskdirs.bak')
files.copy('/etc/color', '/app/backups/color.bak')
files.copy('/etc/guest', '/app/backups/guest.bak')
files.copy('/etc/gui', '/app/backups/gui.bak')
files.copy('/etc/hostname', '/app/backups/hostname.bak')
files.copy('/etc/interface', '/app/backups/interface.bak')
files.copy('/etc/modules', '/app/backups/modules.bak')
files.copy('/etc/permtab', '/app/backups/permtab.bak')
files.copy('/etc/procmsg', '/app/backups/procmsg.bak')
files.copy('/etc/prompt', '/app/backups/prompt.bak')
files.copy('/etc/time', '/app/backups/time.bak')
files.copy('/etc/users/root', '/app/backups/root.bak')

    ## Get packages ##
colors.show("", "ok", "Get the lates version of Pyabr ...")
## Download the file ##
url = upgrade_mirror
r = requests.get(url, allow_redirects=True)

## Check permissions ##
open(files.input('/tmp/pyabr.zip'), 'wb').write(r.content)

    ## Install Upgrades ##
colors.show("","ok","Install upgrade packages ...")

## Just download ##
shutil.unpack_archive('/tmp/pyabr.tar.xz','/tmp/pyabr','xztar')

    ## Unpack backups ##
colors.show("","ok","Unpack backup files ...")
files.cut ('/app/backups/deskdirs.bak','/etc/deskdirs')
files.cut ('/app/backups/color.bak','/etc/color')
files.cut ('/app/backups/guest.bak','/etc/guest')
files.cut ('/app/backups/gui.bak','/etc/gui')
files.cut ('/app/backups/hostname.bak','/etc/hostname')
files.cut ('/app/backups/interface.bak','/etc/interface')
files.cut ('/app/backups/modules.bak','/etc/modules')
files.cut ('/app/backups/permtab.bak','/etc/permtab')
files.cut ('/app/backups/procmsg.bak','/etc/procmsg')
files.cut ('/app/backups/prompt.bak','/etc/prompt')
files.cut ('/app/backups/time.bak','/etc/time')
files.cut ('/app/backups/root.bak','/etc/users/root')