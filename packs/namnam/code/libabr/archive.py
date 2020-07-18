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

from libnam import files, control, colors, permissions
import shutil

## Zip compresser ##
def zip (src,dest):
    su = files.readall("/proc/info/su") ## Get user data base
    if permissions.check (files.output(src),"r",su): ## Check this user permissions
        if permissions.check (files.output(dest+".zip"),"r",su): ## Check read only permission
            if files.isdir (src): ## Check source dir exists
                if files.isdir (dest+".zip"): ## Check dest dir exists
                    colors.show("libabr.archive.zip", "fail", dest+".zip" + ": dest is a directory.")
                else:
                    shutil.make_archive(files.input(dest),"zip",files.input(src)) ## Create archive
            elif files.isfile (src):
                colors.show("libabr.archive.zip", "fail",src+ ": source is a file.") ## Show error for permissions
            else:
                colors.show("libabr.archive.zip", "fail",src+ ": source not found.")
        else:
            colors.show("libabr.archive.zip", "perm", "")
    else:
        colors.show ("libabr.archive.zip","perm","")

## Tarball compresser ##
def tarball (src,dest):
    su = files.readall("/proc/info/su")
    if permissions.check (files.output(src),"r",su):
        if permissions.check (files.output(dest+".tar"),"r",su):
            if files.isdir (src):
                if files.isdir (dest+".tar"):
                    colors.show("libabr.archive.tarball", "fail", dest+".tar" + ": dest is a directory.")
                else:
                    shutil.make_archive(files.input(dest),"tar",files.input(src))
            elif files.isfile (src):
                colors.show("libabr.archive.tarball", "fail",src+ ": source is a file.")
            else:
                colors.show("libabr.archive.tarball", "fail",src+ ": source not found.")
        else:
            colors.show("libabr.archive.tarball", "perm", "")
    else:
        colors.show ("libabr.archive.tarball","perm","")


## XZip compresser ##
def xzip(src, dest):
    su = files.readall("/proc/info/su")
    if permissions.check(files.output(src), "r", su):
        if permissions.check(files.output(dest + ".xz"), "r", su):
            if files.isdir(src):
                if files.isdir(dest + ".xz"):
                    colors.show("libabr.archive.xzip", "fail", dest + ".xz" + ": dest is a directory.")
                else:
                    shutil.make_archive(files.input(dest), "xz", files.input(src))
            elif files.isfile(src):
                colors.show("libabr.archive.xzip", "fail", src + ": source is a file.")
            else:
                colors.show("libabr.archive.xzip", "fail", src + ": source not found.")
        else:
            colors.show("libabr.archive.xzip", "perm", "")
    else:
        colors.show("libabr.archive.xzip", "perm", "")

## GZip compresser ##
def gzip(src, dest):
    su = files.readall("/proc/info/su")
    if permissions.check(files.output(src), "r", su):
        if permissions.check(files.output(dest + ".gz"), "r", su):
            if files.isdir(src):
                if files.isdir(dest + ".gz"):
                    colors.show("libabr.archive.xzip", "fail", dest + ".gz" + ": dest is a directory.")
                else:
                    shutil.make_archive(files.input(dest), "gz", files.input(src))
            elif files.isfile(src):
                colors.show("libabr.archive.gzip", "fail", src + ": source is a file.")
            else:
                colors.show("libabr.archive.gzip", "fail", src + ": source not found.")
        else:
            colors.show("libabr.archive.gzip", "perm", "")
    else:
        colors.show("libabr.archive.gzip", "perm", "")

