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
from libnam import files, control, permissions, colors
import sys

def uinfo (input_username):
    enable_cli = control.read_record("enable_cli", "/etc/guest")
    if not (input_username=="guest" and enable_cli=="Yes"):
        if files.isfile ("/etc/users/"+input_username):
            ## Get information from user database ##
            first_name = control.read_record("first_name", "/etc/users/" + input_username)
            last_name = control.read_record("last_name", "/etc/users/" + input_username)
            company = control.read_record("company", "/etc/users/" + input_username)
            birthday = control.read_record("birthday", "/etc/users/" + input_username)
            gender = control.read_record("gender", "/etc/users/" + input_username)
            blood_type = control.read_record("blood_type", "/etc/users/" + input_username)
            phone = control.read_record("phone", "/etc/users/" + input_username)
            website = control.read_record("website", "/etc/users/" + input_username)
            email = control.read_record("email", "/etc/users/" + input_username)

            ## Show it on screen ##
            bold = colors.color(1, colors.get_bgcolor(), colors.get_fgcolor())
            if not (first_name == None or first_name == ""):  print(
                "\t   First name: " + bold + first_name + colors.get_colors())
            if not (last_name == None or last_name == ""):    print(
                "\t    Last name: " + bold + last_name + colors.get_colors())
            if not (company == None or company == ""):        print(
                "\t      Company: " + bold + company + colors.get_colors())
            if not (birthday == None or birthday == ""):      print(
                "\t     Birthday: " + bold + birthday + colors.get_colors())
            if not (gender == None or gender == ""):          print(
                "\t       Gender: " + bold + gender + colors.get_colors())
            if not (blood_type == None or blood_type == ""):  print(
                "\t    BloodType: " + bold + blood_type + colors.get_colors())
            if not (phone == None or phone == ""):            print(
                "\t Phone number: " + bold + phone + colors.get_colors())
            if not (website == None or website == ""):        print(
                "\t      Website: " + bold + website + colors.get_colors())
            if not (email == None or email == ""):            print(
                "\tEmail address: " + bold + email + colors.get_colors())
        else:
            colors.show ("uinfo","fail",input_username+": user not found.")

if sys.argv[1:]==[]:
    uinfo (files.readall ("/proc/info/su"))
else:
    uinfo (sys.argv[1])