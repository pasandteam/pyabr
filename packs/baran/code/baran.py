
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
import sys, hashlib, os
from libnam import colors, control, files, modules, permissions, process
from libabr import app, archive, core, file, res

## Main entry ##
application = QApplication (sys.argv)
app.start('desktop')
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

        ## Set port name ##
        self.setObjectName('Backend')

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

        ## Set port name ##
        self.setObjectName('Splash')

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
        loginw_round_size = getdata('loginw.round-size')
        loginw_location = getdata('loginw.location')
        loginw_shadow = getdata('loginw.shadow')
        loginw_userlogo = getdata('loginw.userlogo')
        loginw_userlogo_shadow = getdata('loginw.userlogo.shadow')
        loginw_userlogo_color = getdata('loginw.userlogo.color')
        loginw_input_bgcolor = getdata('loginw.input.bgcolor')
        loginw_input_fgcolor = getdata('loginw.input.fgcolor')
        loginw_input_shadow = getdata('loginw.input.shadow')
        loginw_input_round = getdata('loginw.input.round')
        loginw_input_round_size = getdata('loginw.input.round-size')
        loginw_userlogo_round = getdata('loginw.userlogo.round')
        loginw_userlogo_round_size = getdata('loginw.userlogo.round-size')
        loginw_input_fontsize = getdata('loginw.input.fontsize')

        ## Check data ##
        if loginw_bgcolor == None:
            loginw_bgcolor = 'white'

        if loginw_fgcolor == None:
            loginw_fgcolor = 'black'

        if loginw_width == None:
            loginw_width = self.width()

        if loginw_height == None:
            loginw_height = self.height()

        if loginw_round_size == None:
            loginw_round_size = '20% 20%'
        else:
            loginw_round_size = loginw_round_size.replace(' ','% ')+'%'

        if loginw_userlogo_round_size == None:
            loginw_userlogo_round_size = '125% 125%'
        else:
            loginw_userlogo_round_size = loginw_userlogo_round_size.replace(' ','% ')+'%'

        if loginw_input_round_size == None:
            loginw_input_round_size = '20% 20%'
        else:
            loginw_input_round_size = loginw_input_round_size.replace(' ','% ')+'%'

        if loginw_round == 'Yes':
            loginw_round = loginw_round_size
        else:
            loginw_round = '0% 0%'

        if loginw_userlogo_round == 'Yes':
            loginw_userlogo_round = loginw_userlogo_round_size
        else:
            loginw_userlogo_round = '0% 0%'

        if loginw_input_round == 'Yes':
            loginw_input_round = loginw_input_round_size
        else:
            loginw_input_round = '0% 0%'

        if loginw_location == None:
            loginw_location = 'center'

        if loginw_input_fontsize==None:
            loginw_input_fontsize = 12
        else:
            loginw_input_fontsize = int(loginw_input_fontsize)

        self.setMaximumSize(int(loginw_width), int(loginw_height))  ## Set size of loginw

        ## Locations ##

        if loginw_location == 'center':
            self.setGeometry(int(self.Env.width() / 2) - int(self.width() / 2),
                             int(self.Env.height() / 2) - int(self.height() / 2), self.width(),
                             self.height())  ## Geometric
        elif loginw_location == 'top':
            self.setGeometry(int(self.Env.width() / 2) - int(self.width() / 2), int(self.height() / 20), self.width(),
                             self.height())  ## Geometric
        elif loginw_location == 'left':
            self.setGeometry(int(self.width() / 20), int(self.Env.height() / 2) - int(self.height() / 2), self.width(),
                             self.height())  ## Geometric
        elif loginw_location == 'right':
            self.setGeometry(self.Env.width() - int(self.width() / 20) - self.width(),
                             int(self.Env.height() / 2) - int(self.height() / 2), self.width(),
                             self.height())  ## Geometric
        elif loginw_location == 'bottom':
            self.setGeometry(int(self.Env.width() / 2) - int(self.width() / 2),
                             self.Env.height() - int(self.height() / 20) - self.height(), self.width(),
                             self.height())  ## Geometric

        if loginw_shadow=='Yes':
            ## Shadow ##
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.setGraphicsEffect(shadow)

            ## BackgroudcolorButton ##
        self.btnColorButton = QPushButton()
        self.btnColorButton.setGeometry(0,0,self.width(),self.height())
        self.layout().addWidget(self.btnColorButton)
            ##

            ## Set colors ##
        self.setStyleSheet('color:{0};border-radius:{1};'
            .replace('{0}', loginw_fgcolor)
            .replace('{1}', loginw_round)
        )  ## Set color white as default
        self.btnColorButton.setStyleSheet('background-color:{0};'
            .replace('{0}',loginw_bgcolor)
        )

        ## Userlogo ##

        self.userlogo = QToolButton()

            ## Set size & location ##
        self.userlogo.setMaximumSize(250,250)
        self.userlogo.setGeometry(int(self.width()/2)-int(self.userlogo.width()/2),int(self.height()/4)-int(self.userlogo.height()/4),self.userlogo.width(),self.userlogo.height())

        if loginw_userlogo_color == None: loginw_userlogo_color = 'white'

        if not loginw_userlogo == None:
            if self.Env.objectName()=='Enter':
                logo = control.read_record ('loginw.userlogo','/etc/users/'+self.Env.username)
                if not logo == None: loginw_userlogo = logo

            self.userlogo.setStyleSheet('background-color: {0};border-radius: {1};background-image: url({2});'
                .replace('{0}', loginw_userlogo_color)
                .replace('{1}',loginw_userlogo_round)
                .replace('{2}', res.get(loginw_userlogo))
            )

            ## Shadow for userlogo ##
        ## Shadow ##
        if not loginw_userlogo_shadow=='No':
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.userlogo.setGraphicsEffect(shadow)

            ## Default userlogo ##
        self.layout().addWidget (self.userlogo)

            ## leInput username ##

        self.leInput = QLineEdit()

            ## Size & Location of leInput ##
        self.leInput.setMaximumSize(int(self.width()/2),40)
        self.leInput.setGeometry(int(self.width()/2)-int(self.leInput.width()/2),self.height()-int(self.height()/4)-self.leInput.height(),self.leInput.width(),self.leInput.height())

            ## Shadow of leInput ##
        ## Shadow ##
        if not loginw_input_shadow=='No':
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.leInput.setGraphicsEffect(shadow)

            ## Colors of leInput ##
        if loginw_input_bgcolor==None: loginw_input_bgcolor='white'
        if loginw_input_fgcolor==None: loginw_input_fgcolor='black'

            ## Setting up all colors ##
        self.leInput.setStyleSheet('background-color: '+loginw_input_bgcolor+';color: '+loginw_input_fgcolor+";border-width: 3%;border-radius: "+loginw_input_round)

            ## Place holder in input ##

        if self.Env.objectName()=='Login':
            self.leInput.setPlaceholderText(res.get('@string/username_placeholder')) # See https://stackoverflow.com/questions/24274318/placeholder-text-not-showing-pyside-pyqt
        else:
            self.leInput.setEchoMode(QLineEdit.Password)
            print (res.get('@string/password_placeholder').replace("{0}",self.Env.username))
            self.leInput.setPlaceholderText(res.get('@string/password_placeholder').replace("{0}",self.Env.username))

            ## Setting up font settings ##
        f = QFont()
        f.setPointSize(loginw_input_fontsize)
        self.leInput.setFont(f)

            ## Connect to action ##

        self.leInput.returnPressed.connect (self.actions)

        ## Add leInput Widget ##
        self.layout().addWidget(self.leInput)

    def actions (self):
        if self.Env.objectName() == 'Login':
            username = self.leInput.text()  ## Get username

            if self.Env.guest == 'Yes' and username == 'guest':
                self.Env.setCentralWidget(Desktop([self.Backend,self],username,'*'))

            elif not files.isfile('/etc/users/' + username):
                self.leInput.clear()
                self.leInput.setEnabled(False)
                message = res.get('@string/user_not_found')
                if not message==None: message = message.replace("{0}",username)
                self.leInput.setPlaceholderText(message)
                QTimer.singleShot(2500, self.clean)
            else:
                ## Check user ##
                hashname = hashlib.sha3_256(username.encode()).hexdigest()  ## Get hashname
                name = control.read_record ('username','/etc/users/'+username)

                if not hashname==name:
                    self.leInput.clear()
                    self.leInput.setEnabled(False)
                    message = res.get('@string/user_not_found')
                    if not message == None: message = message.replace("{0}", username)
                    self.leInput.setPlaceholderText(message)
                    QTimer.singleShot(2500, self.clean)

                else:
                    ## Setting up switched user ##

                    self.Env.setCentralWidget(Enter ([self.Backend,self],username)) ## Switch user
        elif self.Env.objectName()=='Enter':

            username = self.Env.username
            password = self.leInput.text()

            ## Check password ##
            hashcode = hashlib.sha3_512(password.encode()).hexdigest() ## Create hashcode for password
            code = control.read_record('code','/etc/users/'+username)

            if not code==hashcode:
                self.leInput.clear()
                self.leInput.setEnabled(False)
                message = res.get('@string/wrong_password')
                self.leInput.setPlaceholderText(message)
                QTimer.singleShot(2500, self.clean)
            else:
                self.Env.setCentralWidget(Desktop([self.Backend,self],username,password))

    def clean (self):
        self.leInput.setEnabled(True)
        if self.Env.objectName()=='Login':
            self.leInput.setPlaceholderText(res.get('@string/username_placeholder')) # See https://stackoverflow.com/questions/24274318/placeholder-text-not-showing-pyside-pyqt
        else:
            self.leInput.setPlaceholderText(res.get('@string/password_placeholder').replace('{0}',self.Env.username))

## Login ##
class Login (QMainWindow):
    def __init__(self,ports):
        super(Login, self).__init__()

        ## Guest user ##
        self.guest = control.read_record('enable_gui','/etc/guest')

        ## Set port name ##
        self.setObjectName('Login')

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
            variables.login_fgcolor = 'black'
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

        ## username ##
        self.username = username

        ## Ports ##
        self.Backend = ports[0]
        self.Env = ports[1]

        ## Set port name ##
        self.setObjectName('Enter')

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

        if not self.username=='guest':
            value = control.read_record('enter.bgcolor','/etc/users/'+self.username)
            if not value==None: bgcolor = value

        if not self.username=='guest':
            value = control.read_record('enter.background','/etc/users/'+self.username)
            if not value==None: background = value

        if not self.username=='guest':
            value = control.read_record('enter.fgcolor','/etc/users/'+self.username)
            if not value==None: fgcolor = value

        ## Set fgcolor ##
        if fgcolor == None:
            variables.enter_fgcolor = 'black'
        else:
            variables.enter_fgcolor = fgcolor

        ## Widget for bgcolor or background ##
        self.backgroundButton = QPushButton()
        self.backgroundButton.setGeometry(0, 0, variables.width, variables.height)
        self.layout().addWidget(self.backgroundButton)

        ## Set bgcolor and background ##
        if background == None and bgcolor == None:

            ## Set bgcolor ##
            variables.enter_bgcolor = 'white'
            self.setStyleSheet('color: {0};'.replace('{0}', variables.enter_fgcolor))
            self.backgroundButton.setStyleSheet(
                'border:none;background-color: {0};'.replace('{0}', variables.enter_bgcolor))

        elif background == None:

            ## Set bgcolor ##
            variables.enter_bgcolor = bgcolor

            self.setStyleSheet('color: {0};'.replace('{0}', variables.enter_fgcolor))

            self.backgroundButton.setStyleSheet(
                'border:none;background-color: {0};'.replace('{0}', variables.enter_bgcolor))
        else:
            ## Set bgcolor ##
            variables.enter_background = res.get(background)
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

        ## Login widget ##

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

## Desktop ##
class Desktop (QMainWindow):
    def __init__(self,ports,username,password):
        super(Desktop, self).__init__()

        ## Set port name ##
        self.setObjectName('Desktop')

        ## username ##
        self.username = username
        self.password = password

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

        bgcolor = getdata('desktop.bgcolor')
        background = getdata('desktop.background')
        fgcolor = getdata('desktop.fgcolor')

        if not self.username=='guest':
            value = control.read_record('desktop.bgcolor','/etc/users/'+self.username)
            if not value==None: bgcolor = value

        if not self.username=='guest':
            value = control.read_record('desktop.background','/etc/users/'+self.username)
            if not value==None: background = value

        if not self.username=='guest':
            value = control.read_record('desktop.fgcolor','/etc/users/'+self.username)
            if not value==None: fgcolor = value

        ## Set fgcolor ##
        if fgcolor == None:
            variables.enter_fgcolor = 'black'
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

        if not height == None and not autosize=='Yes':
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