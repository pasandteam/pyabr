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

def get (filename):
    model = control.read_record("model", "/etc/gui")  # read model

    if not filename == None:
        filename = filename.split("/")  # @widget:barge

        share = filename[0]
        name = filename[1]

        ## Real Resource ##
        if share.startswith("@widget"):
            if files.isfile("/usr/share/" + share.replace("@widget", "widgets")  + "/" + name + ".ui"):
                return files.input(
                    "/usr/share/" + share.replace("@widget", "widgets") + "/" + name + ".ui")
            else:
                return None

        elif share.startswith("@font"):
            if files.isfile ("/usr/share/fonts/"+name+".ttf"):
                return "/usr/share/fonts/"+name+".ttf"
            else:
                return None

        elif share.startswith("@background"):
            if files.isfile("/usr/share/backgrounds/" + name + ".svg"):
                return files.input(
                    "/usr/share/backgrounds/" + name + ".svg")
            elif files.isfile(
                    "/usr/share/backgrounds/" + name + ".png"):
                return files.input(
                    "/usr/share/backgrounds/" + name + ".png")
            elif files.isfile(
                    "/usr/share/backgrounds/" + name + ".jpg"):
                return files.input(
                    "/usr/share/backgrounds/" + name + ".jpg")
            elif files.isfile(
                    "/usr/share/backgrounds/" + name + ".jpeg"):
                return files.input(
                    "/usr/share/backgrounds/" + name + ".jpeg")
            elif files.isfile(
                    "/usr/share/backgrounds/" + name + ".gif"):
                return files.input(
                    "/usr/share/backgrounds/" + name + ".gif")
            else:
                return None

        elif share.startswith("@image"):
            if files.isfile("/usr/share/images/" + name + ".svg"):
                return files.input(
                    "/usr/share/images/"+ name + ".svg")
            elif files.isfile(
                    "/usr/share/images/" + name + ".png"):
                return files.input(
                    "/usr/share/images/"  + name + ".png")
            elif files.isfile(
                    "/usr/share/images/" + name + ".jpg"):
                return files.input(
                    "/usr/share/images/" + name + ".jpg")
            elif files.isfile(
                    "/usr/share/images/" + name + ".jpeg"):
                return files.input(
                    "/usr/share/images/" + name + ".jpeg")
            elif files.isfile(
                    "/usr/share/images/"  + name + ".gif"):
                return files.input(
                    "/usr/share/images/"  + name + ".gif")
            else:
                return None

        elif share.startswith("@app"):
            if files.isfile("/usr/share/" + share.replace("@app", "applications") + "/" + name + ".desk"):
                return files.input("/usr/share/" + share.replace("@app", "applications") + "/" + name + ".desk")
            else:
                return None

        elif share.startswith("@icon"):
            if files.isfile("/usr/share/" + share.replace("@icon", "icons") + "/" + name + ".svg"):
                return files.input("/usr/share/" + share.replace("@icon", "icons") + "/" + name + ".svg")
            elif files.isfile("/usr/share/" + share.replace("@icon", "icons") + "/" + name + ".png"):
                return files.input("/usr/share/" + share.replace("@icon", "icons") + "/" + name + ".png")
            elif files.isfile("/usr/share/" + share.replace("@icon", "icons") + "/" + name + ".gif"):
                return files.input("/usr/share/" + share.replace("@icon", "icons") + "/" + name + ".gif")
            else:
                return None

        elif share.startswith("@string"):
            locale = control.read_record("locale", "/etc/gui")
            id = files.readall("/proc/info/id")

            ## Set default lang ##
            if locale == None: locale = "en"

            ## Get value from string ##
            result =  control.read_record(id.replace(".desk","")+"."+name, "/usr/share/locales/" + locale + ".locale")

            ## Find default ##
            if result==None:
                result = control.read_record(id.replace(".desk","")+"."+name, "/usr/share/locales/" + 'en' + ".locale")

            return result

        ## None Resource ##
        else:
            return None
    else:
        return None