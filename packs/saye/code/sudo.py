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
import os,sys, subprocess,hashlib

from libnam import permissions, control,files, colors

if sys.argv[1:]==[]:
    colors.show ('sudo','fail','no inputs.')
    sys.exit()

if not sys.argv[1].startswith('-'):

    ## Get user name ##

    thisuser = files.readall("/proc/info/su")

    ## Check guest account ##
    if thisuser == "guest":
        colors.show("sudo", 'fail', 'cannot use sudo command in guest user.')
        sys.exit(0)

    ## Check sudoers account ##
    if not thisuser == "root":
        sudoers = files.readall('/etc/sudoers')

        if not sudoers.__contains__(thisuser):
            colors.show('sudo', 'fail', thisuser + ": user is'nt sudoers account.")
            sys.exit()

    ## Send /etc/users/root to /proc/info/su username ##

    files.write("/proc/info/su", 'root')

    prompt = ['./'+files.readall('/proc/info/boot'), 'exec']

    for i in sys.argv[1:]:
        prompt.append(i)

    subprocess.call(prompt)

    files.write("/proc/info/su", thisuser)
elif sys.argv[1]=='-a':
    ## Check root ##
    if not permissions.check_root(files.readall("/proc/info/su")):
        colors.show("sudo", "perm", "")
        sys.exit(0)
    ## Check user exists or no ##
    if files.isfile ('/etc/users/'+sys.argv[2]):
        hashname = hashlib.sha3_256(sys.argv[2].encode()).hexdigest()
        username = control.read_record ('username','/etc/users/'+sys.argv[2])

        if hashname==username:
            files.append ('/etc/sudoers',sys.argv[2]+"\n")
            colors.show ('','ok','Add \''+sys.argv[2]+'\' user account in sudoers.')
        else:
            colors.show('sudo', 'fail', sys.argv[2] + ": user not found.")
    else:
        colors.show('sudo', 'fail', sys.argv[2] + ": user not found.")
else:
    colors.show ('sudo','fail',sys.argv[1]+": option not found.")