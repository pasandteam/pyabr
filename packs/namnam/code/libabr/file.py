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

from libnam import files, permissions, colors, control

def create (name):
    su = files.readall("/proc/info/su")
    if permissions.check (files.output(name),"w",su):
        if isdir (name):
            colors.show("libabr.file.create", "fail", name + ": is a directory.")
        else:
            files.create (name)
    else:
        colors.show("libabr.file.create", "perm", "")

def write (name,text):
    su = files.readall("/proc/info/su")
    if permissions.check (files.output(name),"w",su):
        if isdir (name):
            colors.show("libabr.file.write", "fail", name + ": is a directory.")
        else:
            files.write (name,text)
    else:
        colors.show("libabr.file.write", "perm", "")

def readall (name):
    su = files.readall("/proc/info/su")
    if permissions.check (files.output(name),"r",su):
        if files.isfile (name):
            file = open(files.input(name), "rb")
            check_bin = str(file.read())
            file.close()
            if check_bin.__contains__("\\x00"):
                return check_bin
            else:
                return files.readall(name)
        else:
            colors.show("libabr.file.readall", "fail", name + ": file not found.")
    else:
        colors.show("libabr.file.readall", "perm", "")
def append (name,text):
    su = files.readall("/proc/info/su")
    if permissions.check (files.output(name),"w",su):
        if isdir (name):
            colors.show("libabr.file.append", "fail", name + ": is a directory.")
        else:
            files.append (name,text)
    else:
        colors.show("libabr.file.append", "perm", "")

def isfile (name):
    su = files.readall("/proc/info/su")
    if permissions.check (files.output(name),"r",su):
        return files.isfile (name)
    else:
        colors.show("libabr.file.isfile", "perm", "")
        return None

def isdir (name):
    su = files.readall("/proc/info/su")
    if permissions.check (files.output(name),"r",su):
        return files.isdir (name)
    else:
        colors.show("libabr.file.isdir", "perm", "")
        return None

def mkdir (name):
    su = files.readall("/proc/info/su")
    if permissions.check(files.output(name), "w", su):
        if isfile (name):
            colors.show("libabr.file.mkdir", "fail", name + ": is a file.")
        else:
            files.makedirs(name)
    else:
        colors.show("libabr.file.mkdir", "perm", "")

def remove (name):
    su = files.readall("/proc/info/su")
    if permissions.check(files.output(name), "w", su):
        if isfile (name):
            files.remove (name)
        elif isdir (name):
            files.removedirs (name)
        else:
            colors.show ("libabr.file.remove","fail",name+": file or directory not found.")
    else:
        colors.show("libabr.file.remove", "perm", "")

def copy (src,dest):
    su = files.readall("/proc/info/su")
    if permissions.check(files.output(src), "r", su):
        if isfile (src):
            if permissions.check(files.output(dest), "w", su):
                if files.isdir (dest):
                    colors.show("libabr.file.copy", "fail", dest + ": dest is a directory.")
                else:
                    perm = permissions.get_permissions(files.output(src))
                    control.write_record(files.output(dest), perm, "/etc/permtab")
                    files.copy (src,dest)
            else:
                colors.show("libabr.file.copy", "perm", "")
        elif isdir (src):
            if permissions.check(files.output(dest), "w", su):
                if files.isfile(dest):
                    colors.show("libabr.file.copy", "fail", dest + ": dest is a file.")
                else:
                    perm = permissions.get_permissions(files.output(src))
                    control.write_record(files.output(dest), perm, "/etc/permtab")
                    files.copydir(src, dest)
            else:
                colors.show("libabr.file.copy", "perm", "")
        else:
            colors.show ("libabr.file.copy","fail",src+": source not found.")
    else:
        colors.show("libabr.file.copy", "perm", "")

def cut (src,dest):
    su = files.readall("/proc/info/su")
    if permissions.check(files.output(src), "r", su) and  permissions.check(files.output(src), "w", su):
        if isfile (src):
            if permissions.check(files.output(dest), "w", su):
                if files.isdir (dest):
                    colors.show("libabr.file.cut", "fail", dest + ": dest is a directory.")
                else:
                    perm = permissions.get_permissions(files.output(src))
                    control.write_record(files.output(dest), perm, "/etc/permtab")
                    files.cut (src,dest)
            else:
                colors.show("libabr.file.cut", "perm", "")
        elif isdir (src):
            if permissions.check(files.output(dest), "w", su):
                if files.isfile(dest):
                    colors.show("libabr.file.cut", "fail", dest + ": dest is a file.")
                else:
                    perm = permissions.get_permissions(files.output(src))
                    control.write_record(files.output(dest), perm, "/etc/permtab")
                    files.cutdir(src, dest)
            else:
                colors.show("libabr.file.cut", "perm", "")
        else:
            colors.show ("libabr.file.cut","fail",src+": source not found.")
    else:
        colors.show("libabr.file.cut", "perm", "")

def list (name):
    su = files.readall("/proc/info/su")
    if permissions.check(files.output(name), "r", su):
        return files.list (name)
    else:
        colors.show("libabr.file.list", "perm", "")
        return []

def compile (src,dest):
    su = files.readall("/proc/info/su")
    if permissions.check(files.output(src), "r", su):
        if isfile (src):
            if permissions.check(files.output(dest), "w", su):
                if files.isdir (dest):
                    colors.show("libabr.file.compile", "fail", dest + ": dest is a directory.")
                else:
                    files.compile (src,dest)
            else:
                colors.show("libabr.file.compile", "perm", "")
        elif isdir (src):
            colors.show("libabr.file.compile", "fail", src + ": source is a directory.")
        else:
            colors.show ("libabr.file.compile","fail",src+": source not found.")
    else:
        colors.show("libabr.file.compile", "perm", "")