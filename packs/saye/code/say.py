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

for i in sys.argv[1:]:
    print(
        i
            .replace("-a", "\a")
            .replace("-b", "\b")
            .replace("-f", "\f")
            .replace("-n", "\n")
            .replace("-r", "\r")
            .replace("-t", "\t")
            .replace("-v", "\v"),end=' ')