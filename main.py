#!/usr/bin/env python
# -*- coding: utf-8 -*-
#███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
#████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
#██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
#██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
#██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
#╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#            @GorpoOrko | Manicomio TCXS Project | 2020
"""Anotações:

criar arquivo mainwindow.py:
    pyuic5 -x mainwindow.ui -o mainwindow.py

criar arquivo files_rc_rc.py
    pyrcc5 -o files_rc_rc.py files_rc.qrc


sempre que quisermos chamar um stackedWidget usamos o comando abaixo e mudar sua "indexação"
    self.ui.stackedWidget.setCurrentIndex(1)

usando o sistema para chamar os arquivos do layout:
    self.ui.string_do_objeto


Exemplo de layout limpo:
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QFile
from mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):

    # --------------FUNÇÃO DE INICIO
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
"""
from PyQt5 import QtCore, QtGui, QtWidgets,QtWebEngineWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import cvlib as cv
import cv2
from cvlib.object_detection import draw_bbox
from PIL import Image, ImageQt
import subprocess
import sys
import time
#importaçoes pessoais-------------->
from mainwindow import Ui_MainWindow
from funcoes import menus
from funcoes import camera
from funcoes import deepnude
from funcoes import minibrowser
from funcoes.relogio_digital import DigitalClock
from funcoes import homeWindows
from funcoes import serverDeepnude
from funcoes import botDeepnude
from funcoes import python_console
from funcoes import recognition
from funcoes import faceRecognition
from funcoes import db_links
from funcoes import botManicomio

class MainWindow(QMainWindow):
    def movimentoMouse(self):
        self.mwidget = QMainWindow(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # remove a barra
        self.center()
        # cria uma falsa label em todo objeto para poder ser movido
        self.lbl = QLabel(self)
        # self.lbl.setText("cria um texto para achar a label, pois ali em baixo sumi com ela da tela")
        self.lbl.setGeometry(-50, -50, 60, 40)
        self.oldPos = self.pos()
        self.show()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        # print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
    #limpa os campos do painel bd
    def limpaTitulodb(self,event):
        self.ui.db_texto_titulo.clear()
    def limpaLinkdb(self,event):
        self.ui.db_texto_link.clear()
    def limpaCodigodb(self,event):
        self.ui.db_texto_codigo.clear()
    def limpaObservacaodb(self,event):
        self.ui.db_texto_observacao.clear()


    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.clic= pyqtSignal()
        #menus------------->
        self.movimentoMouse()
        menus.menusJanela(self)
        #funcoes------------>
        camera.funcoesCamera(self)
        minibrowser.funcoesBrowser(self)
        deepnude.funcoesDeepfake(self)
        DigitalClock.mostraRelogio(self)
        homeWindows.funcoesWindowsSO(self)
        serverDeepnude.funcoesServerDeepnude(self)
        botDeepnude.funcoesBotdeepnude(self)
        python_console.Consolepython(self)
        recognition.funcoesRecognition(self)
        faceRecognition.funcoesFacerecognition(self)
        db_links.funcoesBancodadoslink(self)
        botManicomio.funcoesBotmanicomio(self)









if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
