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
import sys, os, hashlib, getpass
from libnam import files, control, permissions, colors

def uadd (input_username,user):
    if permissions.check_root(user):
        ## Check exists user ##
        if files.isfile("/etc/users/" + input_username) or input_username == "root":
            colors.show("uadd", "fail", input_username + ": user exists.")
        elif input_username == "guest":
            colors.show("uadd", "fail", "cannot create user account with guest username.")
        else:
            while True:
                password = getpass.getpass ('Enter a new password: ')
                confirm = getpass.getpass ('Confirm the new password: ')
                if password==confirm:break

            ## Informations ##
            first_name =        input ('\tEnter your first name []: ')
            last_name =         input ('\tEnter your last name []: ')
            company =           input ('\tEnter your company name []: ')
            birthday =          input ('\tEnter your birthday []: ')
            gender =            input ('\tChoose your gender [Male/Female/Other]: ')
            blood_type =        input ('\tChoose your blood type [O/A/B/AB]: ')
            phone =             input ('\tEnter your phone number []: ')
            website =           input ('\tEnter your website address []: ')
            email =             input ('\tEnter your email address []: ')

            hashname = hashlib.sha3_256(str(input_username).encode()).hexdigest()
            hashcode = hashlib.sha3_512(str(password).encode()).hexdigest()

            files.create ("/etc/users/"+input_username)
            control.write_record ("username",hashname,'/etc/users/'+input_username)
            control.write_record ("code",hashcode,'/etc/users/'+input_username)

            ## Add informations ##
            if not (first_name == None or first_name == ""):
                control.write_record("first_name", first_name, '/etc/users/' + input_username)
            if not (last_name == None or last_name == ""):
                control.write_record("last_name", last_name, '/etc/users/' + input_username)
            if not (company == None or company == ""):
                control.write_record ("company",company,'/etc/users/'+input_username)
            if not (birthday == None or birthday == ""):
                control.write_record("birthday", birthday, '/etc/users/' + input_username)
            if not (gender == None or gender == ""):
                control.write_record("gender", gender, '/etc/users/' + input_username)
            if not (blood_type == None or blood_type == ""):
                control.write_record("blood_type", blood_type, '/etc/users/' + input_username)
            if not (phone == None or phone == ""):
                control.write_record("phone", phone, '/etc/users/' + input_username)
            if not (website == None or website == ""):
                control.write_record("website", website, '/etc/users/' + input_username)
            if not (email == None or email == ""):
                control.write_record ("email",email,'/etc/users/'+input_username)

            permissions.create ("/desk/"+input_username,7,1,0,input_username) ## Create permission for another user

            colors.show('', 'ok', "Add '" + input_username + "' user account.")
    else:
        colors.show ("uadd","perm","")

if not sys.argv[1:] == []:
    uadd(sys.argv[1],files.readall ("/proc/info/su"))
else:
    colors.show("uadd", "fail", "no inputs.")