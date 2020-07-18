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
from libabr import core
import shutil, requests
import sys, shutil, os
from libnam import files, permissions, colors

## Clean the cache ##
def clean():
    if permissions.check_root(files.readall ("/proc/info/su")):
        if files.isdir ("/app/cache"):
            files.removedirs ("/app/cache")
            files.mkdir("/app/cache")
            files.mkdir("/app/cache/gets")
            files.mkdir("/app/cache/archives")
            files.mkdir("/app/cache/archives/code")
            files.mkdir("/app/cache/archives/control")
            files.mkdir("/app/cache/archives/data")
            files.mkdir("/app/cache/archives/build")
    else:
        colors.show ("libpa.clean","perm","")

## Create .pa archive ##

def build(name):
    if permissions.check_root(files.readall ("/proc/info/su")):
        if not files.isfile (name+"/control/manifest"):
            colors.show ("libpa.build","fail","cannot create archive package")
            clean()
            sys.exit(0)

        if not files.isdir (name+"/data"): files.mkdir(name+"/data")
        if not files.isdir (name+"/code"): files.mkdir(name + "/code")

        ## Remove cache archives ##
        if files.isdir ('/app/cache/archives/code'): files.removedirs ('/app/cache/archives/code')
        if files.isdir('/app/cache/archives/control'): files.removedirs('/app/cache/archives/control')
        if files.isdir('/app/cache/archives/data'): files.removedirs('/app/cache/archives/data')

        ## Copy dir ##
        files.copydir (name+'/data','/app/cache/archives/data')
        files.copydir(name + '/code', '/app/cache/archives/code')
        files.copydir(name + '/control', '/app/cache/archives/control')

        ## Compile codes ##
        if files.isfile("/app/cache/archives/control/compile"):
            listcodes = control.read_list("/app/cache/archives/control/compile")
            for i in listcodes:
                i = i.split(":")
                files.compile("/app/cache/archives/code/" + i[0], "/app/cache/archives/data/" + i[1])

        ## Pack archives ##
        shutil.make_archive(files.input("/app/cache/archives/build/data"), "xztar", files.input('/app/cache/archives/data'))
        shutil.make_archive(files.input("/app/cache/archives/build/control"), "xztar", files.input('/app/cache/archives/control'))
        shutil.make_archive(files.input(name),"zip",files.input("/app/cache/archives/build"))

        files.cut (name+".zip",name+".pa")
        ## Unlock the cache ##
    else:
        colors.show ("libpa.build","perm","")

## Unpack .pa archives ##

def unpack (name):
    if permissions.check_root(files.readall("/proc/info/su")):
        ## unpack package ##
        shutil.unpack_archive(files.input(name),files.input("/app/cache/archives/build"),"zip")

        shutil.unpack_archive(files.input("/app/cache/archives/build/data.tar.xz"),files.input("/app/cache/archives/data"),"xztar")
        shutil.unpack_archive(files.input("/app/cache/archives/build/control.tar.xz"), files.input("/app/cache/archives/control"), "xztar")

        ## Get database of this package ##
        name = control.read_record("name", "/app/cache/archives/control/manifest").lower()
        unpack = control.read_record("unpack", "/app/cache/archives/control/manifest")
        depends = control.read_record("depends","/app/cache/archives/control/manifest")

        if not (depends==None):
            depends.split(",")

        ## Search for tree dependency ##

        if not depends==None:
            for i in depends:
                if not files.isfile("/app/packages/" + i + ".manifest"):
                    core.system ('paye -i '+name)

        ## Write dependency ##

        if not depends == None:
            for i in depends:
                files.create("/app/packages/" + i + ".depends")
                files.write("/app/packages/" + i + ".depends", name + "\n")

        ## Run preinstall script ##

        if files.isfile ('/app/cache/archives/control/preinstall.py'):
            files.compile ('/app/cache/archives/control/preinstall.py','/usr/bin/preinstall.pyc')
            core.system ('preinstall') # Run it
            files.remove ('/usr/bin/preinstall.pyc')

            ## Copy preinstall script ##

            files.copy ('/app/cache/archives/control/preinstall.py','/app/packages/'+name+".preinstall")

        ## Setting up ##

        if files.isfile ("/app/cache/archives/control/list"): files.copy("/app/cache/archives/control/list","/app/packages/"+name+".list")
        if files.isfile ("/app/cache/archives/control/manifest"): files.copy("/app/cache/archives/control/manifest","/app/packages/"+name + ".manifest")

        ## Unpack data again ##
        shutil.unpack_archive(files.input("/app/cache/archives/build/data.tar.xz"),files.input(unpack),"xztar")

        ## After install ##

        ## Run postinstall script ##

        if files.isfile('/app/cache/archives/control/postinstall.py'):
            files.compile('/app/cache/archives/control/postinstall.py','/usr/bin/postinstall.pyc')
            core.system('postinstall')  # Run it
            files.remove ('/usr/bin/postinstall.pyc')

            ## Copy preinstall script ##

            files.copy('/app/cache/archives/control/postinstall.py', '/app/packages/' + name + ".postinstall")

        ## Copy other scripts ##
        if files.isfile('/app/cache/archives/control/preremove.py'):
            files.copy ('/app/cache/archives/control/preremove.py','/app/packages/'+name+".preremove")

        if files.isfile('/app/cache/archives/control/postremove.py'):
            files.copy ('/app/cache/archives/control/postremove.py','/app/packages/'+name+".postremove")

        ## Unlock the cache ##
    else:
        colors.show("libpa.unpack", "perm", "")

## Remove package ##
def remove (name):
    if permissions.check_root(files.readall("/proc/info/su")):

        location = "/app/packages/" + name.lower() + ".manifest"

        if not files.isfile(location):
            colors.show("libpa.remove", "fail", name + ": package not found")
            clean()
            sys.exit(0)

        ## Database control ##

        list = "/app/packages/" + name.lower() + ".list"
        preinstall = "/app/packages/"+name.lower()+".preinstall"
        postinstall = "/app/packages/"+name.lower()+".postinstall"
        preremove = "/app/packages/"+name.lower()+".preremove"
        postremove = "/app/packages/"+name.lower()+".postremove"
        compile = "/app/packages/"+name.lower()+".compile"
        depends = "/app/packages/"+name.lower()+".depends"


        ## Create preremove and postremove copies ##

        if files.isfile(preremove): files.copy(preremove,"/app/cache/archives/control/preremove.py")
        if files.isfile(postremove): files.copy(postremove, "/app/cache/archives/control/postremove.py")

        ## Run pre remove script ##

        if files.isfile("/app/cache/archives/control/preremove.py"):
            files.compile("/app/cache/archives/control/preremove.py",'/usr/bin/preremove.pyc')
            core.system("preremove")
            files.remove('/usr/bin/preremove.pyc')

        ## Remove depends ##

        if files.isfile(depends):
            depends = control.read_list(depends)
            for i in depends:
                remove(i)

        ####################

        unpack = control.read_record("unpack",location)

        ## Unpacked removal ##
        filelist = control.read_list(list)

        for i in filelist:
            if files.isdir (unpack+"/"+i):
                files.removedirs(unpack + "/" + i)
            elif files.isfile (unpack+"/"+i):
                files.remove (unpack+"/"+i)

        ## Database removal ##

        if files.isfile (location): files.remove (location)
        if files.isfile(compile): files.remove(compile)
        if files.isfile(list): files.remove(list)
        if files.isfile(preinstall): files.remove(preinstall)
        if files.isfile(postinstall): files.remove(postinstall)
        if files.isfile(preremove): files.remove(preremove)
        if files.isfile(postremove): files.remove(postremove)
        if files.isfile (depends): files.remove(depends)

        ## Remove source code ##
        if files.isdir ('/usr/src/'+name): files.removedirs('/usr/src/'+name)

        ## Run postremove script ##

        if files.isfile("/app/cache/archives/control/postremove.py"):
            files.compile ('/app/cache/archives/control/postremove.py','/usr/bin/postremove.pyc')
            core.system("postremove")
            files.remove('/usr/bin/postremove.pyc')

    else:
        colors.show ("libpa.remove","perm","")

## Download package ##
def download (packname):
    if permissions.check_root(files.readall("/proc/info/su")):
        mirror = files.readall ('/app/mirrors/'+packname.lower())

        ## Download the file ##
        url = mirror
        r = requests.get(url, allow_redirects=True)

        ## Check permissions ##
        open(files.input('/app/cache/gets/'+packname.lower()+'.pa'), 'wb').write(r.content)

        ## Remove temporary ##
        files.remove ('/app/cache/gets/'+packname+'.pa')
    else:
        colors.show ("libpa.download","perm","")

## Create a mirro ##
def add_mirror (name,mirror):
    if permissions.check_root(files.readall("/proc/info/su")):
        files.write ('/app/mirrors/'+name,mirror)
    else:
        colors.show ("libpa.add_mirror","perm","")

## Remove a mirror ##
def remove_mirror (name):
    if permissions.check_root(files.readall("/proc/info/su")):
        files.remove ('/app/mirrors/'+name)
    else:
        colors.show ("libpa.remove_mirror","perm","")