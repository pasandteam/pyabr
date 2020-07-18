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

root = "./"

import os, shutil, sys, py_compile

def input (filename):
    if filename.startswith("/"):
        return root + filename
    else:
        pwd = readall("/proc/info/pwd")
        return root + pwd + "/" + filename

def output_shell (filename):
    return input(filename).replace("///", "/").replace("//", "/").replace("./", "/")

def input_exec (filename):
    return input(filename.replace("./","")).replace(".//","").replace("/",".")

def output (filename):
    if filename.startswith("/"):
        return filename
    else:
        return input(filename).replace("///", "/").replace("//", "/").replace("./", "/").replace("//","/")

def create (filename):
    file = open (input(filename),"w")
    file.close()

def readall (filename):
    file = open (input(filename),"r")
    strv = file.read()
    file.close()
    return strv

def write (filename,text):
    file = open(input(filename), "w")
    file.write(text)
    file.close()

def append (filename,text):
    file = open(input(filename), "a")
    file.write(text)
    file.close()

def isfile (filename):
    if os.path.isfile(input(filename)):
        return True
    else:
        return False

def isdir (dirname):
    if os.path.isdir(input(dirname)):
        return True
    else:
        return False

def mkdir (dirname):
    os.mkdir(input(dirname))

def makedirs (dirname):
    os.makedirs(input(dirname))

def remove (filename):
    os.remove(input(filename))

def rmdir (dirname):
    os.rmdir(input(dirname))

def removedirs (dirname):
    shutil.rmtree (input(dirname))

def copy (src,dest):
    shutil.copyfile (input(src),input(dest))

def cut (src,dest):
    copy (src,dest)
    remove(src)

def copydir (src,dest):
    shutil.copytree(input(src),input(dest))

def cutdir (src,dest):
    copydir(input(src),input(dest))
    removedirs(src)

def list (path):
    return os.listdir(input(path))

def parentdir (filename):
    file = input(filename) ## Get file name

    file = file.split ('/')
    file.pop (len(file)-1)

    strv = ''
    for i in file:
        strv+=i

    return strv

def filename (path):
    file = input(path)  ## Get file name

    file = file.split('/')

    return file[len(file)-1]
