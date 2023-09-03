from PyQt5.QtCore import QSize, Qt,QTimer,QDateTime
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QDialog, QLineEdit, QStatusBar
from PyQt5 import QtGui
from PyQt5.QtCore import*
from pathlib import Path
import os
from ewmh import EWMH
import netifaces as ni
import sys
import socket
import Xlib
import Xlib.display
import threading

app = QApplication(sys.argv)

screen_resolution = app.desktop().screenGeometry()
width = screen_resolution.width() 

height = 25
position_x = 1
position_y = 0

styleSheet = """
    background-color: #454545;
    font-size:22px;
    color : white;
"""

home = str(Path.home())

time = QDateTime.currentDateTime()
this_time = time.toString('M/d/yyyy h:mm:ss ap')

net_dev = 'wlp2s0'

def window_detect():
    import active_windows

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setStyleSheet(styleSheet)
        self.move(position_x,position_y)

        self.setWindowFlag(Qt.X11BypassWindowManagerHint)
        self.setWindowFlag(Qt.NoDropShadowWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.FramelessWindowHint) 
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(QSize(width, height))

        self.clock = QLabel(this_time,self)
        self.clock.setAttribute(Qt.WA_TranslucentBackground)
        self.clock.move(width - 250,0)
        self.clock.resize(500,25)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)


        self.identify_host()

        self.identify_network()

        self.identify_user()

    threading.Thread(target=window_detect).start()

    def identify_host(self):
        button = QLabel(socket.gethostname(),self)
        button.setAttribute(Qt.WA_TranslucentBackground)
        button.move(0,0)
        button.resize(200,25)

    def identify_user(self):
        user = os.getlogin()
        button = QLabel(user,self)
        button.setAttribute(Qt.WA_TranslucentBackground)
        button.move(width - 520,0)
        button.resize(80,25)

    def identify_network(self):
        ip = ni.ifaddresses(net_dev)[ni.AF_INET][0]['addr']
        button = QLabel(ip,self)
        button.setAttribute(Qt.WA_TranslucentBackground)
        button.move(width-420,0)
        button.resize(150,25)

    def showTime(self):
        time = QDateTime.currentDateTime()
        this_time = time.toString('M/d/yyyy h:mm:ss ap')
        self.clock.setText(this_time)

window = MainWindow()

window.show()

app.exec()
