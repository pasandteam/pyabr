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

import site, shutil, os, sys

#print(site.getusersitepackages()) # https://stackoverflow.com/questions/122327/how-do-i-find-the-location-of-my-python-site-packages-directory

s = site.getusersitepackages()
shutil.copyfile(s+"/pyabr/pyabr.zip","pyabr.zip")
shutil.unpack_archive("pyabr.zip","pyabr-install","zip")
os.system("cd pyabr-install && \""+sys.executable+"\" setup.py")
shutil.rmtree("pyabr-install")
os.remove("pyabr.zip")
