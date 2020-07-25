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

from buildlibs import pack_archives as pack
from buildlibs import control
import shutil, os, sys


#os.system('cd core && pyinstaller --onefile --noconfirm vmnam.py --hidden-import requests');shutil.copyfile('core/dist/vmnam','stor/vmnam')
'''
pack.build ("namnam")
pack.build ("baran")
pack.build ("paye")
pack.build ("saye")

pack.unpack ("namnam")
pack.unpack ("baran")
pack.unpack ("paye")
pack.unpack ("saye")
'''

pack.build ("baran")
pack.unpack('baran')