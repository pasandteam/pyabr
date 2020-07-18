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

import shutil, os, sys

os.system ("\""+sys.executable+"\" pre-build.py")

shutil.unpack_archive('wheel/setup.zip','wheel/setup','zip') # Unpack setup wheel package

## Copy all files and dirs in wheel/setup/src ##

shutil.copyfile('setup.ui','wheel/src/setup.ui')
shutil.copyfile('setup.svg','wheel/src/setup.svg')
shutil.copyfile('setup.py','wheel/src/setup.py')
shutil.copyfile('setup.png','wheel/src/setup.png')
shutil.copyfile('run.py','wheel/src/run.py')
shutil.copyfile('README.md','wheel/setup/README.md')
shutil.copyfile('README.md','wheel/src/README.md')
shutil.copyfile('pre-build.py','wheel/src/pre-build.py')
shutil.copyfile('pack-wheel.py','wheel/src/pack-wheel.py')
shutil.copyfile('LICENSE','wheel/src/LICENSE')
shutil.copyfile('LICENSE','wheel/setup/LICENSE')
shutil.copyfile('debug.py','wheel/src/debug.py')
shutil.copyfile('build.py','wheel/src/build.py')
shutil.copytree('packs','wheel/src/packs')
shutil.copytree('buildlibs','wheel/src/buildlibs')
shutil.copyfile('wheel/setup-pack.py','wheel/setup/setup.py')
shutil.copyfile('wheel/setup-installer.py','wheel/setup/pyabr/setup.py')

file = open ("wheel/setup/pyabr/__main__.py","w");file.write('from pyabr import setup');file.close()

## Pack src to setup ##
shutil.make_archive('wheel/setup/pyabr/pyabr','zip','wheel/src')

## Build wheel package and save it to build-packs ##

os.system ("cd wheel/setup && \""+sys.executable+"\" setup.py bdist_wheel")