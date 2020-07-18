
#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Pasand team. GNU General Pucdic License v3.0
#
#  Offical website:         http://itpasand.com
#  Telegram or Gap channel: @pyabr
#  Telegram or Gap group:   @pyabr_community
#  Git source:              github.com/pasandteam/pyabr
#
#######################################################################################

## Imports ##
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from libnam import colors, control, files, modules, permissions, process
from libabr import app, archive, core, file, res

## Main entry ##
application = QApplication (sys.argv)
## https://www.cdog.pythonlibrary.org/2015/08/18/getting-your-screen-resolution-with-python/ Get screen model ##
screen_resolution = application.desktop().screenGeometry()
width, height = screen_resolution.width(), screen_resolution.height()

## variables ##

class variables:
    backend_color = '#000000'
    backend_timeout = 1000
    splash_color = '#ABCDEF'
    splash_timeout = 3000
    fullscreen = True
    width = width
    height = height
    sides = False
    login_bgcolor = '#FFFFFF'
    login_fgcolor = '#000000'
    login_background = None
    enter_bgcolor = '#FFFFFF'
    enter_fgcolor = '#000000'
    enter_background = None
    username = ''
    password = ''
    desktop_bgcolor = '#123456'
    desktop_fgcolor = '#FFFFFF'

## ## ## ## ##

## Get data ##
def getdata (name):
    return control.read_record (name,'/etc/gui')

## Backend ##
class Backend (QMainWindow):
    ## Run splash page ##
    def runSplash (self):
        self.setCentralWidget(Splash([self]))

    def __init__(self):
        super(Backend, self).__init__()

        ## Get informations ##
        cs = files.readall ('/proc/info/cs')
        ver = files.readall('/proc/info/ver')
        cd = files.readall('/proc/info/cd')

        self.setWindowTitle(cs+' '+ver+' ('+cd+")")

        ## Get app logo ##
        applogo = getdata('logo')
        if not applogo == None:
            self.setWindowIcon(QIcon(res.get(applogo)))

        ## Get backend color ##
        color = getdata('backend.color')

        ## Set color ##
        if not color==None:
            variables.backend_color = color

        self.setStyleSheet('background-color: ' + variables.backend_color)

        ## Set size ##
        autosize = getdata('autosize')
        width = getdata('width')
        height = getdata('height')

        if not width==None and not autosize=='Yes':
            variables.width = int(width)

        if not height==None and not autosize=='Yes':
            variables.height = int(height)

        self.resize(variables.width, variables.height)

        ## Set sides ##
        ## Set sides ##
        sides = getdata('sides')

        if sides == 'Yes':
            variables.sides = True
        else:
            variables.sides = False

        if variables.sides == False:
            self.setWindowFlag(Qt.FramelessWindowHint)

        ## Show ##

            ## Get data ##
        fullscreen = getdata('fullscreen')

        if fullscreen == 'Yes':
            variables.fullscreen = True
        else:
            variables.fullscreen = False

        if variables.fullscreen == True:
            self.showFullScreen()
        else:
            self.show()

        ## Run backend after showing backend ##
        timeout = getdata('backend.timeout')
        if timeout==None:
            variables.backend_timeout = 1000
        else:
            variables.backend_timeout = int(timeout)

        QTimer.singleShot(variables.backend_timeout,self.runSplash) ## Run splash after 1s

## Splash ##
class Splash (QMainWindow):

    ## Run login page ##
    def runLogin(self):
        self.setCentralWidget(Login([self.Backend]))

    def __init__(self,ports):
        super(Splash, self).__init__()

        ## Get informations ##
        cs = files.readall('/proc/info/cs')
        ver = files.readall('/proc/info/ver')
        cd = files.readall('/proc/info/cd')

        self.setWindowTitle(cs + ' ' + ver + ' (' + cd + ")")

        ## Get app logo ##
        applogo = getdata('logo')
        if not applogo == None:
            self.setWindowIcon(QIcon(res.get(applogo)))

        ## Get app logo ##
        applogo = getdata('logo')
        if not applogo==None:
            self.setWindowIcon(QIcon(res.get(applogo)))

        ## Ports ##

        self.Backend = ports[0]

        ## Get backend color ##
        color = getdata('splash.color')

        ## Set color ##
        if not color==None:
            variables.splash_color = color

        self.setStyleSheet('background-color: {0}'.replace('{0}',variables.splash_color))

        ## Set size ##
        width = getdata('width')
        height = getdata('height')
        autosize =getdata('autosize')

        if not width == None  and not autosize=='Yes':
            variables.width = int(width)

        if not height == None:
            variables.height = int(height)

        self.resize(variables.width, variables.height)

        ## Set sides ##
        sides = getdata('sides')

        if sides=='Yes':
            variables.sides = True
        else:
            variables.sides = False

        if variables.sides == False:
            self.setWindowFlag(Qt.FramelessWindowHint)

        ## Show ##
        ## Get data ##
        fullscreen = getdata('fullscreen')

        if fullscreen == 'Yes':
            variables.fullscreen = True
        else:
            variables.fullscreen = False

        if variables.fullscreen == True:
            self.showFullScreen()
        else:
            self.show()

        ## Splash Logo ##

        logo = getdata('splash.logo')

        self.logo = QToolButton()
        self.layout().addWidget (self.logo)

        ## Set logo ##
        if not logo==None:
            self.logo.setIcon(QIcon(res.get(logo)))

        logo_size = getdata('splash.logo-size')

        if not logo_size==None:
            self.w = int(logo_size)
        else:
            self.w = 300

        self.logo.setMaximumSize(self.w,self.w) ## Set size
        self.logo.setIconSize(QSize(self.w,self.w))

        self.logo.setStyleSheet('border:none;')

        self.logo.setGeometry(int(self.width()/2)-int(self.w/2),int(self.height()/2)-int(self.w/2),self.w,self.w)

        ## Run splash after showing backend ##
        timeout = getdata('splash.timeout')
        if timeout==None:
            variables.splash_timeout = 3000
        else:
            variables.splash_timeout = int(timeout)

        QTimer.singleShot(variables.splash_timeout, self.runLogin) ## Run login

## LoginW ##
class LoginWidget (QMainWindow):
    def __init__(self,ports):
        super(LoginWidget, self).__init__()

        ## ports ##

        self.Backend = ports[0]
        self.Env = ports[1]

        ######

        loginw_bgcolor = getdata('loginw.bgcolor')
        loginw_fgcolor = getdata('loginw.fgcolor')
        loginw_width = getdata('loginw.width')
        loginw_height = getdata('loginw.height')
        loginw_round = getdata('loginw.round')
        loginw_location = getdata('loginw.location')

        ## Check data ##
        if loginw_bgcolor == None:
            loginw_bgcolor = 'white'

        if loginw_fgcolor == None:
            loginw_fgcolor = 'black'

        if loginw_width == None:
            loginw_width = self.width()

        if loginw_height == None:
            loginw_height = self.height()

        if loginw_round == 'Yes':
            loginw_round = '20% 20%'
        else:
            loginw_round = '0% 0%'

        if loginw_location == None:
            loginw_location = 'center'

        self.setStyleSheet('background-color:{0};color:{1};border-radius:{2};'
                                  .replace('{0}', loginw_bgcolor)
                                  .replace('{1}', loginw_fgcolor)
                                  .replace('{2}', loginw_round)
                                  )  ## Set color white as default
        self.setMaximumSize(int(loginw_width), int(loginw_height))  ## Set size of loginw

        ## Locations ##

        if loginw_location=='center':
            self.setGeometry(int(self.Env.width() / 2) - int(self.width() / 2),int(self.Env.height() / 2) - int(self.height() / 2), self.width(),self.height())  ## Geometric
        elif loginw_location=='top':
            self.setGeometry(int(self.Env.width() / 2) - int(self.width() / 2),int(self.height()/20), self.width(),self.height())  ## Geometric
        elif loginw_location=='left':
            self.setGeometry(int(self.width()/20),int(self.Env.height() / 2) - int(self.height() / 2), self.width(),self.height())  ## Geometric
        elif loginw_location=='right':
            self.setGeometry(self.Env.width()-int(self.width()/20)-self.width(),int(self.Env.height() / 2) - int(self.height() / 2), self.width(),self.height())  ## Geometric
        elif loginw_location=='bottom':
            self.setGeometry(int(self.Env.width() / 2) - int(self.width() / 2),self.Env.height()-int(self.height()/20)-self.height(), self.width(),self.height())  ## Geometric
## Login ##
class Login (QMainWindow):
    def __init__(self,ports):
        super(Login, self).__init__()

        ## Get informations ##
        cs = files.readall('/proc/info/cs')
        ver = files.readall('/proc/info/ver')
        cd = files.readall('/proc/info/cd')

        self.setWindowTitle(cs + ' ' + ver + ' (' + cd + ")")

        ## Get app logo ##
        applogo = getdata('logo')
        if not applogo == None:
            self.setWindowIcon(QIcon(res.get(applogo)))

        ## Ports ##

        self.Backend = ports[0]

        bgcolor = getdata('login.bgcolor')
        background = getdata('login.background')
        fgcolor = getdata('login.fgcolor')

        ## Set fgcolor ##
        if fgcolor == None:
            variables.login_fgcolor = 'cdack'
        else:
            variables.login_fgcolor = fgcolor

        ## Widget for bgcolor or background ##
        self.backgroundButton = QPushButton()
        self.backgroundButton.setGeometry(0,0,variables.width,variables.height)
        self.layout().addWidget(self.backgroundButton)

        ## Set bgcolor and background ##
        if background==None and bgcolor==None:

            ## Set bgcolor ##
            variables.login_bgcolor = 'white'
            self.setStyleSheet('color: {0};'.replace('{0}',variables.login_fgcolor))
            self.backgroundButton.setStyleSheet('border:none;background-color: {0};'.replace('{0}',variables.login_bgcolor))

        elif background==None:

            ## Set bgcolor ##
            variables.login_bgcolor = bgcolor

            self.setStyleSheet('color: {0};'.replace('{0}', variables.login_fgcolor))

            self.backgroundButton.setStyleSheet('border:none;background-color: {0};'.replace('{0}', variables.login_bgcolor))
        else:
            ## Set bgcolor ##
            variables.login_background = res.get(background)
            self.setStyleSheet('color: {0};'.replace('{0}', variables.login_fgcolor))
            self.backgroundButton.setStyleSheet('border:none;background-image: url({0});'.replace('{0}', variables.login_background))

        ## Set size ##
        width = getdata('width')
        height = getdata('height')
        autosize =getdata('autosize')

        if not width == None  and not autosize=='Yes':
            variables.width = int(width)

        if not height == None:
            variables.height = int(height)

        self.resize(variables.width, variables.height)

        ## Set sides ##
        ## Set sides ##
        sides = getdata('sides')

        if sides == 'Yes':
            variables.sides = True
        else:
            variables.sides = False
        if variables.sides == False:
            self.setWindowFlag(Qt.FramelessWindowHint)

        ## Login widget ##

            ## Import data ##
        self.loginw = LoginWidget([self.Backend,self])
        self.layout().addWidget (self.loginw)

        ## Show ##
        ## Get data ##
        fullscreen = getdata('fullscreen')

        if fullscreen == 'Yes':
            variables.fullscreen = True
        else:
            variables.fullscreen = False

        if variables.fullscreen == True:
            self.showFullScreen()
        else:
            self.show()

## Enter ##
class Enter (QMainWindow):
    def __init__(self,ports,username):
        super(Enter, self).__init__()

        ## Get informations ##
        cs = files.readall('/proc/info/cs')
        ver = files.readall('/proc/info/ver')
        cd = files.readall('/proc/info/cd')

        self.setWindowTitle(cs + ' ' + ver + ' (' + cd + ")")

        ## Get app logo ##
        applogo = getdata('logo')
        if not applogo == None:
            self.setWindowIcon(QIcon(res.get(applogo)))

        bgcolor = getdata('enter.bgcolor')
        background = getdata('enter.background')
        fgcolor = getdata('enter.fgcolor')

        ## Set fgcolor ##
        if fgcolor == None:
            variables.enter_fgcolor = 'cdack'
        else:
            variables.enter_fgcolor = fgcolor

        ## Widget for bgcolor or background ##
        self.backgroundButton = QPushButton()
        self.backgroundButton.setGeometry(0, 0, variables.width, variables.height)
        self.layout().addWidget(self.backgroundButton)

        ## Set bgcolor and background ##
        if background == None and bgcolor == None:

            ## Set bgcolor ##
            variables.login_bgcolor = 'white'
            self.setStyleSheet('color: {0};'.replace('{0}', variables.enter_fgcolor))
            self.backgroundButton.setStyleSheet(
                'border:none;background-color: {0};'.replace('{0}', variables.enter_bgcolor))

        elif background == None:

            ## Set bgcolor ##
            variables.login_bgcolor = bgcolor

            self.setStyleSheet('color: {0};'.replace('{0}', variables.enter_fgcolor))

            self.backgroundButton.setStyleSheet(
                'border:none;background-color: {0};'.replace('{0}', variables.enter_bgcolor))
        else:
            ## Set bgcolor ##
            variables.login_background = res.get(background)
            self.setStyleSheet('color: {0};'.replace('{0}', variables.enter_fgcolor))
            self.backgroundButton.setStyleSheet(
                'border:none;background-image: url({0});'.replace('{0}', variables.enter_background))

        ## Set size ##
        width = getdata('width')
        height = getdata('height')
        autosize =getdata('autosize')

        if not width == None  and not autosize=='Yes':
            variables.width = int(width)

        if not height == None:
            variables.height = int(height)

        self.resize(variables.width, variables.height)

        ## Set sides ##
        ## Set sides ##
        sides = getdata('sides')

        if sides == 'Yes':
            variables.sides = True
        else:
            variables.sides = False
        if variables.sides == False:
            self.setWindowFlag(Qt.FramelessWindowHint)

        ## Show ##
        ## Get data ##
        fullscreen = getdata('fullscreen')

        if fullscreen == 'Yes':
            variables.fullscreen = True
        else:
            variables.fullscreen = False

        if variables.fullscreen == True:
            self.showFullScreen()
        else:
            self.show()

## Desktop ##
class Desktop (QMainWindow):
    def __init__(self,ports,username,password):
        super(Desktop, self).__init__()

        ## Get informations ##
        cs = files.readall('/proc/info/cs')
        ver = files.readall('/proc/info/ver')
        cd = files.readall('/proc/info/cd')

        self.setWindowTitle(cs + ' ' + ver + ' (' + cd + ")")

        ## Get app logo ##
        applogo = getdata('logo')
        if not applogo == None:
            self.setWindowIcon(QIcon(res.get(applogo)))

        ## Widget for bgcolor or background ##
        self.backgroundButton = QPushButton()
        self.backgroundButton.setGeometry(0, 0, variables.width, variables.height)
        self.layout().addWidget(self.backgroundButton)

        bgcolor = getdata('enter.bgcolor')
        background = getdata('enter.background')
        fgcolor = getdata('enter.fgcolor')

        ## Set fgcolor ##
        if fgcolor == None:
            variables.enter_fgcolor = 'cdack'
        else:
            variables.enter_fgcolor = fgcolor


        ## Set bgcolor and background ##
        if background == None and bgcolor == None:

            ## Set bgcolor ##
            variables.login_bgcolor = 'white'
            self.setStyleSheet('color: {0};'.replace('{0}', variables.login_fgcolor))
            self.backgroundButton.setStyleSheet(
                'border:none;background-color: {0};'.replace('{0}', variables.login_bgcolor))

        elif background == None:

            ## Set bgcolor ##
            variables.login_bgcolor = bgcolor

            self.setStyleSheet('color: {0};'.replace('{0}', variables.login_fgcolor))

            self.backgroundButton.setStyleSheet(
                'border:none;background-color: {0};'.replace('{0}', variables.login_bgcolor))
        else:
            ## Set bgcolor ##
            variables.login_background = res.get(background)
            self.setStyleSheet('color: {0};'.replace('{0}', variables.login_fgcolor))
            self.backgroundButton.setStyleSheet(
                'border:none;background-image: url({0});'.replace('{0}', variables.login_background))

        ## Set size ##
        width = getdata('width')
        height = getdata('height')
        autosize =getdata('autosize')

        if not width == None  and not autosize=='Yes':
            variables.width = int(width)

        if not height == None:
            variables.height = int(height)

        self.resize(variables.width, variables.height)

        ## Set sides ##
        ## Set sides ##
        sides = getdata('sides')

        if sides == 'Yes':
            variables.sides = True
        else:
            variables.sides = False
        if variables.sides == False:
            self.setWindowFlag(Qt.FramelessWindowHint)

        ## Show ##
        ## Get data ##
        fullscreen = getdata('fullscreen')

        if fullscreen == 'Yes':
            variables.fullscreen = True
        else:
            variables.fullscreen = False

        if variables.fullscreen == True:
            self.showFullScreen()
        else:
            self.show()

    ## Run baran as Backend ##
if sys.argv[1:]==[]:
    mainApp = Backend()

    ## Run baran as Splash Page ##
elif sys.argv[1]=='splash':
    mainApp = Splash([None])

    ## Run baran as Login Page ##
elif sys.argv[1]=='login':
    mainApp = Login([None])

    ## Run baran as Enter Page ##
elif sys.argv[1]=='su':
    mainApp = Enter([None],sys.argv[2])

    ## Run baran as Desktop page ##
elif sys.argv[1]=='user':
    mainApp = Desktop([None],sys.argv[2],sys.argv[3])

else:
    exit()

application.exec_()
