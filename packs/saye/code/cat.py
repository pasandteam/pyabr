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

import sys, os, hashlib
from libnam import files, control, permissions, colors, process


def cat (name,option):

    ## Read files ##
    if option=='' or option=='-r':
        if files.isfile(name):
            if permissions.check(files.output(name), "r", files.readall("/proc/info/su")):
                file = open(files.input(name), "rb")
                check_bin = str(file.read())
                file.close()
                if check_bin.__contains__("\\x00"):
                    print(check_bin)
                else:
                    print(files.readall(name))
            else:
                colors.show("cat", "perm", "")
        elif files.isdir(name):
            colors.show("cat", "fail", name + ": is a directory.")
        else:
            colors.show("cat", "fail", name + ": file not found.")

    ## Create files ##
    elif option=='-c':
        if files.isdir (name):
            colors.show("cat", "fail", name + ": is a directory.")
        else:
            if permissions.check(files.output(name), "w", files.readall("/proc/info/su")):
                files.create (name)
            else:
                colors.show("cat", "perm", "")

    ## Write into files ##
    elif option=='-w':
        if files.isdir (name):
            colors.show("cat", "fail", name + ": is a directory.")
        else:
            if permissions.check(files.output(name), "w", files.readall("/proc/info/su")):

                ## Set EOF
                if cmdln[3:]==[]:
                    EOF = 'EOF'
                else:
                    EOF = cmdln[3]

                # WRITE COMMAND LINE

                texts = ''

                while True:
                    cmd = input('> ')
                    if cmd==EOF: break
                    else:
                        if texts == '':
                            texts = cmd
                        else:
                            texts = texts + '\n' + cmd

                ## WRITE INTO FILE
                files.write (cmdln[2],texts)
            else:
                colors.show("cat", "perm", "")

    ## Write into files ##
    elif option == '-a':
        if files.isdir(name):
            colors.show("cat", "fail", name + ": is a directory.")
        else:
            if permissions.check(files.output(name), "w", files.readall("/proc/info/su")):

                ## Set EOF
                if cmdln[3] == []:
                    EOF = 'EOF'
                else:
                    EOF = cmdln[3]

                # WRITE COMMAND LINE

                texts = ''

                while True:
                    cmd = input('> ')
                    if cmd == EOF:
                        break
                    else:
                        if texts == '':
                            texts = cmd
                        else:
                            texts = texts + '\n' + cmd

                ## WRITE INTO FILE
                files.append(cmdln[2], texts)
            else:
                colors.show("cat", "perm", "")

cmdln = ['']
cmdln[1:] = sys.argv[1:]

if not cmdln[1:]==[]:
    if cmdln[1]=='-r' or cmdln[1]=='-c' or cmdln[1]=='-w' or cmdln[1]=='-a':
        cat (cmdln[2],cmdln[1])
    else:
        cat (cmdln[1],'')
else:
    colors.show("cat", "fail", "no inputs.")