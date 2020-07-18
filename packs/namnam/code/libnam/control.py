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

from libnam import files, permissions


def read_record (name,filename):
    strv = files.readall(filename)
    strv = strv.split("\n")

    for i in strv:
        if i.startswith(name):
            i = i.split(": ")
            if i[0]==(name):
                return i[1]

def read_list (filename):
    strv = files.readall(filename)
    strv = strv.split("\n")
    return strv

def write_record (name,value,filename):
    all = files.readall(filename)
    record = read_record(name, filename)
    files.remove(filename)
    if not (record == None):
        all = all.replace(name + ": " + record, "")
    files.write(filename, all + "\n" + name + ": " + value)

def remove_record (name,filename):
    all = files.readall(filename)
    record = read_record(name, filename)
    files.remove(filename)
    if not (record == None):
        all = all.replace(name + ": " + record, "")
    files.write(filename, all)

def remove_item (name,filename):
    items = read_list(filename)
    strv = ""
    for i in items:
        if i == name:
            strv = strv + "\n"
        else:
            strv = strv + "\n" + i
    files.write(filename,strv)