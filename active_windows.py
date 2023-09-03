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
import time

app = QApplication(sys.argv)

screen_resolution = app.desktop().screenGeometry()
width = screen_resolution.width() 

height = 25
position_x = 500
position_y = 0

styleSheet = """
    background-color: #454545;
    font-size:22px;
    color : white;
"""

def loop_function():
    import importXlib

class MainWindow(QLabel):
    def __init__(self):
        super().__init__()

        self.setStyleSheet(styleSheet)
        self.move(position_x,position_y)

        self.setWindowFlag(Qt.X11BypassWindowManagerHint)
        self.setWindowFlag(Qt.NoDropShadowWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.FramelessWindowHint) 
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(QSize(width-1500, height))

        self.identify_windows()

    def identify_windows(self):
        threading.Thread(target=loop_function).start()
        
        disp = Xlib.display.Display()
        windows = disp.get_input_focus().focus
        win_title = windows.get_wm_name()
        
        button = QLabel(win_title,self)
        button.setAttribute(Qt.WA_TranslucentBackground)
        button.move(0,0)

window = MainWindow()

window.show()

app.exec()