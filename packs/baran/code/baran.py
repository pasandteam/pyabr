
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
    login_bgcolor = '#123456'
    login_fgcolor = '#000000'
    login_background = None
    enter_bgcolor = None
    enter_fgcolor = '#000000'
    enter_background = None
    username = ''
    password = ''
    desktop_bgcolor = '#FFFFFF'
    desktop_fgcolor = '#000000'
    desktop_background = None
    taskbar_bgcolor = '#FFFFFF'
    loginw_bgcolor = '#FFFFFF'
    userlogo_color = '#FFFFFF'
    input_bgcolor = '#FFFFFF'
    input_fgcolor = '#000000'
    loginw_fgcolor = '#000000'
    loginw_round_size = 20
    loginw_userlogo_round_size = 125
    loginw_input_round_size = 20
    loginw_location = 'center'
    loginw_input_fontsize = 12
    loginw_login_bgcolor = '#ABCDEF'
    loginw_login_fgcolor = '#FFFFFF'
    loginw_login_pressed_bgcolor = '#123456'
    loginw_login_pressed_fgcolor = '#FFFFFF'
    loginw_login_fontsize = 12
    loginw_login_round = 'Yes'
    loginw_login_round_size = 20
    loginw_login_hide = 'No'
    loginw_login_width = 300
    loginw_enter_bgcolor = 'pink'
    loginw_enter_fgcolor = '#FFFFFF'
    loginw_enter_pressed_bgcolor = 'purple'
    loginw_enter_pressed_fgcolor = '#FFFFFF'
    loginw_enter_fontsize = 12
    loginw_enter_round = 'Yes'
    loginw_enter_round_size = 20
    loginw_enter_hide = 'No'
    loginw_enter_width = 300
    loginw_shadow = 'Yes'
    loginw_userlogo_shadow = 'Yes'
    loginw_input_shadow = 'Yes'
    loginw_login_shadow = 'No'
    loginw_enter_shadow = 'No'
    loginw_input_width = 300
    loginw_input_height = 40
    loginw_login_height = 40
    loginw_enter_height = 40

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
        loginw_input_width = getdata('loginw.input.width')
        loginw_input_round_size = getdata('loginw.input.round-size')
        loginw_userlogo_round = getdata('loginw.userlogo.round')
        loginw_userlogo_round_size = getdata('loginw.userlogo.round-size')
        loginw_input_fontsize = getdata('loginw.input.fontsize')
        loginw_login_bgcolor = getdata('loginw.login.bgcolor')
        loginw_login_fgcolor = getdata('loginw.login.fgcolor')
        loginw_login_fontsize = getdata('loginw.login.fontsize')
        loginw_login_round = getdata('loginw.login.round')
        loginw_login_round_size = getdata('loginw.login.round-size')
        loginw_login_hide = getdata ('loginw.login.hide')
        loginw_login_pressed_fgcolor = getdata('loginw.login.pressed-fgcolor')
        loginw_login_pressed_bgcolor = getdata('loginw.login.pressed-bgcolor')
        loginw_login_width = getdata('loginw.login.width')
        loginw_login_shadow = getdata('loginw.login.shadow')
        loginw_enter_bgcolor = getdata('loginw.enter.bgcolor')
        loginw_enter_fgcolor = getdata('loginw.enter.fgcolor')
        loginw_enter_fontsize = getdata('loginw.enter.fontsize')
        loginw_enter_round = getdata('loginw.enter.round')
        loginw_enter_round_size = getdata('loginw.enter.round-size')
        loginw_enter_hide = getdata('loginw.enter.hide')
        loginw_enter_pressed_fgcolor = getdata('loginw.enter.pressed-fgcolor')
        loginw_enter_pressed_bgcolor = getdata('loginw.enter.pressed-bgcolor')
        loginw_enter_width = getdata('loginw.enter.width')
        loginw_enter_shadow = getdata('loginw.enter.shadow')
        loginw_input_height = getdata('loginw.input.height')
        loginw_login_height = getdata('loginw.login.height')
        loginw_enter_height = getdata('loginw.enter.height')

        ## Check data ##
        if loginw_bgcolor == None:
            loginw_bgcolor = variables.loginw_bgcolor

        if loginw_input_height == None:
            loginw_input_height = variables.loginw_input_height
        else:
            loginw_input_height = int(loginw_input_height)

        if loginw_login_height == None:
            loginw_login_height = variables.loginw_login_height
        else:
            loginw_login_height = int(loginw_login_height)

        if loginw_enter_height == None:
            loginw_enter_height = variables.loginw_enter_height
        else:
            loginw_enter_height = int(loginw_enter_height)

        if loginw_login_width == None:
            loginw_login_width = variables.loginw_login_width
        else:
            loginw_login_width = int(loginw_login_width)

        if loginw_input_width == None:
            loginw_input_width = variables.loginw_input_width
        else:
            loginw_input_width = int(loginw_input_width)

        if loginw_enter_width == None:
            loginw_enter_width = variables.loginw_enter_width
        else:
            loginw_enter_width = int(loginw_enter_width)

        if loginw_fgcolor == None:
            loginw_fgcolor = variables.loginw_fgcolor

        if loginw_login_bgcolor == None:
            loginw_login_bgcolor = variables.loginw_login_bgcolor

        if loginw_login_fgcolor == None:
            loginw_login_fgcolor = variables.loginw_login_fgcolor

        if loginw_login_pressed_bgcolor == None:
            loginw_login_pressed_bgcolor = variables.loginw_login_pressed_bgcolor

        if loginw_login_pressed_fgcolor == None:
            loginw_login_pressed_fgcolor = variables.loginw_login_pressed_fgcolor

        if loginw_enter_bgcolor == None:
            loginw_enter_bgcolor = variables.loginw_enter_bgcolor

        if loginw_enter_fgcolor == None:
            loginw_enter_fgcolor = variables.loginw_enter_fgcolor

        if loginw_enter_pressed_bgcolor == None:
            loginw_enter_pressed_bgcolor = variables.loginw_enter_pressed_bgcolor

        if loginw_enter_pressed_fgcolor == None:
            loginw_enter_pressed_fgcolor = variables.loginw_enter_pressed_fgcolor

        if loginw_width == None:
            loginw_width = self.width()

        if loginw_height == None:
            loginw_height = self.height()

        if loginw_round_size == None:
            loginw_round_size = str(variables.loginw_round_size)+'% '+str(variables.loginw_round_size)+'%'
        else:
            loginw_round_size = loginw_round_size.replace(' ','% ')+'%'

        if loginw_userlogo_round_size == None:
            loginw_userlogo_round_size = str(variables.loginw_userlogo_round_size)+'% '+str(variables.loginw_userlogo_round_size)+'%'
        else:
            loginw_userlogo_round_size = loginw_userlogo_round_size.replace(' ','% ')+'%'

        if loginw_input_round_size == None:
            loginw_input_round_size = str(variables.loginw_input_round_size)+'% '+str(variables.loginw_input_round_size)+'%'
        else:
            loginw_input_round_size = loginw_input_round_size.replace(' ','% ')+'%'

        if loginw_login_round_size == None:
            loginw_login_round_size = str(variables.loginw_login_round_size)+'% '+str(variables.loginw_login_round_size)+'%'
        else:
            loginw_login_round_size = loginw_login_round_size.replace(' ','% ')+'%'

        if loginw_enter_round_size == None:
            loginw_enter_round_size = str(variables.loginw_enter_round_size)+'% '+str(variables.loginw_enter_round_size)+'%'
        else:
            loginw_enter_round_size = loginw_enter_round_size.replace(' ','% ')+'%'

        if loginw_round == 'Yes':
            loginw_round = loginw_round_size
        else:
            loginw_round ='0% 0%'

        if loginw_userlogo_round == 'Yes':
            loginw_userlogo_round = loginw_userlogo_round_size
        else:
            loginw_userlogo_round = '0% 0%'

        if loginw_input_round == 'Yes':
            loginw_input_round = loginw_input_round_size
        else:
            loginw_input_round = '0% 0%'

        if loginw_login_round == 'Yes':
            loginw_login_round = loginw_login_round_size
        else:
            loginw_login_round = '0% 0%'

        if loginw_enter_round == 'Yes':
            loginw_enter_round = loginw_enter_round_size
        else:
            loginw_enter_round = '0% 0%'

        if loginw_location == None:
            loginw_location = variables.loginw_location

        if loginw_input_fontsize==None:
            loginw_input_fontsize = variables.loginw_input_fontsize
        else:
            loginw_input_fontsize = int(loginw_input_fontsize)

        if loginw_login_fontsize==None:
            loginw_login_fontsize = variables.loginw_login_fontsize
        else:
            loginw_login_fontsize = int(loginw_login_fontsize)

        if loginw_login_hide == None: loginw_login_hide = variables.loginw_login_hide

        if loginw_enter_fontsize==None:
            loginw_enter_fontsize = variables.loginw_enter_fontsize
        else:
            loginw_enter_fontsize = int(loginw_enter_fontsize)

        if loginw_enter_hide == None: loginw_enter_hide = variables.loginw_enter_hide

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

        if loginw_shadow==None: loginw_shadow = variables.loginw_shadow
        if loginw_userlogo_shadow == None: loginw_userlogo_shadow = variables.loginw_userlogo_shadow
        if loginw_input_shadow == None: loginw_input_shadow = variables.loginw_input_shadow
        if loginw_login_shadow == None: loginw_login_shadow = variables.loginw_login_shadow
        if loginw_enter_shadow == None: loginw_enter_shadow = variables.loginw_enter_shadow

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

        if loginw_userlogo_color == None: loginw_userlogo_color = variables.userlogo_color

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
        if loginw_userlogo_shadow=='Yes':
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
        self.leInput.setMaximumSize(loginw_input_width,loginw_input_height)
        self.leInput.setGeometry(int(self.width()/2)-int(self.leInput.width()/2),self.height()-int(self.height()/4)-self.leInput.height(),self.leInput.width(),self.leInput.height())

            ## Shadow of leInput ##
        ## Shadow ##
        if loginw_input_shadow=='Yes':
            # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.leInput.setGraphicsEffect(shadow)

            ## Colors of leInput ##
        if loginw_input_bgcolor==None: loginw_input_bgcolor=variables.input_bgcolor
        if loginw_input_fgcolor==None: loginw_input_fgcolor=variables.input_fgcolor

            ## Setting up all colors ##
        self.leInput.setStyleSheet('background-color: '+loginw_input_bgcolor+';color: '+loginw_input_fgcolor+";border-width: 3%;border-radius: "+loginw_input_round)

            ## Place holder in input ##

        if self.Env.objectName()=='Login':
            self.leInput.setPlaceholderText(res.get('@string/username_placeholder')) # See https://stackoverflow.com/questions/24274318/placeholder-text-not-showing-pyside-pyqt
        else:
            self.leInput.setEchoMode(QLineEdit.Password)
            self.leInput.setPlaceholderText(res.get('@string/password_placeholder').replace("{0}",self.Env.username))

            ## Setting up font settings ##
        f = QFont()
        f.setPointSize(loginw_input_fontsize)
        self.leInput.setFont(f)

            ## Connect to action ##

        self.leInput.returnPressed.connect (self.actions)

        ## Add leInput Widget ##
        self.layout().addWidget(self.leInput)

            ## Enter button ##
        if self.Env.objectName()=='Login':
            self.btnLogin = QPushButton()

            ## Shadow ##
            if loginw_login_shadow == 'Yes':
                ## Shadow ##
                # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
                shadow = QGraphicsDropShadowEffect()
                shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
                shadow.setOffset(0)
                shadow.setBlurRadius(10)
                self.btnLogin.setGraphicsEffect(shadow)

            self.btnLogin.clicked.connect (self.actions)
            print(loginw_login_round)
            self.btnLogin.setStyleSheet('''
                    QPushButton {
                        background-color: ''' + loginw_login_bgcolor + """;
                        color: """ + loginw_login_fgcolor + """;
                        border-radius: """ + loginw_login_round + '''
                    } 
                    QPushButton:pressed {
                        background-color:''' + loginw_login_pressed_bgcolor + ''';
                        color:''' + loginw_login_pressed_fgcolor + ''';
                        border-radius: ''' + loginw_login_round + ''';
                    }
                    ''')

            f = QFont()
            f.setPointSize(loginw_login_fontsize)
            self.btnLogin.setFont(f)
            if loginw_login_hide == 'Yes':
                self.btnLogin.hide()
            self.btnLogin.setText(res.get('@string/next_text'))
            self.btnLogin.setMaximumSize(loginw_login_width, loginw_login_height)
            self.btnLogin.setGeometry(int(self.width() / 2) - int(self.btnLogin.width() / 2),
                                      self.height() - int(self.height() / 4) - int(self.btnLogin.height() / 4) + int(self.btnLogin.height()/2),
                                      self.btnLogin.width(), self.btnLogin.height())
            self.layout().addWidget(self.btnLogin)
        else:
            self.btnEnter = QPushButton()
            ## Shadow ##
            if loginw_enter_shadow == 'Yes':
                ## Shadow ##
                # Copy right shadow box: medium.com/@rekols/qt-button-box-shadow-property-c47c7bf58721 ##
                shadow = QGraphicsDropShadowEffect()
                shadow.setColor(QColor(10, 2, 34, 255 * 0.8))
                shadow.setOffset(0)
                shadow.setBlurRadius(10)
                self.btnEnter.setGraphicsEffect(shadow)

            self.btnEnter.clicked.connect (self.actions)
            self.btnEnter.setStyleSheet('''
                    QPushButton {
                        background-color: ''' + loginw_enter_bgcolor + """;
                        color: """ + loginw_enter_fgcolor + """;
                        border-radius: """ + loginw_enter_round + '''
                    } 
                    QPushButton:pressed {
                        background-color:''' + loginw_enter_pressed_bgcolor + ''';
                        color:''' + loginw_enter_pressed_fgcolor + ''';
                        border-radius: ''' + loginw_enter_round + ''';
                    }
                    ''')

            f = QFont()
            f.setPointSize(loginw_enter_fontsize)
            self.btnEnter.setFont(f)
            if loginw_enter_hide == 'Yes':
                self.btnEnter.hide()
            self.btnEnter.setText(res.get('@string/enter_text'))
            self.btnEnter.setMaximumSize(loginw_enter_width, loginw_enter_height)
            self.btnEnter.setGeometry(int(self.width() / 2) - int(self.btnEnter.width() / 2),
                                      self.height() - int(self.height() / 4) - int(self.btnEnter.height() / 4) + int(self.btnEnter.height()/2),
                                      self.btnEnter.width(), self.btnEnter.height())
            self.layout().addWidget(self.btnEnter)


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

        ## Widget for bgcolor or background ##
        self.backgroundButton = QPushButton()
        self.backgroundButton.setGeometry(0,0,variables.width,variables.height)
        self.layout().addWidget(self.backgroundButton)

        ## Set bgcolor and background ##

        if background==None and bgcolor==None and not fgcolor==None:
            variables.login_fgcolor = fgcolor
            ## Set colors ##
            self.setStyleSheet('color: {0};'.replace('{0}',variables.login_fgcolor))
            self.backgroundButton.setStyleSheet('border:none;background-color: {0};'.replace('{0}',variables.login_bgcolor))

        elif background==None and not fgcolor==None:

            ## Set colors ##
            variables.login_bgcolor = bgcolor
            variables.login_fgcolor = fgcolor

            self.setStyleSheet('color: {0};'.replace('{0}', variables.login_fgcolor))

            self.backgroundButton.setStyleSheet('border:none;background-color: {0};'.replace('{0}', variables.login_bgcolor))
        elif not background==None and not fgcolor==None:
            ## Set bgcolor ##

            variables.login_background = res.get(background)
            self.setStyleSheet('color: {0};'.replace('{0}', variables.login_fgcolor))
            self.backgroundButton.setStyleSheet('border:none;background-image: url({0});'.replace('{0}', variables.login_background))
        else:
            self.setStyleSheet('background-color:{1};color: {0};'.replace('{0}', variables.login_fgcolor).replace('{1}',variables.login_bgcolor))

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
        self.username = username.lower()

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

        ## Widget for bgcolor or background ##
        self.backgroundButton = QPushButton()
        self.backgroundButton.setGeometry(0, 0, variables.width, variables.height)
        self.layout().addWidget(self.backgroundButton)

        ## Set bgcolor and background ##

        if background == None and bgcolor == None and not fgcolor == None:
            variables.enter_fgcolor = fgcolor
            ## Set colors ##
            self.setStyleSheet('color: {0};'.replace('{0}', variables.enter_fgcolor))
            self.backgroundButton.setStyleSheet(
                'border:none;background-color: {0};'.replace('{0}', variables.enter_bgcolor))

        elif background == None and not fgcolor == None:

            ## Set colors ##
            variables.enter_bgcolor = bgcolor
            variables.enter_fgcolor = fgcolor

            self.setStyleSheet('color: {0};'.replace('{0}', variables.enter_fgcolor))

            self.backgroundButton.setStyleSheet(
                'border:none;background-color: {0};'.replace('{0}', variables.enter_bgcolor))
        elif not background == None and not fgcolor == None:
            ## Set bgcolor ##

            variables.enter_background = res.get(background)
            self.setStyleSheet('color: {0};'.replace('{0}', variables.enter_fgcolor))
            self.backgroundButton.setStyleSheet(
                'border:none;background-image: url({0});'.replace('{0}', variables.enter_background))
        else:
            self.setStyleSheet('background-color:{1};color: {0};'.replace('{0}', variables.enter_fgcolor).replace('{1}',
                                                                                                                  variables.enter_bgcolor))

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

## Taskbar ##
class TaskBar (QToolBar):
    def __init__(self,ports):
        super(TaskBar,self).__init__()

        ## Ports ##
        self.Backend = ports[0]
        self.Env = ports[1]

        ## Set username ##
        self.username = self.Env.username

            ## Get DATAS ###################

        ## Set bgcolor ##
        bgcolor = getdata('taskbar.bgcolor')
        if not self.Env.username=='guest':
            value = control.read_record('taskbar.bgcolor','/etc/users/'+self.username)
            if not value==None: bgcolor = value
        if bgcolor == None: bgcolor = variables.taskbar_bgcolor

        ## Set fgcolor ##
        fgcolor = getdata('taskbar.fgcolor')
        if not self.Env.username=='guest':
            value = control.read_record('taskbar.fgcolor','/etc/users/'+self.username)
            if not value==None: fgcolor = value
        if fgcolor == None: fgcolor = 'black'

            ################################

        # styles #

        self.setStyleSheet('background-color: '+bgcolor+";color: "+fgcolor+";")

        ## Add taskbar ##
        self.Env.addToolBar (self)

## Desktop ##
class Desktop (QMainWindow):
    def __init__(self,ports,username,password):
        super(Desktop, self).__init__()

        ## Set port name ##
        self.setObjectName('Desktop')

        ## ports ##
        self.Backend = ports[0]

        ## username ##
        self.username = username.lower()
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


        ## Check background or bgcolor in users ##
        if not self.username=='guest':
            value = control.read_record('desktop.bgcolor','/etc/users/'+self.username)
            if not value==None: bgcolor = value

        if not self.username=='guest':
            value = control.read_record('desktop.background','/etc/users/'+self.username)
            if not value==None: background = value

        if not self.username=='guest':
            value = control.read_record('desktop.fgcolor','/etc/users/'+self.username)
            if not value==None: fgcolor = value

            ## Set bgcolor and background ##

            if background == None and bgcolor == None and not fgcolor == None:
                variables.desktop_fgcolor = fgcolor
                ## Set colors ##
                self.setStyleSheet('color: {0};'.replace('{0}', variables.desktop_fgcolor))
                self.backgroundButton.setStyleSheet(
                    'border:none;background-color: {0};'.replace('{0}', variables.desktop_bgcolor))

            elif background == None and not fgcolor == None:

                ## Set colors ##
                variables.desktop_bgcolor = bgcolor
                variables.desktop_fgcolor = fgcolor

                self.setStyleSheet('color: {0};'.replace('{0}', variables.desktop_fgcolor))

                self.backgroundButton.setStyleSheet(
                    'border:none;background-color: {0};'.replace('{0}', variables.desktop_bgcolor))
            elif not background == None and not fgcolor == None:
                ## Set bgcolor ##

                variables.desktop_background = res.get(background)
                self.setStyleSheet('color: {0};'.replace('{0}', variables.desktop_fgcolor))
                self.backgroundButton.setStyleSheet(
                    'border:none;background-image: url({0});'.replace('{0}', variables.desktop_background))
            else:
                self.setStyleSheet(
                    'background-color:{1};color: {0};'.replace('{0}', variables.desktop_fgcolor).replace('{1}',
                                                                                                       variables.desktop_bgcolor))

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

        ## Taskbar ##
        self.taskbar = TaskBar ([Backend,self])

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