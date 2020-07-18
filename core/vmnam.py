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

# In the name of God, the Compassionte, the Merciful
# pyabr NamNam kernel (wet) written in Python
# Virtual Memory NamNam Kernel (vmnam)
# (c) 2020 Mani Jamali All rights reserved.

import sys, socket, platform, hashlib, os, getpass, subprocess as sub, cpuinfo, importlib
from psutil import virtual_memory
## @variables ##

hostname = ""
distro_name = ""
distro_code = ""
distro_version = ""
distro_build = ""
ip = ""
arch = ""
os_user = ""
osname = ""
kernel_name = "NamNam"
kernel_version = "0.1.2"
user = ""
code = ""
argv = sys.argv[1:] # kernel parameters
kernel_file = "vmnam"
select = ""
tz = ""
cpu = ''
cpuc = ''
ram = ''

## Configure kernel ###############################################################################


################## Module configure ##########################

sys.path.append("usr/app")

from libnam import modules, files, control, colors, process, permissions
from libabr import core

################## Interface configure ##########################

modules.get_modules()
## @core/interface ##

if argv == []:
    interface = files.readall ("/etc/interface").upper()

    if interface.startswith("CLI"):
        argv = ['kernel']
    elif interface.startswith("GUI"):
        argv = ['gui']
    else:
        colors.show("interface", "fail-start", "")
        colors.show("kernel", "stop", "")
        sys.exit(0)

## @core/params-check ##

if not (argv[0] == "kernel" or
    argv[0] == "gui" or
    argv[0] == "user" or
    argv[0] == "login" or
    argv[0] == "gui-user" or
    argv[0] == "gui-login" or
    argv[0] == "exec" ):
    colors.show("params-check", "fail-start", "")
    colors.show("kernel", "stop", "")
    sys.exit(0)
else:
    if argv[0]=='kernel' or argv[0]=='gui':
        if files.isfile ("/proc/0"):
            colors.show("params-check", "fail-start", "")
            colors.show("kernel", "stop", "")
            sys.exit(0)

colors.argv = argv[0] ## Set color argv

## @core/exec ##

if argv[0]=='exec':
    user = files.readall("/proc/info/su")

    if (argv[1:] == [] or
            argv[1] == "" or
            argv[1] == " " or
            argv[1].startswith(";")
    ):
        print(end='')
    elif argv[1].__contains__("/"):
        if files.isfile(argv[1]+".so"):
            if permissions.check(files.output(argv[1])+".so", "x", user):
                ## Set args ##
                sys.argv = argv[1:]

                appname = argv[1]

                sys.path.append(files.parentdir (appname))
                __import__(files.filename(appname))
                sys.path.remove (files.parentdir (appname))
            else:
                colors.show(argv[1], "perm", "")
        elif files.isfile(argv[1]):
            if permissions.check(files.output(argv[1]), "x", user):
                ## command ##
                command = [files.input(argv[1])]

                for i in argv[2:]:
                    command.append(i)

                sub.call(command)
            else:
                colors.show(argv[1], "perm", "")
        elif files.isfile(argv[1]+'.sa'):
            if permissions.check(files.output(argv[1])+'.sa', "x", user):
                strv = ''
                for i in argv[1:]:
                    strv+=i
                core.system ('saye '+strv)
            else:
                colors.show(argv[1], "perm", "")
        else:
            colors.show(argv[1], "fail", "command not found.")
    else:
        ## Library execute in path ##
        if files.isfile("/usr/app/"+argv[1]+".so"):
            if permissions.check("/usr/app/"+files.output(argv[1])+".so", "x", user):
                ## Set args ##
                sys.argv = argv[1:]

                __import__(argv[1])
            else:
                colors.show(argv[1], "perm", "")
        elif files.isfile ('/usr/app/'+argv[1]):
            if permissions.check("/usr/app/" + files.output(argv[1]), "x", user):
                ## command ##
                command = [files.input ('/usr/app/'+argv[1])]

                for i in argv[2:]:
                    command.append(i)

                sub.call(command)
            else:
                colors.show(argv[1], "perm", "")
        elif files.isfile('/usr/app/'+argv[1]+'.sa'):
            if permissions.check('/usr/app/'+files.output(argv[1])+'.sa', "x", user):
                strv = ''
                for i in argv[1:]:
                    strv+=i
                core.system ('saye '+strv)
            else:
                colors.show(argv[1], "perm", "")
        else:
            colors.show(argv[1], "fail", "command not found.")
    sys.exit()

###################################################################################

colors.show ("kernel","poweron","")

################## Switch configure ##########################

switch = process.processor() # Switch the process
process.check (switch) # Check the switched process

if switch == None:
    switch = 0

files.write("/proc/info/sel","/proc/"+str(switch))
select = files.readall("/proc/info/sel")

colors.show ("/proc/"+str(switch),"ok-switch","")

####################################################################################################

## @core/hostname ##

if files.isfile("/etc/hostname"):
    files.copy("/etc/hostname", "/proc/info/host")
    hostname = files.readall("/etc/hostname")
    colors.show("hostname", "ok-start", "")
else:
    colors.show("hostname", "fail-start", "")
    colors.show("kernel", "stop", "")
    sys.exit(0)


## @core/distro ##

if files.isfile("/etc/distro"):
    distro_name = control.read_record("name", "/etc/distro")
    distro_code = control.read_record("code", "/etc/distro")
    distro_version = control.read_record("version", "/etc/distro")
    distro_build = control.read_record("build", "/etc/distro")
    files.write("/proc/info/cs", distro_name)
    files.write("/proc/info/cd", distro_code)
    files.write("/proc/info/ver", distro_version)
    files.write("/proc/info/bl", distro_build)
    colors.show("distro", "ok-start", "")
else:
    colors.show("distro", "fail-start", "")
    colors.show("kernel", "stop", "")
    sys.exit(0)

## @core/kernel-info ##

if not (argv[0]=='user' or argv[0]=='login'):
    colors.show("kernel-info", "ok-start", "")
    files.write("/proc/info/kname", kernel_name)
    files.write("/proc/info/kver", kernel_version)

## @core/system-info ##

    colors.show("system-info", "ok-start", "")
    ip = socket.gethostbyname(socket.gethostname())
    osname = platform.system()
    arch = platform.architecture()[0]
    os_user = platform.node()
    tz = control.read_record("format", "/etc/time")
    sweek = control.read_record("start-week", "/etc/time")
    cpu = str(cpuinfo.get_cpu_info()['brand_raw'])  # Create by darkwlf: https://github.com/darkwlf
    cpuc = str(os.cpu_count())  # Create by darkwlf: https://github.com/darkwlf
    ram = str(virtual_memory().total)  # Create by darkwlf: https://github.com/darkwlf

    if argv[0] == "kernel":
        interface = "CLI"
    else:
        interface = "GUI"

    files.write("/proc/info/ip", ip)
    files.write("/proc/info/os", osname)
    files.write("/proc/info/arch", arch)
    files.write("/proc/info/os_su", os_user)
    files.write("/proc/info/inter", interface)
    files.write("/proc/info/tz", tz)
    files.write("/proc/info/sweek", sweek)
    files.write("/proc/info/boot", kernel_file)
    files.write("/proc/info/cpu", cpu)
    files.write("/proc/info/cpuc", cpuc)
    files.write("/proc/info/ram", ram)

## @core/dirs ##

colors.show("dirs", "ok-start", "")
fhs = control.read_list ("/etc/fhs")
for i in fhs:
    if not files.isdir (i) and not files.isfile (i):
        files.mkdir (i)

## @core/welcome ##

if argv[0]=="kernel":
    colors.show("welcome", "ok-start", "")
    print ()
    print ("Welcome to "+distro_name+" "+distro_version+" ("+distro_code+") clouding system.")
    print()

## @core/issue ##

if (argv[0]=="kernel") and files.isfile ("/etc/issue"):
    colors.show("issue","ok-start","")
    print ()
    print (files.readall("/etc/issue"))
    print ()

## @core/gui ##

if argv[0]=="gui":
    desktop = control.read_record('desktop','/etc/gui')
    if not desktop==None:
        core.system (desktop)
    else:
        colors.show ('gui','fail-start','')
        colors.show ('kernel','stop','')
    sys.exit(0)

## @core/gui-login ##

if argv[0]=="gui-login":
    login = control.read_record('login','/etc/gui')
    if not login==None:
        core.system (login)
    else:
        colors.show ('gui-login','fail-start','')
        colors.show ('kernel','stop','')
    sys.exit(0)

## @core/gui-user ##

if argv[0]=="gui-user":
    user = control.read_record('user','/etc/gui')
    if not user==None:
        if argv[1]=='guest':
            core.system (user + ' ' + argv[1])
        else:
            core.system(user + ' ' + argv[1] + ' ' + argv[2])
    else:
        colors.show ('gui-user','fail-start','')
        colors.show ('kernel','stop','')
    sys.exit(0)

## @lib/shell ##

def shell():
    print()

    if user=="root":
        files.write("/proc/info/pwd","/root")
    else:
        files.write("/proc/info/pwd","/desk/"+user)

    select = files.readall ("/proc/info/sel")  # Change selected database

    while True:
        if not files.isfile ("/proc/selected"):
            files.write("/proc/info/sel", "/proc/" + str(switch))  ## Write this controller
        ## Check the switched process ##
        process.check(switch)  # Check the switched process

        files.write("/proc/info/sp", str(switch))  # Write switched process

        if files.isfile ("/tmp/su.tmp"): files.remove ("/tmp/su.tmp")

        ## User configure check ##
        files.write("/proc/info/su",user) # Write user name in info processor
        if not user=="guest":
            hashname = hashlib.sha3_256(str(user).encode()).hexdigest()
            username = control.read_record("username","/etc/users/"+user)
            hashcode = hashlib.sha3_512(str(code).encode()).hexdigest()
            password = control.read_record("code","/etc/users/"+user)

            if not (hostname==username) and not (password==hashcode):
                colors.show("shell","fail-start","")
                colors.show("kernel","stop","")
                sys.exit(0)
        ## PWD path setting up at all ##
        if not user == "root":
            if not files.isdir("/desk/" + user): files.mkdir("/desk/" + user)  # Create home folder

        ## Prompt data base ##

        show_username = control.read_record("show_username", "/etc/prompt")
        show_hostname = control.read_record("show_hostname", "/etc/prompt")
        show_path = control.read_record("show_path", "/etc/prompt")
        root_symbol = control.read_record("root","/etc/prompt")
        user_symbol = control.read_record("user", "/etc/prompt")

        ## Setting up prompt data base 2 ##

        color_uh = ""
        color_path = ""
        prompt_symbol = ""

        if user=="root":
            prompt_symbol = root_symbol
            color_uh = colors.get_colors()
            color_path = colors.get_colors()
        else:
            prompt_symbol = user_symbol
            color_uh = colors.get_ok()
            color_path = colors.get_path()

        ## Setting up space of prompt ##

        if show_username == "Yes":
            space_username = user
        else:
            space_username = ""

        if show_hostname == "Yes":
            space_hostname = hostname
        else:
            space_hostname = ""

        if show_path == "Yes":
            space_path = files.readall("/proc/info/pwd")
        else:
            space_path = ""

        if show_hostname == "Yes" and show_username == "Yes":
            space1 = "@"
        else:
            space1 = ""

        if (show_hostname == "Yes" or show_username == "Yes") and show_path == "Yes":
            space2 = ":"
        else:
            space2 = ""

        ## Shell prompt ##

        cmd = input(color_uh + space_username + space1 + space_hostname + colors.get_colors() + space2 + color_path + space_path + colors.get_colors() + prompt_symbol + " ")

        cmdln = cmd.split(" ")


        strcmdln = ""

        for i in cmdln:
            if str(i).startswith("$"):
                select = files.readall("/proc/info/sel")
                var = control.read_record(str(i).replace("$",""),select)
                if var==None:
                    strcmdln = strcmdln + " " + i
                else:
                    strcmdln = strcmdln + " " + var
            else:
                strcmdln = strcmdln + " " + i

        ## Command line ##
        cmdln = strcmdln.split(" ")
        cmdln.remove ('')

        ## All commands run in here ##

        ## New command ##
        if cmdln[0]=="new":
            files.create ("/tmp/su.tmp")
            control.write_record ("username",user,"/tmp/su.tmp")
            control.write_record ("code",code,"/tmp/su.tmp")


        ## Other commands ##
        if (cmdln == [] or
                cmdln[0] == "" or
                cmdln[0] == " " or
                cmd.startswith("#") or
                cmd.startswith("//") or
                (cmd.startswith("/*") and cmd.endswith("*/")) or
                (cmd.startswith("\'\'\'") and cmd.endswith("\'\'\'")) or
                cmd.startswith(";")
        ):
            continue
        else:
            ## Run commands ##
           # os.system('./'+kernel_file+" exec "+cmd)# Credit learned with https://pymotw.com/2/subprocess/


            ## Prompt ##
            prompt = [
                './'+kernel_file,
                'exec',
                cmdln[0]
            ]

            ## Arguments ##
            for i in cmdln[1:]:
                prompt.append(i)

            ## Call the kernel ##
            sub.call (prompt)
## @core/user ##

if argv[0]=="user":
    input_username = argv[1]
    if input_username=="guest":
        enable_cli = control.read_record("enable_cli", "/etc/guest")
        if enable_cli == "Yes":
            ## Set variables ##
            user = "guest"
            code = "*"
            ## Create info ##
            files.write("/proc/info/su", input_username)
            shell()
            sys.exit(0)
        else:
            colors.show(input_username, "fail", "user not found.")
    else:
        input_password = argv[2]
        hashname = hashlib.sha3_256(str(input_username).encode()).hexdigest()
        hashcode = hashlib.sha3_512(str(input_password).encode()).hexdigest()

        if files.isfile ("/etc/users/"+input_username):
            username = control.read_record("username","/etc/users/"+input_username)
            password = control.read_record("code","/etc/users/"+input_username)
            if username==hashname and password==hashcode:
                ## Set variables ##
                user = input_username
                code = input_password
                ## Create info ##
                files.write("/proc/info/su", input_username)
                permissions.user = user
                permissions.code = code
                shell()
                sys.exit(0)
            else:
                colors.show("user", "fail-start", "")
                colors.show("kernel", "stop", "")
                sys.exit(0)
        else:
            colors.show ("user","fail-start","")
            colors.show ("kernel","stop","")
            sys.exit(0)

## @core/login ##

if argv[0]=="kernel" or argv[0]=="login":
    colors.show ("login","ok-start","")
    while True:
        print()

        process.check(switch)  # Check the switched process

        input_username = input("Enter an username: ")
        if input_username == "" or input_username == " ":
            continue
        elif input_username == "guest":
            enable_cli = control.read_record("enable_cli", "/etc/guest")
            if enable_cli == "Yes":
                ## Set variables ##
                user = "guest"
                code = "*"
                ## Create info ##
                files.write("/proc/info/su", input_username)
                permissions.user = user
                permissions.code = code
                shell()
                sys.exit(0)
            else:
                colors.show(input_username, "fail", "user not found.")
        elif files.isfile("/etc/users/" + input_username):
            hashname = hashlib.sha3_256(
                str(input_username).encode()).hexdigest()  # Hashname creator from input_username
            username = control.read_record("username", "/etc/users/" + input_username)
            if not hostname == input_username:
                input_password = getpass.getpass("Enter " + input_username + "'s password: ")
                hashcode = hashlib.sha3_512(
                    str(input_password).encode()).hexdigest()  # Hashcode creator from input_password
                password = control.read_record("code", "/etc/users/" + input_username)
                if hashcode == password:
                    ## Set variables ##
                    user = input_username
                    code = input_password
                    ## Create info ##
                    files.write("/proc/info/su", input_username)
                    permissions.user = user
                    permissions.code = code
                    shell()
                    sys.exit(0)
                else:
                    colors.show(input_username, "fail", "wrong password.")
            else:
                colors.show(input_username, "fail", "user not found.")
        else:
            colors.show(input_username, "fail", "user not found.")
