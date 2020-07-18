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

from libnam import control, files

argv = 'kernel'

black = 30
red = 31
green = 32
yellow = 33
blue = 34
purple = 35
cyan = 36
white = 37

style_none = 0
style_bold = 1
style_underline = 2
style_negative1 = 3
style_negative2 = 5

bg_black = 40
bg_red = 41
bg_green = 42
bg_yellow = 43
bg_blue = 44
bg_purple = 45
bg_cyan = 46
bg_white = 47

kernel = control.read_record("kernel","/etc/procmsg")
gui = control.read_record("gui","/etc/procmsg")
gui_login = control.read_record("gui-login","/etc/procmsg")
gui_user = control.read_record("gui-user","/etc/procmsg")
login = control.read_record("login","/etc/procmsg")
user = control.read_record("user","/etc/procmsg")
exec = control.read_record("exec","/etc/procmsg")
client = control.read_record("client","/etc/procmsg")

def show (process_name,process_type,process_message):
    if process_type=="fail":
            print (get_fail()+process_name+": error: "+process_message+get_colors())
    elif process_type=="ok":
        ok = control.read_record('ok','/etc/procmsg')
        if ok=='Yes':
            print(get_ok() + process_message + get_colors())
    elif process_type=="perm":
            print(get_fail()+process_name+": error: " + "Permission denied." + get_colors())
    elif process_type=="upgrade":
            repo = control.read_record('upgrade-mirror','/etc/repo')
            print(get_ok() + "Upgrade: "+get_colors()+" to lates version from ("+repo+") ...")
    elif process_type=="warning":
            print (get_warning()+process_name+": warning: "+process_message+get_colors())
    elif process_type=="ok-start":
            if (
                (argv=='kernel' and kernel=="Yes") or
                (argv == 'gui' and gui == "Yes") or
                (argv == 'gui-login' and gui_login == "Yes") or
                (argv == 'gui-user' and gui_user == "Yes") or
                (argv == 'login' and login == "Yes") or
                (argv == 'user' and user == "Yes") or
                (argv == 'exec' and exec == "Yes")
        ):
                print ("[ "+get_ok()+" OK "+get_colors()+" ] Start "+process_name+" process.")
    elif process_type=="ok-end":
            if (
                    (argv == 'kernel' and kernel == "Yes") or
                    (argv == 'gui' and gui == "Yes") or
                    (argv == 'gui-login' and gui_login == "Yes") or
                    (argv == 'gui-user' and gui_user == "Yes") or
                    (argv == 'login' and login == "Yes") or
                    (argv == 'user' and user == "Yes") or
                    (argv == 'exec' and exec == "Yes")
            ):
                print ("[ "+get_ok()+" OK "+get_colors()+" ] End "+process_name+" process.")
    elif process_type=="ok-switch":
            if (
                    (argv == 'kernel' and kernel == "Yes") or
                    (argv == 'gui' and gui == "Yes") or
                    (argv == 'gui-login' and gui_login == "Yes") or
                    (argv == 'gui-user' and gui_user == "Yes") or
                    (argv == 'login' and login == "Yes") or
                    (argv == 'user' and user == "Yes") or
                    (argv == 'exec' and exec == "Yes")
            ):
                print ("[ "+get_ok()+" OK "+get_colors()+" ] Switch "+process_name+" process.")
    elif process_type=="ok-endswitch":
            if (
                    (argv == 'kernel' and kernel == "Yes") or
                    (argv == 'gui' and gui == "Yes") or
                    (argv == 'gui-login' and gui_login == "Yes") or
                    (argv == 'gui-user' and gui_user == "Yes") or
                    (argv == 'login' and login == "Yes") or
                    (argv == 'user' and user == "Yes") or
                    (argv == 'exec' and exec == "Yes")
            ):
                print ("[ "+get_ok()+" OK "+get_colors()+" ] End "+process_name+" switched process.")
    elif process_type=="ok-id":
            if (
                    (argv == 'kernel' and kernel == "Yes") or
                    (argv == 'gui' and gui == "Yes") or
                    (argv == 'gui-login' and gui_login == "Yes") or
                    (argv == 'gui-user' and gui_user == "Yes") or
                    (argv == 'login' and login == "Yes") or
                    (argv == 'user' and user == "Yes") or
                    (argv == 'exec' and exec == "Yes")
            ):
                print ("[ "+get_ok()+" OK "+get_colors()+" ] Switch ID "+process_name+" process.")
    elif process_type=="ok-endid":
            if (
                    (argv == 'kernel' and kernel == "Yes") or
                    (argv == 'gui' and gui == "Yes") or
                    (argv == 'gui-login' and gui_login == "Yes") or
                    (argv == 'gui-user' and gui_user == "Yes") or
                    (argv == 'login' and login == "Yes") or
                    (argv == 'user' and user == "Yes") or
                    (argv == 'exec' and exec == "Yes")
            ):
                print ("[ "+get_ok()+" OK "+get_colors()+" ] End "+process_name+" ID process.")
    elif process_type=="fail-start":
            print ("[ "+get_fail()+"FAIL "+get_colors()+"] Fail to start "+process_name+" process.")
    elif process_type=="fail-switch":
            print ("[ "+get_fail()+"FAIL "+get_colors()+"] Fail to switch "+process_name+" process.")
    elif process_type=="stop":
            print ("[ "+get_fail()+"STOP"+get_colors()+" ] Stop the "+process_name)
    elif process_type=="ok-show":
            print("[ " + get_ok() + " OK " + get_colors() + " ] "+process_message)
    elif process_type=="fail-show":
            print ("[ "+get_fail()+"FAIL"+get_colors()+" ] "+process_message)
    elif process_type=="poweron":
            if (
                    (argv == 'kernel' and kernel == "Yes") or
                    (argv == 'gui' and gui == "Yes") or
                    (argv == 'gui-login' and gui_login == "Yes") or
                    (argv == 'gui-user' and gui_user == "Yes") or
                    (argv == 'login' and login == "Yes") or
                    (argv == 'user' and user == "Yes") or
                    (argv == 'exec' and exec == "Yes")
            ):
                print ("[ "+get_ok()+" OK "+get_colors()+" ] Power on the "+process_name)
    elif process_type=="poweroff":
            if (
                    (argv == 'kernel' and kernel == "Yes") or
                    (argv == 'gui' and gui == "Yes") or
                    (argv == 'gui-login' and gui_login == "Yes") or
                    (argv == 'gui-user' and gui_user == "Yes") or
                    (argv == 'login' and login == "Yes") or
                    (argv == 'user' and user == "Yes") or
                    (argv == 'exec' and exec == "Yes")
            ):
                print ("[ "+get_ok()+" OK "+get_colors()+" ] Power off the "+process_name)
    elif process_type=="reboot":
            print ("[ "+get_ok()+" OK "+get_colors()+" ] Restart the "+process_name)

def color (style,text,background):
    if not files.isfile("/proc/id/desktop"):
        return "\033["+str(style)+";"+str(text)+";"+str(background)+"m"
    else:
        return ""

def get_colors ():

    if not files.isfile("/proc/id/desktop"):
        fgcolor = control.read_record("fgcolor", "/etc/color")
        bgcolor = control.read_record("bgcolor", "/etc/color")
        style = control.read_record("style", "/etc/color")
        strv = "\033[" + str(style) + ";" + str(fgcolor) + ";" + str(bgcolor) + "m"
        return strv
    else:
        return ""

def get_style ():

    if not files.isfile("/proc/id/desktop"):
        style = control.read_record("style", "/etc/color")
        return style
    else:
        return ""

def get_fgcolor ():

    if not files.isfile("/proc/id/desktop"):
        fgcolor = control.read_record("fgcolor", "/etc/color")
        return fgcolor
    else:
        return ""

def get_bgcolor ():

    if not files.isfile("/proc/id/desktop"):
        bgcolor = control.read_record("bgcolor", "/etc/color")
        return bgcolor
    else:
        return ""

def get_warning():

    if not files.isfile("/proc/id/desktop"):
        style = control.read_record("warning_style", "/etc/color")
        fgcolor = control.read_record("warning_fgcolor", "/etc/color")
        bgcolor = control.read_record("warning_bgcolor", "/etc/color")
        strv = "\033[" + str(style) + ";" + str(fgcolor) + ";" + str(bgcolor) + "m"
        return strv
    else:
        return ""

def get_path():

    if not files.isfile("/proc/id/desktop"):
        style = control.read_record("path_style", "/etc/color")
        fgcolor = control.read_record("path_fgcolor", "/etc/color")
        bgcolor = control.read_record("path_bgcolor", "/etc/color")
        strv = "\033[" + str(style) + ";" + str(fgcolor) + ";" + str(bgcolor) + "m"
        return strv
    else:
        return ""

def get_prompt():

    if not files.isfile("/proc/id/desktop"):
        style = control.read_record("prompt_style", "/etc/color")
        fgcolor = control.read_record("prompt_fgcolor", "/etc/color")
        bgcolor = control.read_record("prompt_bgcolor", "/etc/color")
        strv = "\033[" + str(style) + ";" + str(fgcolor) + ";" + str(bgcolor) + "m"
        return strv
    else:
        return ""

def get_fail():

    if not files.isfile("/proc/id/desktop"):
        style = control.read_record("fail_style", "/etc/color")
        fgcolor = control.read_record("fail_fgcolor", "/etc/color")
        bgcolor = control.read_record("fail_bgcolor", "/etc/color")
        strv = "\033[" + str(style) + ";" + str(fgcolor) + ";" + str(bgcolor) + "m"
        return strv
    else:
        return ""

def get_ok():

    if not files.isfile("/proc/id/desktop"):
        style = control.read_record("ok_style", "/etc/color")
        fgcolor = control.read_record("ok_fgcolor", "/etc/color")
        bgcolor = control.read_record("ok_bgcolor", "/etc/color")
        strv = "\033[" + str(style) + ";" + str(fgcolor) + ";" + str(bgcolor) + "m"
        return strv
    else:
        return ""

def get_hide():

    if not files.isfile("/proc/id/desktop"):
        style = control.read_record("style", "/etc/color")
        bgcolor = control.read_record("bgcolor", "/etc/color")
        fgcolor = int(control.read_record("bgcolor", "/etc/color")) + 10
        strv = "\033[" + str(style) + ";" + str(fgcolor) + ";" + str(bgcolor) + "m"
        return strv
    else:
        return ""