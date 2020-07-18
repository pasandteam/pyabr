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

from libnam import files, control

import hashlib

user = ""

## Create permissions ##
def create (name,user,others,guest,owner):
    if files.isfile (name) or files.isdir (name):
        ## Learned by Guru99 2020 ##
        ## Set user permissions section
        if user==0:
            user = "---"
        elif user==1:
            user = "--x"
        elif user==2:
            user = "-w-"
        elif user==3:
            user = "-wx"
        elif user==4:
            user = "r--"
        elif user==5:
            user = "r-x"
        elif user==6:
            user = "rw-"
        elif user==7:
            user = "rwx"
        else:
            user = "rwx"

        ## Set other users permissions section
        if others == 0:
            others = "---"
        elif others == 1:
            others = "--x"
        elif others == 2:
            others = "-w-"
        elif others == 3:
            others = "-wx"
        elif others == 4:
            others = "r--"
        elif others == 5:
            others = "r-x"
        elif others == 6:
            others = "rw-"
        elif others == 7:
            others = "rwx"
        else:
            others = "rwx"

        ## Set guest user permissions section
        if guest == 0:
            guest = "---"
        elif guest == 1:
            guest = "--x"
        elif guest == 2:
            guest = "-w-"
        elif guest == 3:
            guest = "-wx"
        elif guest == 4:
            guest = "r--"
        elif guest == 5:
            guest = "r-x"
        elif guest == 6:
            guest = "rw-"
        elif guest == 7:
            guest = "rwx"
        else:
            guest = "rwx"

        if files.isdir (name):
            control.write_record (name,"d"+user+others+guest+"/"+owner,"/etc/permtab") # Write permissions for this directory
        else:
            control.write_record(name, "-"+user + others + guest + "/" + owner,"/etc/permtab")  # Write permissions for this file

def exists (name):
    perms = control.read_record(name, "/etc/permtab")  ## get permissions
    if perms==None:
        return False
    else:
        return True

## This function e.g. drwxrwxrwx/root --> 777 ##
def show_number (perm):
    perm = perm.split("/")
    owner = perm[1]
    perms = perm[0]

    dirfile = perms[0]
    user_r = perms[1]
    user_w = perms[2]
    user_x = perms[3]
    others_r = perms[4]
    others_w = perms[5]
    others_x = perms[6]
    guest_r = perms[7]
    guest_w = perms[8]
    guest_x = perms[9]

    user = user_r+user_w+user_x
    others = others_r+others_w+others_x
    guest = guest_r+guest_w+guest_x

    if user=='---':
        user = 0
    elif user=='--x':
        user = 1
    elif user=='-w-':
        user = 2
    elif user=='-wx':
        user = 3
    elif user=='r--':
        user = 4
    elif user=='r-x':
        user = 5
    elif user=='rw-':
        user = 6
    elif user=='rwx':
        user = 7

    if others=='---':
        others = 0
    elif others=='--x':
        others = 1
    elif others=='-w-':
        others = 2
    elif others=='-wx':
        others = 3
    elif others=='r--':
        others = 4
    elif others=='r-x':
        others = 5
    elif others=='rw-':
        others = 6
    elif others=='rwx':
        others = 7

    if guest=='---':
        guest = 0
    elif guest=='--x':
        guest = 1
    elif guest=='-w-':
        guest = 2
    elif guest=='-wx':
        guest = 3
    elif guest=='r--':
        guest = 4
    elif guest=='r-x':
        guest = 5
    elif guest=='rw-':
        guest = 6
    elif guest=='rwx':
        guest = 7


    strnum = str(user)+str(others)+str(guest) # e.g. 7, 7, 7 --> "777"
    num = int (strnum) # e.g. "777"-> 777

    return num

## This function correct at all ##
def get_permissions (name):
    perms = control.read_record(name, "/etc/permtab")  ## get permissions
    if not perms==None:
        return perms
    else:
        ## Father permtab ##
        if files.isdir (name):
            dirfile = "d"
        else:
            dirfile = "-"

        ## The most important part of father permtab ##
        names = name.split("/")

        while not exists(name):
            l = len (names) -1
            names.pop(l)
            name = ""
            for i in names:
                name = name +"/"+i
            name = name.replace("//","/")

        perm = control.read_record(name, "/etc/permtab")  ## get permissions
        perm = perm.split("/")
        owner = perm[1]
        perms = perm[0]
        user_r = perms[1]
        user_w = perms[2]
        user_x = perms[3]
        others_r = perms[4]
        others_w = perms[5]
        others_x = perms[6]
        guest_r = perms[7]
        guest_w = perms[8]
        guest_x = perms[9]
        return dirfile + user_r + user_w + user_x + others_r + others_w + others_x + guest_r + guest_w + guest_x + "/" + owner

## This function correct at all ##
def check (name,request,user):
    perm = get_permissions(name)
    perm = perm.split("/")

    perms = perm[0]
    owner = perm[1]

    dirfile = perms[0]
    user_r = perms[1]
    user_w = perms[2]
    user_x = perms[3]
    others_r = perms[4]
    others_w = perms[5]
    others_x = perms[6]
    guest_r = perms[7]
    guest_w = perms[8]
    guest_x = perms[9]

    if user=="root":
        ## Check exists user ##
        if files.isfile("/etc/users/" + user):
            hashname = hashlib.sha3_256(str("root").encode()).hexdigest()
            username = control.read_record("username", "/etc/users/root")
            if (hashname == username):
                return True
            else:
                return False
        else:
            return False
    elif user=="guest":
        enable_cli = control.read_record("enable_cli","/etc/guest")
        if enable_cli=="Yes":
            if owner==user:
                if request == "r":
                    r = user_r
                    if r == "r":
                        return True
                    else:
                        return False
                elif request == "w":
                    w = user_w
                    if w == "w":
                        return True
                    else:
                        return False
                elif request == "x":
                    x = user_x
                    if x == "x":
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                if request == "r":
                    r = guest_r
                    if r == "r":
                        return True
                    else:
                        return False
                elif request == "w":
                    w = guest_w
                    if w == "w":
                        return True
                    else:
                        return False
                elif request == "x":
                    x = guest_x
                    if x == "x":
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False
    else:
        ## Check exists user ##
        if files.isfile ("/etc/users/"+user):
            hashname = hashlib.sha3_256(str(user).encode()).hexdigest()
            username = control.read_record("username","/etc/users/"+user)
            if (hashname==username):
                if owner==user:
                    if request=="r":
                        r = user_r
                        if r=="r":
                            return True
                        else:
                            return False
                    elif request=="w":
                        w = user_w
                        if w=="w":
                            return True
                        else:
                            return False
                    elif request=="x":
                        x = user_x
                        if x=="x":
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    if request == "r":
                        r = others_r
                        if r == "r":
                            return True
                        else:
                            return False
                    elif request == "w":
                        w = others_w
                        if w == "w":
                            return True
                        else:
                            return False
                    elif request == "x":
                        x = others_x
                        if x == "x":
                            return True
                        else:
                            return False
                    else:
                        return False
            else:
                return False
        else:
            return False

## Get owner ##
def get_owner (filename):
    perm = get_permissions(filename)

    perm = perm.split("/")
    return perm[1]

## Check owner ##
def check_owner(filename,user):
    owner = get_owner(filename)
    if user=="guest":
        enable_cli = control.read_record("enable_cli", "/etc/guest")
        if enable_cli == "Yes":
            if owner == user:
                return True
            else:
                return False
        else:
            return False
    elif user=="root":
        if files.isfile ("/etc/users/"+user):
            hashname = hashlib.sha3_256(str(user).encode()).hexdigest()
            username = control.read_record("username","/etc/users/"+user)
            if (hashname == username):
                return True
            else:
                return False
        else:
            return False
    else:
        if files.isfile ("/etc/users/"+user):
            hashname = hashlib.sha3_256(str(user).encode()).hexdigest()
            username = control.read_record("username","/etc/users/"+user)
            if (hashname == username):
                if owner == user:
                    return True
                elif owner=="guest":
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

## Check root ##
def check_root(user):
    if user == "root":
        if files.isfile("/etc/users/" + user):
            hashname = hashlib.sha3_256(str(user).encode()).hexdigest()
            username = control.read_record("username", "/etc/users/" + user)
            if (hashname == username):
                return True
            else:
                return False
        else:
            return False