# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(892, 699)
        self.janela_pai = QtWidgets.QWidget(MainWindow)
        self.janela_pai.setObjectName("janela_pai")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.janela_pai)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menuTopo = QtWidgets.QFrame(self.janela_pai)
        self.menuTopo.setMaximumSize(QtCore.QSize(16777215, 45))
        self.menuTopo.setStyleSheet("background-color: rgb(31, 31, 31);")
        self.menuTopo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menuTopo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuTopo.setObjectName("menuTopo")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.menuTopo)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_abre_menu = QtWidgets.QFrame(self.menuTopo)
        self.frame_abre_menu.setMinimumSize(QtCore.QSize(50, 0))
        self.frame_abre_menu.setMaximumSize(QtCore.QSize(50, 50))
        self.frame_abre_menu.setStyleSheet("background-color: rgb(31,31,31);")
        self.frame_abre_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_abre_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_abre_menu.setObjectName("frame_abre_menu")
        self.botao_abrir_menu = QtWidgets.QPushButton(self.frame_abre_menu)
        self.botao_abrir_menu.setGeometry(QtCore.QRect(-10, -1, 75, 50))
        self.botao_abrir_menu.setMinimumSize(QtCore.QSize(50, 50))
        self.botao_abrir_menu.setStyleSheet("QPushButton {\n"
"    background-image: url(:/abre_menu/images/menu-4-24.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_abrir_menu.setText("")
        self.botao_abrir_menu.setObjectName("botao_abrir_menu")
        self.horizontalLayout_2.addWidget(self.frame_abre_menu)
        self.frame_informacoes = QtWidgets.QFrame(self.menuTopo)
        self.frame_informacoes.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_informacoes.setStyleSheet("background-color: rgb(31,31,31);")
        self.frame_informacoes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_informacoes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_informacoes.setObjectName("frame_informacoes")
        self.label_6 = QtWidgets.QLabel(self.frame_informacoes)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 171, 21))
        self.label_6.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.frame_informacoes)
        self.frame_minimizar = QtWidgets.QFrame(self.menuTopo)
        self.frame_minimizar.setMinimumSize(QtCore.QSize(50, 50))
        self.frame_minimizar.setMaximumSize(QtCore.QSize(50, 50))
        self.frame_minimizar.setStyleSheet("background-color: rgb(31,31,31);")
        self.frame_minimizar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_minimizar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_minimizar.setObjectName("frame_minimizar")
        self.botao_minimizar = QtWidgets.QPushButton(self.frame_minimizar)
        self.botao_minimizar.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_minimizar.setStyleSheet("QPushButton {\n"
"    background-image: url(:/minimizar/images/minimize.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_minimizar.setText("")
        self.botao_minimizar.setObjectName("botao_minimizar")
        self.horizontalLayout_2.addWidget(self.frame_minimizar)
        self.frame_maximizar = QtWidgets.QFrame(self.menuTopo)
        self.frame_maximizar.setMinimumSize(QtCore.QSize(50, 50))
        self.frame_maximizar.setMaximumSize(QtCore.QSize(50, 50))
        self.frame_maximizar.setStyleSheet("background-color: rgb(31,31,31);")
        self.frame_maximizar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_maximizar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_maximizar.setObjectName("frame_maximizar")
        self.botao_maximizar = QtWidgets.QPushButton(self.frame_maximizar)
        self.botao_maximizar.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_maximizar.setStyleSheet("QPushButton {\n"
"    \n"
"    background-image: url(:/maximizar/images/icons8-toggle-full-screen-24.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_maximizar.setText("")
        self.botao_maximizar.setObjectName("botao_maximizar")
        self.horizontalLayout_2.addWidget(self.frame_maximizar)
        self.frame_fechar = QtWidgets.QFrame(self.menuTopo)
        self.frame_fechar.setMinimumSize(QtCore.QSize(50, 50))
        self.frame_fechar.setMaximumSize(QtCore.QSize(50, 50))
        self.frame_fechar.setStyleSheet("background-color: rgb(31,31,31);")
        self.frame_fechar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_fechar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_fechar.setObjectName("frame_fechar")
        self.botao_fechar = QtWidgets.QPushButton(self.frame_fechar)
        self.botao_fechar.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_fechar.setStyleSheet("QPushButton {\n"
"    background-image: url(:/fechar/images/icons8-delete-24.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_fechar.setText("")
        self.botao_fechar.setObjectName("botao_fechar")
        self.horizontalLayout_2.addWidget(self.frame_fechar)
        self.verticalLayout.addWidget(self.menuTopo)
        self.conteiner_central = QtWidgets.QFrame(self.janela_pai)
        self.conteiner_central.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.conteiner_central.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conteiner_central.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteiner_central.setObjectName("conteiner_central")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.conteiner_central)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu_esquerda = QtWidgets.QFrame(self.conteiner_central)
        self.menu_esquerda.setMinimumSize(QtCore.QSize(50, 0))
        self.menu_esquerda.setMaximumSize(QtCore.QSize(50, 16777215))
        self.menu_esquerda.setStyleSheet("background-color: rgb(31, 31, 31);")
        self.menu_esquerda.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menu_esquerda.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_esquerda.setObjectName("menu_esquerda")
        self.menu_home = QtWidgets.QFrame(self.menu_esquerda)
        self.menu_home.setGeometry(QtCore.QRect(0, 0, 250, 50))
        self.menu_home.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.menu_home.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_home.setObjectName("menu_home")
        self.botao_home = QtWidgets.QPushButton(self.menu_home)
        self.botao_home.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_home.setStyleSheet("QPushButton {\n"
"    background-image: url(:/home/images/home-5-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_home.setText("")
        self.botao_home.setObjectName("botao_home")
        self.texto_menu_home = QtWidgets.QLabel(self.menu_home)
        self.texto_menu_home.setGeometry(QtCore.QRect(60, -1, 191, 51))
        self.texto_menu_home.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_menu_home.setObjectName("texto_menu_home")
        self.menu_browser = QtWidgets.QFrame(self.menu_esquerda)
        self.menu_browser.setGeometry(QtCore.QRect(0, 50, 250, 50))
        self.menu_browser.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.menu_browser.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_browser.setObjectName("menu_browser")
        self.botao_browser = QtWidgets.QPushButton(self.menu_browser)
        self.botao_browser.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_browser.setStyleSheet("QPushButton {\n"
"    background-image: url(:/browser/images/browser-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_browser.setText("")
        self.botao_browser.setObjectName("botao_browser")
        self.texto_menu_browser = QtWidgets.QLabel(self.menu_browser)
        self.texto_menu_browser.setGeometry(QtCore.QRect(60, -1, 191, 51))
        self.texto_menu_browser.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_menu_browser.setObjectName("texto_menu_browser")
        self.menu_python = QtWidgets.QFrame(self.menu_esquerda)
        self.menu_python.setGeometry(QtCore.QRect(0, 100, 250, 50))
        self.menu_python.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.menu_python.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_python.setObjectName("menu_python")
        self.botao_python = QtWidgets.QPushButton(self.menu_python)
        self.botao_python.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_python.setStyleSheet("QPushButton {\n"
"    background-image: url(:/logo_python/images/python.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_python.setText("")
        self.botao_python.setObjectName("botao_python")
        self.texto_menu_python = QtWidgets.QLabel(self.menu_python)
        self.texto_menu_python.setGeometry(QtCore.QRect(60, -1, 191, 51))
        self.texto_menu_python.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_menu_python.setObjectName("texto_menu_python")
        self.menu_server_deepfake = QtWidgets.QFrame(self.menu_esquerda)
        self.menu_server_deepfake.setGeometry(QtCore.QRect(0, 150, 250, 50))
        self.menu_server_deepfake.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.menu_server_deepfake.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_server_deepfake.setObjectName("menu_server_deepfake")
        self.botao_server_deepfake = QtWidgets.QPushButton(self.menu_server_deepfake)
        self.botao_server_deepfake.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_server_deepfake.setStyleSheet("QPushButton {\n"
"    \n"
"    background-image: url(:/server/images/server-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_server_deepfake.setText("")
        self.botao_server_deepfake.setObjectName("botao_server_deepfake")
        self.texto_menu_server_deepfake = QtWidgets.QLabel(self.menu_server_deepfake)
        self.texto_menu_server_deepfake.setGeometry(QtCore.QRect(60, -1, 191, 51))
        self.texto_menu_server_deepfake.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_menu_server_deepfake.setObjectName("texto_menu_server_deepfake")
        self.menu_database = QtWidgets.QFrame(self.menu_esquerda)
        self.menu_database.setGeometry(QtCore.QRect(0, 200, 250, 50))
        self.menu_database.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.menu_database.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_database.setObjectName("menu_database")
        self.botao_database = QtWidgets.QPushButton(self.menu_database)
        self.botao_database.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_database.setStyleSheet("QPushButton {\n"
"    background-image: url(:/banco de dados/images/data-configuration-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_database.setText("")
        self.botao_database.setObjectName("botao_database")
        self.texto_menu_database = QtWidgets.QLabel(self.menu_database)
        self.texto_menu_database.setGeometry(QtCore.QRect(60, -1, 191, 51))
        self.texto_menu_database.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_menu_database.setObjectName("texto_menu_database")
        self.menus_bots = QtWidgets.QFrame(self.menu_esquerda)
        self.menus_bots.setGeometry(QtCore.QRect(0, 300, 250, 50))
        self.menus_bots.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menus_bots.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menus_bots.setObjectName("menus_bots")
        self.menu_bot1 = QtWidgets.QFrame(self.menus_bots)
        self.menu_bot1.setGeometry(QtCore.QRect(0, 0, 250, 50))
        self.menu_bot1.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.menu_bot1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_bot1.setObjectName("menu_bot1")
        self.botao_menu_bot1 = QtWidgets.QPushButton(self.menu_bot1)
        self.botao_menu_bot1.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_menu_bot1.setStyleSheet("QPushButton {\n"
"    background-image: url(:/bot/images/telegram.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_menu_bot1.setText("")
        self.botao_menu_bot1.setObjectName("botao_menu_bot1")
        self.texto_menu_bot1 = QtWidgets.QLabel(self.menu_bot1)
        self.texto_menu_bot1.setGeometry(QtCore.QRect(60, 0, 191, 51))
        self.texto_menu_bot1.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_menu_bot1.setObjectName("texto_menu_bot1")
        self.menu_bot2 = QtWidgets.QFrame(self.menus_bots)
        self.menu_bot2.setGeometry(QtCore.QRect(0, 50, 250, 50))
        self.menu_bot2.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.menu_bot2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_bot2.setObjectName("menu_bot2")
        self.botao_menu_bot2 = QtWidgets.QPushButton(self.menu_bot2)
        self.botao_menu_bot2.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_menu_bot2.setStyleSheet("QPushButton {\n"
"    background-image: url(:/bot/images/telegram.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_menu_bot2.setText("")
        self.botao_menu_bot2.setObjectName("botao_menu_bot2")
        self.texto_menu_bot2 = QtWidgets.QLabel(self.menu_bot2)
        self.texto_menu_bot2.setGeometry(QtCore.QRect(60, 0, 191, 51))
        self.texto_menu_bot2.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_menu_bot2.setObjectName("texto_menu_bot2")
        self.menu_bot3 = QtWidgets.QFrame(self.menus_bots)
        self.menu_bot3.setGeometry(QtCore.QRect(0, 100, 250, 50))
        self.menu_bot3.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.menu_bot3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_bot3.setObjectName("menu_bot3")
        self.botao_menu_bot3 = QtWidgets.QPushButton(self.menu_bot3)
        self.botao_menu_bot3.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_menu_bot3.setStyleSheet("QPushButton {\n"
"    background-image: url(:/bot/images/telegram.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_menu_bot3.setText("")
        self.botao_menu_bot3.setObjectName("botao_menu_bot3")
        self.texto_menu_bot3 = QtWidgets.QLabel(self.menu_bot3)
        self.texto_menu_bot3.setGeometry(QtCore.QRect(60, 0, 191, 51))
        self.texto_menu_bot3.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_menu_bot3.setObjectName("texto_menu_bot3")
        self.menus_camera = QtWidgets.QFrame(self.menu_esquerda)
        self.menus_camera.setGeometry(QtCore.QRect(0, 250, 250, 50))
        self.menus_camera.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menus_camera.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menus_camera.setObjectName("menus_camera")
        self.menu_camera1 = QtWidgets.QFrame(self.menus_camera)
        self.menu_camera1.setGeometry(QtCore.QRect(0, 0, 250, 50))
        self.menu_camera1.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.menu_camera1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_camera1.setObjectName("menu_camera1")
        self.botao_menu_camera1 = QtWidgets.QPushButton(self.menu_camera1)
        self.botao_menu_camera1.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_menu_camera1.setStyleSheet("QPushButton {\n"
"    background-image: url(:/camera/images/screenshot-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_menu_camera1.setText("")
        self.botao_menu_camera1.setObjectName("botao_menu_camera1")
        self.texto_menu_camera1 = QtWidgets.QLabel(self.menu_camera1)
        self.texto_menu_camera1.setGeometry(QtCore.QRect(60, 0, 191, 51))
        self.texto_menu_camera1.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_menu_camera1.setObjectName("texto_menu_camera1")
        self.menu_camera2 = QtWidgets.QFrame(self.menus_camera)
        self.menu_camera2.setGeometry(QtCore.QRect(0, 50, 250, 50))
        self.menu_camera2.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.menu_camera2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_camera2.setObjectName("menu_camera2")
        self.botao_menu_camera2 = QtWidgets.QPushButton(self.menu_camera2)
        self.botao_menu_camera2.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_menu_camera2.setStyleSheet("QPushButton {\n"
"    background-image: url(:/camera/images/screenshot-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_menu_camera2.setText("")
        self.botao_menu_camera2.setObjectName("botao_menu_camera2")
        self.texto_menu_camera2 = QtWidgets.QLabel(self.menu_camera2)
        self.texto_menu_camera2.setGeometry(QtCore.QRect(60, -1, 191, 51))
        self.texto_menu_camera2.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_menu_camera2.setObjectName("texto_menu_camera2")
        self.menu_camera3 = QtWidgets.QFrame(self.menus_camera)
        self.menu_camera3.setGeometry(QtCore.QRect(0, 100, 250, 50))
        self.menu_camera3.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.menu_camera3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_camera3.setObjectName("menu_camera3")
        self.botao_menu_camera3 = QtWidgets.QPushButton(self.menu_camera3)
        self.botao_menu_camera3.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_menu_camera3.setStyleSheet("QPushButton {\n"
"    background-image: url(:/camera/images/screenshot-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_menu_camera3.setText("")
        self.botao_menu_camera3.setObjectName("botao_menu_camera3")
        self.texto_menu_camera3 = QtWidgets.QLabel(self.menu_camera3)
        self.texto_menu_camera3.setGeometry(QtCore.QRect(60, -1, 191, 51))
        self.texto_menu_camera3.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_menu_camera3.setObjectName("texto_menu_camera3")
        self.menu_camera4 = QtWidgets.QFrame(self.menus_camera)
        self.menu_camera4.setGeometry(QtCore.QRect(0, 150, 250, 50))
        self.menu_camera4.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.menu_camera4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_camera4.setObjectName("menu_camera4")
        self.botao_menu_camera4 = QtWidgets.QPushButton(self.menu_camera4)
        self.botao_menu_camera4.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_menu_camera4.setStyleSheet("QPushButton {\n"
"    background-image: url(:/camera/images/screenshot-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_menu_camera4.setText("")
        self.botao_menu_camera4.setObjectName("botao_menu_camera4")
        self.texto_menu_camera4 = QtWidgets.QLabel(self.menu_camera4)
        self.texto_menu_camera4.setGeometry(QtCore.QRect(60, -1, 191, 51))
        self.texto_menu_camera4.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_menu_camera4.setObjectName("texto_menu_camera4")
        self.menu_camera5 = QtWidgets.QFrame(self.menus_camera)
        self.menu_camera5.setGeometry(QtCore.QRect(0, 200, 250, 50))
        self.menu_camera5.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.menu_camera5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_camera5.setObjectName("menu_camera5")
        self.botao_menu_camera5 = QtWidgets.QPushButton(self.menu_camera5)
        self.botao_menu_camera5.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_menu_camera5.setStyleSheet("QPushButton {\n"
"    background-image: url(:/camera/images/screenshot-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_menu_camera5.setText("")
        self.botao_menu_camera5.setObjectName("botao_menu_camera5")
        self.texto_menu_camera5 = QtWidgets.QLabel(self.menu_camera5)
        self.texto_menu_camera5.setGeometry(QtCore.QRect(60, -1, 191, 51))
        self.texto_menu_camera5.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_menu_camera5.setObjectName("texto_menu_camera5")
        self.horizontalLayout.addWidget(self.menu_esquerda)
        self.janela_central = QtWidgets.QFrame(self.conteiner_central)
        self.janela_central.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.janela_central.setFrameShadow(QtWidgets.QFrame.Raised)
        self.janela_central.setObjectName("janela_central")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.janela_central)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.barra_status = QtWidgets.QFrame(self.janela_central)
        self.barra_status.setMinimumSize(QtCore.QSize(0, 15))
        self.barra_status.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.barra_status.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.barra_status.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_status.setObjectName("barra_status")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.barra_status)
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.status = QtWidgets.QLabel(self.barra_status)
        self.status.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(98, 103, 111);\n"
"font: 10px ,Segoe UI;\n"
"}\n"
"\n"
"")
        self.status.setObjectName("status")
        self.horizontalLayout_8.addWidget(self.status)
        self.status_pagina_atual = QtWidgets.QLabel(self.barra_status)
        self.status_pagina_atual.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(98, 103, 111);\n"
"font: 10px ,Segoe UI;\n"
"}\n"
"\n"
"")
        self.status_pagina_atual.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.status_pagina_atual.setObjectName("status_pagina_atual")
        self.horizontalLayout_8.addWidget(self.status_pagina_atual)
        self.verticalLayout_4.addWidget(self.barra_status)
        self.stackedWidget = QtWidgets.QStackedWidget(self.janela_central)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pagina_home = QtWidgets.QWidget()
        self.pagina_home.setObjectName("pagina_home")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.pagina_home)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.stackedWidget_home = QtWidgets.QStackedWidget(self.pagina_home)
        self.stackedWidget_home.setObjectName("stackedWidget_home")
        self.home_01 = QtWidgets.QWidget()
        self.home_01.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.home_01.setObjectName("home_01")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.home_01)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.background = QtWidgets.QLabel(self.home_01)
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("images/bg_home.jpg"))
        self.background.setAlignment(QtCore.Qt.AlignCenter)
        self.background.setWordWrap(False)
        self.background.setObjectName("background")
        self.horizontalLayout_12.addWidget(self.background)
        self.stackedWidget_home.addWidget(self.home_01)
        self.home_02 = QtWidgets.QWidget()
        self.home_02.setObjectName("home_02")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.home_02)
        self.verticalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.area_trabalho = QtWidgets.QFrame(self.home_02)
        self.area_trabalho.setMinimumSize(QtCore.QSize(0, 50))
        self.area_trabalho.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.area_trabalho.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.area_trabalho.setFrameShadow(QtWidgets.QFrame.Raised)
        self.area_trabalho.setObjectName("area_trabalho")
        self.bg_area_trabalho = QtWidgets.QLabel(self.area_trabalho)
        self.bg_area_trabalho.setEnabled(True)
        self.bg_area_trabalho.setGeometry(QtCore.QRect(-10, -10, 931, 591))
        self.bg_area_trabalho.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bg_area_trabalho.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.bg_area_trabalho.setText("")
        self.bg_area_trabalho.setPixmap(QtGui.QPixmap("images/bg_home.jpg"))
        self.bg_area_trabalho.setScaledContents(True)
        self.bg_area_trabalho.setObjectName("bg_area_trabalho")
        self.menu_iniciar_aberto = QtWidgets.QFrame(self.area_trabalho)
        self.menu_iniciar_aberto.setGeometry(QtCore.QRect(0, 340, 0, 251))
        self.menu_iniciar_aberto.setStyleSheet("QFrame {\n"
"    \n"
"    background-color: rgba(35, 35, 35, 35%);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}")
        self.menu_iniciar_aberto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_iniciar_aberto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_iniciar_aberto.setObjectName("menu_iniciar_aberto")
        self.botao_iniciar_deepnude = QtWidgets.QPushButton(self.menu_iniciar_aberto)
        self.botao_iniciar_deepnude.setGeometry(QtCore.QRect(90, 170, 75, 75))
        self.botao_iniciar_deepnude.setStyleSheet("QPushButton {\n"
"    background-image: url(:/bot/images/telegram.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"    padding-top: 50px; \n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(35, 35, 35);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_iniciar_deepnude.setObjectName("botao_iniciar_deepnude")
        self.botao_iniciar_botmanicomio = QtWidgets.QPushButton(self.menu_iniciar_aberto)
        self.botao_iniciar_botmanicomio.setGeometry(QtCore.QRect(170, 170, 75, 75))
        self.botao_iniciar_botmanicomio.setStyleSheet("QPushButton {\n"
"    background-image: url(:/bot/images/telegram.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"    padding-top: 50px; \n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(35, 35, 35);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_iniciar_botmanicomio.setObjectName("botao_iniciar_botmanicomio")
        self.botao_iniciar_recognition = QtWidgets.QPushButton(self.menu_iniciar_aberto)
        self.botao_iniciar_recognition.setGeometry(QtCore.QRect(170, 90, 75, 75))
        self.botao_iniciar_recognition.setStyleSheet("QPushButton {\n"
"    \n"
"    background-image: url(:/camera/images/screenshot-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"    padding-top: 50px; \n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(35, 35, 35);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_iniciar_recognition.setObjectName("botao_iniciar_recognition")
        self.botao_iniciar_server = QtWidgets.QPushButton(self.menu_iniciar_aberto)
        self.botao_iniciar_server.setGeometry(QtCore.QRect(90, 10, 75, 75))
        self.botao_iniciar_server.setStyleSheet("QPushButton {\n"
"    background-image: url(:/server/images/server-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"    padding-top: 50px; \n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(35, 35, 35);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_iniciar_server.setObjectName("botao_iniciar_server")
        self.botao_iniciar_facerecog = QtWidgets.QPushButton(self.menu_iniciar_aberto)
        self.botao_iniciar_facerecog.setGeometry(QtCore.QRect(90, 90, 75, 75))
        self.botao_iniciar_facerecog.setStyleSheet("QPushButton {\n"
"    \n"
"    background-image: url(:/camera/images/screenshot-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"    padding-top: 50px; \n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(35, 35, 35);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_iniciar_facerecog.setObjectName("botao_iniciar_facerecog")
        self.botao_iniciar_browser = QtWidgets.QPushButton(self.menu_iniciar_aberto)
        self.botao_iniciar_browser.setGeometry(QtCore.QRect(10, 10, 75, 75))
        self.botao_iniciar_browser.setStyleSheet("QPushButton {\n"
"    background-image: url(:/browser/images/browser-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"    padding-top: 50px; \n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(35, 35, 35);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_iniciar_browser.setObjectName("botao_iniciar_browser")
        self.botao_iniciar_camera = QtWidgets.QPushButton(self.menu_iniciar_aberto)
        self.botao_iniciar_camera.setGeometry(QtCore.QRect(10, 90, 75, 75))
        self.botao_iniciar_camera.setStyleSheet("QPushButton {\n"
"    \n"
"    background-image: url(:/camera/images/screenshot-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"    padding-top: 50px; \n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(35, 35, 35);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_iniciar_camera.setObjectName("botao_iniciar_camera")
        self.botao_iniciar_configuracoes = QtWidgets.QPushButton(self.menu_iniciar_aberto)
        self.botao_iniciar_configuracoes.setGeometry(QtCore.QRect(10, 170, 75, 75))
        self.botao_iniciar_configuracoes.setStyleSheet("QPushButton {\n"
"    background-image: url(:/configuracoes/images/services-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"    padding-top: 50px; \n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(35, 35, 35);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_iniciar_configuracoes.setObjectName("botao_iniciar_configuracoes")
        self.botao_iniciar_bancodados = QtWidgets.QPushButton(self.menu_iniciar_aberto)
        self.botao_iniciar_bancodados.setGeometry(QtCore.QRect(170, 10, 75, 75))
        self.botao_iniciar_bancodados.setStyleSheet("QPushButton {\n"
"    background-image: url(:/banco de dados/images/data-configuration-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"    padding-top: 50px; \n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(35, 35, 35);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_iniciar_bancodados.setObjectName("botao_iniciar_bancodados")
        self.verticalLayout_7.addWidget(self.area_trabalho)
        self.barra_iniciar = QtWidgets.QFrame(self.home_02)
        self.barra_iniciar.setMinimumSize(QtCore.QSize(0, 3))
        self.barra_iniciar.setMaximumSize(QtCore.QSize(16777215, 22))
        self.barra_iniciar.setStyleSheet("background-color: rgb(15, 16, 16);")
        self.barra_iniciar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.barra_iniciar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_iniciar.setObjectName("barra_iniciar")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.barra_iniciar)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.botao_menu_iniciar = QtWidgets.QPushButton(self.barra_iniciar)
        self.botao_menu_iniciar.setMaximumSize(QtCore.QSize(30, 30))
        self.botao_menu_iniciar.setStyleSheet("QPushButton {\n"
"    background-image: url(:/menu_iniciar/images/iniciar.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(35, 35, 35);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_menu_iniciar.setText("")
        self.botao_menu_iniciar.setObjectName("botao_menu_iniciar")
        self.horizontalLayout_11.addWidget(self.botao_menu_iniciar)
        self.barra_tarefas_iniciar = QtWidgets.QFrame(self.barra_iniciar)
        self.barra_tarefas_iniciar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_tarefas_iniciar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_tarefas_iniciar.setObjectName("barra_tarefas_iniciar")
        self.horizontalLayout_11.addWidget(self.barra_tarefas_iniciar)
        self.relogio2 = QtWidgets.QWidget(self.barra_iniciar)
        self.relogio2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.relogio2.setObjectName("relogio2")
        self.horizontalLayout_11.addWidget(self.relogio2)
        self.botao_direita_iniciar = QtWidgets.QPushButton(self.barra_iniciar)
        self.botao_direita_iniciar.setMaximumSize(QtCore.QSize(10, 16777215))
        self.botao_direita_iniciar.setText("")
        self.botao_direita_iniciar.setObjectName("botao_direita_iniciar")
        self.horizontalLayout_11.addWidget(self.botao_direita_iniciar)
        self.verticalLayout_7.addWidget(self.barra_iniciar)
        self.stackedWidget_home.addWidget(self.home_02)
        self.verticalLayout_6.addWidget(self.stackedWidget_home)
        self.stackedWidget.addWidget(self.pagina_home)
        self.pagina_camera = QtWidgets.QWidget()
        self.pagina_camera.setObjectName("pagina_camera")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.pagina_camera)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.area_video = QtWidgets.QLabel(self.pagina_camera)
        self.area_video.setStyleSheet("")
        self.area_video.setText("")
        self.area_video.setObjectName("area_video")
        self.verticalLayout_2.addWidget(self.area_video)
        self.menus_fotografia = QtWidgets.QFrame(self.pagina_camera)
        self.menus_fotografia.setMaximumSize(QtCore.QSize(16777215, 50))
        self.menus_fotografia.setStyleSheet("")
        self.menus_fotografia.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menus_fotografia.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menus_fotografia.setObjectName("menus_fotografia")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.menus_fotografia)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.camera_local = QtWidgets.QRadioButton(self.menus_fotografia)
        self.camera_local.setMinimumSize(QtCore.QSize(200, 50))
        self.camera_local.setStyleSheet("QRadioButton{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"")
        self.camera_local.setObjectName("camera_local")
        self.horizontalLayout_3.addWidget(self.camera_local)
        self.camera_droidcam = QtWidgets.QRadioButton(self.menus_fotografia)
        self.camera_droidcam.setMinimumSize(QtCore.QSize(0, 50))
        self.camera_droidcam.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.camera_droidcam.setAutoFillBackground(False)
        self.camera_droidcam.setStyleSheet("QRadioButton{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"")
        self.camera_droidcam.setObjectName("camera_droidcam")
        self.horizontalLayout_3.addWidget(self.camera_droidcam)
        self.botao_inica_video = QtWidgets.QPushButton(self.menus_fotografia)
        self.botao_inica_video.setMinimumSize(QtCore.QSize(0, 50))
        self.botao_inica_video.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_inica_video.setObjectName("botao_inica_video")
        self.horizontalLayout_3.addWidget(self.botao_inica_video)
        self.botao_bate_foto = QtWidgets.QPushButton(self.menus_fotografia)
        self.botao_bate_foto.setMinimumSize(QtCore.QSize(0, 50))
        self.botao_bate_foto.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_bate_foto.setObjectName("botao_bate_foto")
        self.horizontalLayout_3.addWidget(self.botao_bate_foto)
        self.verticalLayout_2.addWidget(self.menus_fotografia)
        self.stackedWidget.addWidget(self.pagina_camera)
        self.deep_fake = QtWidgets.QWidget()
        self.deep_fake.setObjectName("deep_fake")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.deep_fake)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.conteiner_logo_deepnude = QtWidgets.QFrame(self.deep_fake)
        self.conteiner_logo_deepnude.setMaximumSize(QtCore.QSize(16777215, 100))
        self.conteiner_logo_deepnude.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conteiner_logo_deepnude.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteiner_logo_deepnude.setObjectName("conteiner_logo_deepnude")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.conteiner_logo_deepnude)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.logo_deepnude = QtWidgets.QLabel(self.conteiner_logo_deepnude)
        self.logo_deepnude.setText("")
        self.logo_deepnude.setPixmap(QtGui.QPixmap("images/logo.png"))
        self.logo_deepnude.setObjectName("logo_deepnude")
        self.horizontalLayout_5.addWidget(self.logo_deepnude, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.conteiner_logo_deepnude)
        self.conteiner_imagens_deepnude = QtWidgets.QFrame(self.deep_fake)
        self.conteiner_imagens_deepnude.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conteiner_imagens_deepnude.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteiner_imagens_deepnude.setObjectName("conteiner_imagens_deepnude")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.conteiner_imagens_deepnude)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.imagem_normal_deepnude = QtWidgets.QLabel(self.conteiner_imagens_deepnude)
        self.imagem_normal_deepnude.setText("")
        self.imagem_normal_deepnude.setPixmap(QtGui.QPixmap("images/bg1.png"))
        self.imagem_normal_deepnude.setObjectName("imagem_normal_deepnude")
        self.horizontalLayout_6.addWidget(self.imagem_normal_deepnude, 0, QtCore.Qt.AlignHCenter)
        self.imagem_renderizada_deepnude = QtWidgets.QLabel(self.conteiner_imagens_deepnude)
        self.imagem_renderizada_deepnude.setText("")
        self.imagem_renderizada_deepnude.setPixmap(QtGui.QPixmap("images/bg2.png"))
        self.imagem_renderizada_deepnude.setObjectName("imagem_renderizada_deepnude")
        self.horizontalLayout_6.addWidget(self.imagem_renderizada_deepnude, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.conteiner_imagens_deepnude)
        self.conteiner_botoes_deepnude = QtWidgets.QFrame(self.deep_fake)
        self.conteiner_botoes_deepnude.setMaximumSize(QtCore.QSize(16777215, 50))
        self.conteiner_botoes_deepnude.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conteiner_botoes_deepnude.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteiner_botoes_deepnude.setObjectName("conteiner_botoes_deepnude")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.conteiner_botoes_deepnude)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.botao_imagem_deepnude = QtWidgets.QPushButton(self.conteiner_botoes_deepnude)
        self.botao_imagem_deepnude.setMinimumSize(QtCore.QSize(0, 50))
        self.botao_imagem_deepnude.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_imagem_deepnude.setObjectName("botao_imagem_deepnude")
        self.horizontalLayout_4.addWidget(self.botao_imagem_deepnude)
        self.botao_criar_deepnude = QtWidgets.QPushButton(self.conteiner_botoes_deepnude)
        self.botao_criar_deepnude.setMinimumSize(QtCore.QSize(0, 50))
        self.botao_criar_deepnude.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_criar_deepnude.setObjectName("botao_criar_deepnude")
        self.horizontalLayout_4.addWidget(self.botao_criar_deepnude)
        self.verticalLayout_3.addWidget(self.conteiner_botoes_deepnude)
        self.stackedWidget.addWidget(self.deep_fake)
        self.recognition = QtWidgets.QWidget()
        self.recognition.setObjectName("recognition")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.recognition)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.area_video_recognition = QtWidgets.QLabel(self.recognition)
        self.area_video_recognition.setStyleSheet("")
        self.area_video_recognition.setText("")
        self.area_video_recognition.setPixmap(QtGui.QPixmap("images/bg_camera.png"))
        self.area_video_recognition.setScaledContents(True)
        self.area_video_recognition.setObjectName("area_video_recognition")
        self.verticalLayout_11.addWidget(self.area_video_recognition)
        self.conteiner_botoes_recognition = QtWidgets.QFrame(self.recognition)
        self.conteiner_botoes_recognition.setMaximumSize(QtCore.QSize(16777215, 50))
        self.conteiner_botoes_recognition.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.conteiner_botoes_recognition.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteiner_botoes_recognition.setObjectName("conteiner_botoes_recognition")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.conteiner_botoes_recognition)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.camera_local_recognition = QtWidgets.QRadioButton(self.conteiner_botoes_recognition)
        self.camera_local_recognition.setMinimumSize(QtCore.QSize(100, 50))
        self.camera_local_recognition.setStyleSheet("QRadioButton{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"")
        self.camera_local_recognition.setObjectName("camera_local_recognition")
        self.horizontalLayout_14.addWidget(self.camera_local_recognition)
        self.camera_droidcam_recognition = QtWidgets.QRadioButton(self.conteiner_botoes_recognition)
        self.camera_droidcam_recognition.setMinimumSize(QtCore.QSize(0, 50))
        self.camera_droidcam_recognition.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.camera_droidcam_recognition.setAutoFillBackground(False)
        self.camera_droidcam_recognition.setStyleSheet("QRadioButton{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"")
        self.camera_droidcam_recognition.setObjectName("camera_droidcam_recognition")
        self.horizontalLayout_14.addWidget(self.camera_droidcam_recognition)
        self.botao_recognition_pessoas = QtWidgets.QPushButton(self.conteiner_botoes_recognition)
        self.botao_recognition_pessoas.setMinimumSize(QtCore.QSize(0, 50))
        self.botao_recognition_pessoas.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_recognition_pessoas.setObjectName("botao_recognition_pessoas")
        self.horizontalLayout_14.addWidget(self.botao_recognition_pessoas)
        self.botao_recognition_completo = QtWidgets.QPushButton(self.conteiner_botoes_recognition)
        self.botao_recognition_completo.setMinimumSize(QtCore.QSize(0, 50))
        self.botao_recognition_completo.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_recognition_completo.setObjectName("botao_recognition_completo")
        self.horizontalLayout_14.addWidget(self.botao_recognition_completo)
        self.verticalLayout_11.addWidget(self.conteiner_botoes_recognition)
        self.stackedWidget.addWidget(self.recognition)
        self.face_recognition = QtWidgets.QWidget()
        self.face_recognition.setObjectName("face_recognition")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.face_recognition)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.area_video_facerecognition = QtWidgets.QLabel(self.face_recognition)
        self.area_video_facerecognition.setStyleSheet("")
        self.area_video_facerecognition.setText("")
        self.area_video_facerecognition.setPixmap(QtGui.QPixmap("images/bg_camera.png"))
        self.area_video_facerecognition.setScaledContents(True)
        self.area_video_facerecognition.setObjectName("area_video_facerecognition")
        self.verticalLayout_12.addWidget(self.area_video_facerecognition)
        self.conteiner_botoes_facerecognition = QtWidgets.QFrame(self.face_recognition)
        self.conteiner_botoes_facerecognition.setMinimumSize(QtCore.QSize(0, 50))
        self.conteiner_botoes_facerecognition.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.conteiner_botoes_facerecognition.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteiner_botoes_facerecognition.setObjectName("conteiner_botoes_facerecognition")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.conteiner_botoes_facerecognition)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.camera_local_facerecognition = QtWidgets.QRadioButton(self.conteiner_botoes_facerecognition)
        self.camera_local_facerecognition.setMinimumSize(QtCore.QSize(200, 50))
        self.camera_local_facerecognition.setStyleSheet("QRadioButton{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"")
        self.camera_local_facerecognition.setObjectName("camera_local_facerecognition")
        self.horizontalLayout_15.addWidget(self.camera_local_facerecognition)
        self.camera_droidcam_facerecognition = QtWidgets.QRadioButton(self.conteiner_botoes_facerecognition)
        self.camera_droidcam_facerecognition.setMinimumSize(QtCore.QSize(0, 50))
        self.camera_droidcam_facerecognition.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.camera_droidcam_facerecognition.setAutoFillBackground(False)
        self.camera_droidcam_facerecognition.setStyleSheet("QRadioButton{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"")
        self.camera_droidcam_facerecognition.setObjectName("camera_droidcam_facerecognition")
        self.horizontalLayout_15.addWidget(self.camera_droidcam_facerecognition)
        self.botao_inica_facerecognition = QtWidgets.QPushButton(self.conteiner_botoes_facerecognition)
        self.botao_inica_facerecognition.setMinimumSize(QtCore.QSize(0, 50))
        self.botao_inica_facerecognition.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_inica_facerecognition.setObjectName("botao_inica_facerecognition")
        self.horizontalLayout_15.addWidget(self.botao_inica_facerecognition)
        self.verticalLayout_12.addWidget(self.conteiner_botoes_facerecognition)
        self.stackedWidget.addWidget(self.face_recognition)
        self.server_deepnude = QtWidgets.QWidget()
        self.server_deepnude.setObjectName("server_deepnude")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.server_deepnude)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.web_browser_flask = QtWebEngineWidgets.QWebEngineView(self.server_deepnude)
        self.web_browser_flask.setStyleSheet("background-color: rgb(15, 16, 16);")
        self.web_browser_flask.setObjectName("web_browser_flask")
        self.verticalLayout_8.addWidget(self.web_browser_flask)
        self.conteiner_serverdeepnude = QtWidgets.QFrame(self.server_deepnude)
        self.conteiner_serverdeepnude.setMaximumSize(QtCore.QSize(16777215, 55))
        self.conteiner_serverdeepnude.setFrameShape(QtWidgets.QFrame.Panel)
        self.conteiner_serverdeepnude.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteiner_serverdeepnude.setObjectName("conteiner_serverdeepnude")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.conteiner_serverdeepnude)
        self.horizontalLayout_13.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.inicia_server_deepnude = QtWidgets.QPushButton(self.conteiner_serverdeepnude)
        self.inicia_server_deepnude.setMinimumSize(QtCore.QSize(200, 42))
        self.inicia_server_deepnude.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.inicia_server_deepnude.setObjectName("inicia_server_deepnude")
        self.horizontalLayout_13.addWidget(self.inicia_server_deepnude)
        self.endereco_localhost = QtWidgets.QLineEdit(self.conteiner_serverdeepnude)
        self.endereco_localhost.setMinimumSize(QtCore.QSize(0, 40))
        self.endereco_localhost.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(85, 170, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.endereco_localhost.setObjectName("endereco_localhost")
        self.horizontalLayout_13.addWidget(self.endereco_localhost)
        self.endereco_ngrok = QtWidgets.QLineEdit(self.conteiner_serverdeepnude)
        self.endereco_ngrok.setMinimumSize(QtCore.QSize(0, 40))
        self.endereco_ngrok.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(85, 170, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.endereco_ngrok.setObjectName("endereco_ngrok")
        self.horizontalLayout_13.addWidget(self.endereco_ngrok)
        self.verticalLayout_8.addWidget(self.conteiner_serverdeepnude)
        self.stackedWidget.addWidget(self.server_deepnude)
        self.bot_deepfake = QtWidgets.QWidget()
        self.bot_deepfake.setObjectName("bot_deepfake")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.bot_deepfake)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_3 = QtWidgets.QFrame(self.bot_deepfake)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(40, 160, 300, 300))
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("QLabel{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 0px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLabel:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLabel:focus{\n"
"border: 2px solid  rgb(85, 170, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/marcinho.jpg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.logo_deepnude_2 = QtWidgets.QLabel(self.frame_3)
        self.logo_deepnude_2.setGeometry(QtCore.QRect(280, 40, 230, 72))
        self.logo_deepnude_2.setText("")
        self.logo_deepnude_2.setPixmap(QtGui.QPixmap("images/logo.png"))
        self.logo_deepnude_2.setObjectName("logo_deepnude_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_3)
        self.textBrowser.setGeometry(QtCore.QRect(410, 160, 391, 300))
        self.textBrowser.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_9.addWidget(self.frame_3)
        self.conteiner_bot_deepfake = QtWidgets.QFrame(self.bot_deepfake)
        self.conteiner_bot_deepfake.setMaximumSize(QtCore.QSize(16777215, 50))
        self.conteiner_bot_deepfake.setFrameShape(QtWidgets.QFrame.Panel)
        self.conteiner_bot_deepfake.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteiner_bot_deepfake.setObjectName("conteiner_bot_deepfake")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.conteiner_bot_deepfake)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.botao_inicia_bot_deepnude = QtWidgets.QPushButton(self.conteiner_bot_deepfake)
        self.botao_inicia_bot_deepnude.setMinimumSize(QtCore.QSize(200, 42))
        self.botao_inicia_bot_deepnude.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_inicia_bot_deepnude.setObjectName("botao_inicia_bot_deepnude")
        self.horizontalLayout_10.addWidget(self.botao_inicia_bot_deepnude)
        self.bot_token = QtWidgets.QLineEdit(self.conteiner_bot_deepfake)
        self.bot_token.setMinimumSize(QtCore.QSize(0, 40))
        self.bot_token.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(85, 170, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.bot_token.setClearButtonEnabled(True)
        self.bot_token.setObjectName("bot_token")
        self.horizontalLayout_10.addWidget(self.bot_token)
        self.endereco_bot_api = QtWidgets.QLineEdit(self.conteiner_bot_deepfake)
        self.endereco_bot_api.setMinimumSize(QtCore.QSize(0, 40))
        self.endereco_bot_api.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(85, 170, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.endereco_bot_api.setClearButtonEnabled(True)
        self.endereco_bot_api.setObjectName("endereco_bot_api")
        self.horizontalLayout_10.addWidget(self.endereco_bot_api)
        self.verticalLayout_9.addWidget(self.conteiner_bot_deepfake)
        self.stackedWidget.addWidget(self.bot_deepfake)
        self.browser = QtWidgets.QWidget()
        self.browser.setObjectName("browser")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.browser)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.browser)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.voltar_site = QtWidgets.QPushButton(self.frame_2)
        self.voltar_site.setMinimumSize(QtCore.QSize(30, 40))
        self.voltar_site.setStyleSheet("QPushButton {\n"
"    background-image: url(:/volta_site/images/arrow-left.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.voltar_site.setText("")
        self.voltar_site.setObjectName("voltar_site")
        self.horizontalLayout_9.addWidget(self.voltar_site)
        self.atualiza_site = QtWidgets.QPushButton(self.frame_2)
        self.atualiza_site.setMinimumSize(QtCore.QSize(30, 40))
        self.atualiza_site.setStyleSheet("QPushButton {\n"
"    background-image: url(:/reload_site/images/reload.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.atualiza_site.setText("")
        self.atualiza_site.setObjectName("atualiza_site")
        self.horizontalLayout_9.addWidget(self.atualiza_site)
        self.avanca_site = QtWidgets.QPushButton(self.frame_2)
        self.avanca_site.setMinimumSize(QtCore.QSize(30, 40))
        self.avanca_site.setStyleSheet("QPushButton {\n"
"    background-image: url(:/avanca_site/images/arrow-right.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.avanca_site.setText("")
        self.avanca_site.setObjectName("avanca_site")
        self.horizontalLayout_9.addWidget(self.avanca_site)
        self.input_site = QtWidgets.QLineEdit(self.frame_2)
        self.input_site.setMinimumSize(QtCore.QSize(0, 30))
        self.input_site.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(85, 170, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.input_site.setObjectName("input_site")
        self.horizontalLayout_9.addWidget(self.input_site)
        self.botao_envia_site = QtWidgets.QPushButton(self.frame_2)
        self.botao_envia_site.setMinimumSize(QtCore.QSize(30, 45))
        self.botao_envia_site.setStyleSheet("QPushButton {\n"
"    background-image: url(:/avanca_site/images/arrow-right.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_envia_site.setText("")
        self.botao_envia_site.setObjectName("botao_envia_site")
        self.horizontalLayout_9.addWidget(self.botao_envia_site)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.web_browser = QtWebEngineWidgets.QWebEngineView(self.browser)
        self.web_browser.setObjectName("web_browser")
        self.verticalLayout_5.addWidget(self.web_browser)
        self.stackedWidget.addWidget(self.browser)
        self.python_console = QtWidgets.QWidget()
        self.python_console.setObjectName("python_console")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.python_console)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.area_consolepython = QtWidgets.QWidget(self.python_console)
        self.area_consolepython.setAutoFillBackground(False)
        self.area_consolepython.setStyleSheet("QWidget{\n"
"    \n"
"    background-color: rgb(15, 16, 16);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px Consolas, regular;\n"
"}")
        self.area_consolepython.setObjectName("area_consolepython")
        self.verticalLayout_10.addWidget(self.area_consolepython)
        self.stackedWidget.addWidget(self.python_console)
        self.banco_de_dados = QtWidgets.QWidget()
        self.banco_de_dados.setObjectName("banco_de_dados")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.banco_de_dados)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.barra_menus_banco_dados = QtWidgets.QFrame(self.banco_de_dados)
        self.barra_menus_banco_dados.setMinimumSize(QtCore.QSize(0, 300))
        self.barra_menus_banco_dados.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_menus_banco_dados.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_menus_banco_dados.setObjectName("barra_menus_banco_dados")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.barra_menus_banco_dados)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.conteiner_esquerda_db = QtWidgets.QFrame(self.barra_menus_banco_dados)
        self.conteiner_esquerda_db.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.conteiner_esquerda_db.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteiner_esquerda_db.setObjectName("conteiner_esquerda_db")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.conteiner_esquerda_db)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.db_texto_titulo = QtWidgets.QLineEdit(self.conteiner_esquerda_db)
        self.db_texto_titulo.setMinimumSize(QtCore.QSize(0, 40))
        self.db_texto_titulo.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(85, 170, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.db_texto_titulo.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.db_texto_titulo.setClearButtonEnabled(False)
        self.db_texto_titulo.setObjectName("db_texto_titulo")
        self.verticalLayout_15.addWidget(self.db_texto_titulo)
        self.db_texto_codigo = QtWidgets.QTextEdit(self.conteiner_esquerda_db)
        self.db_texto_codigo.setStyleSheet("QTextEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Courier New;\n"
"}\n"
"QTextEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QTextEdit:focus{\n"
"border: 2px solid  rgb(85, 170, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.db_texto_codigo.setOverwriteMode(False)
        self.db_texto_codigo.setPlaceholderText("")
        self.db_texto_codigo.setObjectName("db_texto_codigo")
        self.verticalLayout_15.addWidget(self.db_texto_codigo)
        self.horizontalLayout_17.addWidget(self.conteiner_esquerda_db)
        self.conteiner_direita_db = QtWidgets.QFrame(self.barra_menus_banco_dados)
        self.conteiner_direita_db.setMaximumSize(QtCore.QSize(400, 16777215))
        self.conteiner_direita_db.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conteiner_direita_db.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteiner_direita_db.setObjectName("conteiner_direita_db")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.conteiner_direita_db)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.db_texto_link = QtWidgets.QLineEdit(self.conteiner_direita_db)
        self.db_texto_link.setMinimumSize(QtCore.QSize(0, 40))
        self.db_texto_link.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(85, 170, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.db_texto_link.setObjectName("db_texto_link")
        self.verticalLayout_14.addWidget(self.db_texto_link)
        self.db_texto_observacao = QtWidgets.QTextEdit(self.conteiner_direita_db)
        self.db_texto_observacao.setMaximumSize(QtCore.QSize(16777215, 250))
        self.db_texto_observacao.setStyleSheet("QTextEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Courier New;\n"
"}\n"
"QTextEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QTextEdit:focus{\n"
"border: 2px solid  rgb(85, 170, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.db_texto_observacao.setObjectName("db_texto_observacao")
        self.verticalLayout_14.addWidget(self.db_texto_observacao)
        self.conteiner_menus_db = QtWidgets.QFrame(self.conteiner_direita_db)
        self.conteiner_menus_db.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conteiner_menus_db.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteiner_menus_db.setObjectName("conteiner_menus_db")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.conteiner_menus_db)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.botao_db_adiciona = QtWidgets.QPushButton(self.conteiner_menus_db)
        self.botao_db_adiciona.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_db_adiciona.setObjectName("botao_db_adiciona")
        self.horizontalLayout_18.addWidget(self.botao_db_adiciona)
        self.botao_db_atualiza = QtWidgets.QPushButton(self.conteiner_menus_db)
        self.botao_db_atualiza.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_db_atualiza.setObjectName("botao_db_atualiza")
        self.horizontalLayout_18.addWidget(self.botao_db_atualiza)
        self.botao_db_deleta = QtWidgets.QPushButton(self.conteiner_menus_db)
        self.botao_db_deleta.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_db_deleta.setObjectName("botao_db_deleta")
        self.horizontalLayout_18.addWidget(self.botao_db_deleta)
        self.verticalLayout_14.addWidget(self.conteiner_menus_db)
        self.horizontalLayout_17.addWidget(self.conteiner_direita_db)
        self.verticalLayout_13.addWidget(self.barra_menus_banco_dados)
        self.conteiner_dados_db = QtWidgets.QFrame(self.banco_de_dados)
        self.conteiner_dados_db.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conteiner_dados_db.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteiner_dados_db.setObjectName("conteiner_dados_db")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.conteiner_dados_db)
        self.horizontalLayout_16.setContentsMargins(9, 0, 9, 9)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.tabela_dados_db = QtWidgets.QTableView(self.conteiner_dados_db)
        self.tabela_dados_db.setStyleSheet("QHeaderView {\n"
"background: rgb(30, 30, 30);\n"
"}\n"
"QHeaderView::section{\n"
"    color: rgb(255, 255, 255);\n"
"background: rgb(35,35,35);\n"
"}\n"
"QTableCornerButton::section{\n"
"background: rgb(35,35,35);\n"
"}\n"
"QHeaderView::section:pressed{\n"
"background: rgb(30,144,255);\n"
"}\n"
"QTableCornerButton::section:pressed{\n"
"background: rgb(30,144,255);\n"
"}\n"
"\n"
"\n"
"\n"
"QTableView{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QTableView:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QTableView:focus{\n"
"border: 2px solid  rgb(85, 170, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}\n"
"* { gridline-color: gray }")
        self.tabela_dados_db.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tabela_dados_db.setGridStyle(QtCore.Qt.SolidLine)
        self.tabela_dados_db.setObjectName("tabela_dados_db")
        self.tabela_dados_db.horizontalHeader().setDefaultSectionSize(150)
        self.horizontalLayout_16.addWidget(self.tabela_dados_db)
        self.verticalLayout_13.addWidget(self.conteiner_dados_db)
        self.stackedWidget.addWidget(self.banco_de_dados)
        self.botManicomio = QtWidgets.QWidget()
        self.botManicomio.setObjectName("botManicomio")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.botManicomio)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.conteiner_topo_manicomiobot = QtWidgets.QFrame(self.botManicomio)
        self.conteiner_topo_manicomiobot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.conteiner_topo_manicomiobot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteiner_topo_manicomiobot.setObjectName("conteiner_topo_manicomiobot")
        self.img_bot_manicomio = QtWidgets.QLabel(self.conteiner_topo_manicomiobot)
        self.img_bot_manicomio.setGeometry(QtCore.QRect(40, 140, 300, 300))
        self.img_bot_manicomio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.img_bot_manicomio.setStyleSheet("QLabel{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 0px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLabel:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLabel:focus{\n"
"border: 2px solid  rgb(85, 170, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.img_bot_manicomio.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.img_bot_manicomio.setText("")
        self.img_bot_manicomio.setPixmap(QtGui.QPixmap("images/crowley.png"))
        self.img_bot_manicomio.setScaledContents(True)
        self.img_bot_manicomio.setAlignment(QtCore.Qt.AlignCenter)
        self.img_bot_manicomio.setObjectName("img_bot_manicomio")
        self.textBrowser_bot_manicomio = QtWidgets.QTextBrowser(self.conteiner_topo_manicomiobot)
        self.textBrowser_bot_manicomio.setGeometry(QtCore.QRect(400, 140, 391, 300))
        self.textBrowser_bot_manicomio.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.textBrowser_bot_manicomio.setObjectName("textBrowser_bot_manicomio")
        self.logo_bot_manicomio = QtWidgets.QLabel(self.conteiner_topo_manicomiobot)
        self.logo_bot_manicomio.setGeometry(QtCore.QRect(220, 20, 301, 101))
        self.logo_bot_manicomio.setText("")
        self.logo_bot_manicomio.setPixmap(QtGui.QPixmap("images/logo_manicomio.png"))
        self.logo_bot_manicomio.setScaledContents(True)
        self.logo_bot_manicomio.setObjectName("logo_bot_manicomio")
        self.verticalLayout_16.addWidget(self.conteiner_topo_manicomiobot)
        self.rodape_bot_manicomio = QtWidgets.QFrame(self.botManicomio)
        self.rodape_bot_manicomio.setMaximumSize(QtCore.QSize(16777215, 50))
        self.rodape_bot_manicomio.setFrameShape(QtWidgets.QFrame.Panel)
        self.rodape_bot_manicomio.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rodape_bot_manicomio.setObjectName("rodape_bot_manicomio")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.rodape_bot_manicomio)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.bot_token_manicomio = QtWidgets.QLineEdit(self.rodape_bot_manicomio)
        self.bot_token_manicomio.setMinimumSize(QtCore.QSize(0, 40))
        self.bot_token_manicomio.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(85, 170, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.bot_token_manicomio.setClearButtonEnabled(True)
        self.bot_token_manicomio.setObjectName("bot_token_manicomio")
        self.horizontalLayout_19.addWidget(self.bot_token_manicomio)
        self.bot_canalid_manicomio = QtWidgets.QLineEdit(self.rodape_bot_manicomio)
        self.bot_canalid_manicomio.setMinimumSize(QtCore.QSize(0, 40))
        self.bot_canalid_manicomio.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(85, 170, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.bot_canalid_manicomio.setClearButtonEnabled(True)
        self.bot_canalid_manicomio.setObjectName("bot_canalid_manicomio")
        self.horizontalLayout_19.addWidget(self.bot_canalid_manicomio)
        self.bot_idpessoal_manicomio = QtWidgets.QLineEdit(self.rodape_bot_manicomio)
        self.bot_idpessoal_manicomio.setMinimumSize(QtCore.QSize(0, 40))
        self.bot_idpessoal_manicomio.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(85, 170, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.bot_idpessoal_manicomio.setClearButtonEnabled(True)
        self.bot_idpessoal_manicomio.setObjectName("bot_idpessoal_manicomio")
        self.horizontalLayout_19.addWidget(self.bot_idpessoal_manicomio)
        self.verticalLayout_16.addWidget(self.rodape_bot_manicomio)
        self.botao_inicia_bot_manicomio = QtWidgets.QPushButton(self.botManicomio)
        self.botao_inicia_bot_manicomio.setMinimumSize(QtCore.QSize(200, 42))
        self.botao_inicia_bot_manicomio.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_inicia_bot_manicomio.setObjectName("botao_inicia_bot_manicomio")
        self.verticalLayout_16.addWidget(self.botao_inicia_bot_manicomio)
        self.stackedWidget.addWidget(self.botManicomio)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(330, 122, 321, 151))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.rodape = QtWidgets.QFrame(self.janela_central)
        self.rodape.setMinimumSize(QtCore.QSize(0, 17))
        self.rodape.setStyleSheet("background-color: rgb(31, 31, 31);")
        self.rodape.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.rodape.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rodape.setObjectName("rodape")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.rodape)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.rodape_desenvolvedor = QtWidgets.QLabel(self.rodape)
        self.rodape_desenvolvedor.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(98, 103, 111);\n"
"font: 10px ,Segoe UI;\n"
"margin-right: 5px;\n"
"}\n"
"\n"
"")
        self.rodape_desenvolvedor.setObjectName("rodape_desenvolvedor")
        self.horizontalLayout_7.addWidget(self.rodape_desenvolvedor)
        self.rodape_versao = QtWidgets.QLabel(self.rodape)
        self.rodape_versao.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(98, 103, 111);\n"
"font: 10px ,Segoe UI;\n"
"margin-right: 5px;\n"
"}\n"
"\n"
"")
        self.rodape_versao.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rodape_versao.setObjectName("rodape_versao")
        self.horizontalLayout_7.addWidget(self.rodape_versao)
        self.redimensionador = QtWidgets.QFrame(self.rodape)
        self.redimensionador.setMaximumSize(QtCore.QSize(20, 20))
        self.redimensionador.setStyleSheet("QSizeGrip {\n"
"    \n"
"    background-image: url(:/redimensiona/images/cil-move.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"}")
        self.redimensionador.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.redimensionador.setFrameShadow(QtWidgets.QFrame.Raised)
        self.redimensionador.setObjectName("redimensionador")
        self.horizontalLayout_7.addWidget(self.redimensionador)
        self.verticalLayout_4.addWidget(self.rodape)
        self.horizontalLayout.addWidget(self.janela_central)
        self.verticalLayout.addWidget(self.conteiner_central)
        MainWindow.setCentralWidget(self.janela_pai)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Manicomio Pannel"))
        self.texto_menu_home.setText(_translate("MainWindow", "home"))
        self.texto_menu_browser.setText(_translate("MainWindow", "browser"))
        self.texto_menu_python.setText(_translate("MainWindow", "python"))
        self.texto_menu_server_deepfake.setText(_translate("MainWindow", "server deep fake"))
        self.texto_menu_database.setText(_translate("MainWindow", "database"))
        self.texto_menu_bot1.setText(_translate("MainWindow", "chatbot\'s"))
        self.texto_menu_bot2.setText(_translate("MainWindow", "deep nude"))
        self.texto_menu_bot3.setText(_translate("MainWindow", "manicomio"))
        self.texto_menu_camera1.setText(_translate("MainWindow", "camera"))
        self.texto_menu_camera2.setText(_translate("MainWindow", "camera"))
        self.texto_menu_camera3.setText(_translate("MainWindow", "deep fake"))
        self.texto_menu_camera4.setText(_translate("MainWindow", "recognition"))
        self.texto_menu_camera5.setText(_translate("MainWindow", "face recognition"))
        self.status.setText(_translate("MainWindow", "infos"))
        self.status_pagina_atual.setText(_translate("MainWindow", "| home"))
        self.botao_iniciar_deepnude.setText(_translate("MainWindow", "deepfake bot"))
        self.botao_iniciar_botmanicomio.setText(_translate("MainWindow", "manicomio bot"))
        self.botao_iniciar_recognition.setText(_translate("MainWindow", "recognition"))
        self.botao_iniciar_server.setText(_translate("MainWindow", "server"))
        self.botao_iniciar_facerecog.setText(_translate("MainWindow", "face recog"))
        self.botao_iniciar_browser.setText(_translate("MainWindow", "browser"))
        self.botao_iniciar_camera.setText(_translate("MainWindow", "camera"))
        self.botao_iniciar_configuracoes.setText(_translate("MainWindow", "configs"))
        self.botao_iniciar_bancodados.setText(_translate("MainWindow", "database"))
        self.camera_local.setText(_translate("MainWindow", "camera local"))
        self.camera_droidcam.setText(_translate("MainWindow", "droidcam"))
        self.botao_inica_video.setText(_translate("MainWindow", "iniciar video"))
        self.botao_bate_foto.setText(_translate("MainWindow", "bater foto"))
        self.botao_imagem_deepnude.setText(_translate("MainWindow", "carregar imagem"))
        self.botao_criar_deepnude.setText(_translate("MainWindow", "deep fake"))
        self.camera_local_recognition.setText(_translate("MainWindow", "camera local"))
        self.camera_droidcam_recognition.setText(_translate("MainWindow", "droidcam"))
        self.botao_recognition_pessoas.setText(_translate("MainWindow", "face recognition"))
        self.botao_recognition_completo.setText(_translate("MainWindow", "recognition full"))
        self.camera_local_facerecognition.setText(_translate("MainWindow", "camera local"))
        self.camera_droidcam_facerecognition.setText(_translate("MainWindow", "droidcam"))
        self.botao_inica_facerecognition.setText(_translate("MainWindow", "face recognition"))
        self.inicia_server_deepnude.setText(_translate("MainWindow", "start"))
        self.endereco_localhost.setText(_translate("MainWindow", "localhost"))
        self.endereco_ngrok.setText(_translate("MainWindow", "ngrok"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Deep Nudes</span><span style=\" font-size:11pt;\"> são </span><span style=\" font-size:11pt; font-style:italic;\">fakes de nudes</span><span style=\" font-size:11pt;\"> que eu crio usando </span><span style=\" font-size:11pt; font-style:italic;\">Deep Learning</span><span style=\" font-size:11pt;\"> e </span><span style=\" font-size:11pt; font-style:italic;\">Machine Learning</span><span style=\" font-size:11pt;\">.<br /></span><span style=\" font-size:11pt; font-style:italic;\">Devido este processo ser longo e consumir muito processamento!!!</span><span style=\" font-size:11pt;\"><br /></span><span style=\" font-size:11pt; font-weight:600;\">Agora quero que preste atenção:</span><span style=\" font-size:11pt;\"><br />- o processo todo pode levar ate 10 minutos!<br />- nem sempre estou online, afinal isto é muito pesado!<br />- irei avisando ao longo do processo ate entregar a imagem!<br /></span><span style=\" font-size:11pt; font-weight:600;\">Como usar meus serviços:</span><span style=\" font-size:11pt;\"><br />- apenas faça um upload de uma imagem e espere!<br />- só reconheço imagens de biquini ou roupas intimas!<br />- preste atenção na imagem de exemplo!<br />- reconheço imagens somente como exemplo mostrado!<br />- fique a vontade para testar com imagens fora do contexto do exemplo...</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\"><br /></span><span style=\" font-size:11pt; font-weight:600;\">========================================</span><span style=\" font-size:11pt;\"><br />Conteudo criado apenas para fins academicos, não nos responsabilizamos pelo que aqui é criado ou postado!</span></p></body></html>"))
        self.botao_inicia_bot_deepnude.setText(_translate("MainWindow", "start"))
        self.bot_token.setText(_translate("MainWindow", "insira o token bot"))
        self.endereco_bot_api.setText(_translate("MainWindow", "aguarde link api json"))
        self.input_site.setText(_translate("MainWindow", "https://"))
        self.db_texto_titulo.setText(_translate("MainWindow", "titulo"))
        self.db_texto_codigo.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier New\'; font-size:15px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:15px;\">codigo</span></p></body></html>"))
        self.db_texto_link.setText(_translate("MainWindow", "link"))
        self.db_texto_observacao.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier New\'; font-size:15px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:15px;\">observações</span></p></body></html>"))
        self.botao_db_adiciona.setText(_translate("MainWindow", "adiciona"))
        self.botao_db_atualiza.setText(_translate("MainWindow", "atualiza"))
        self.botao_db_deleta.setText(_translate("MainWindow", "deleta"))
        self.textBrowser_bot_manicomio.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Bot Manicomio</span><br /><span style=\" font-size:16pt; vertical-align:super;\">desenvolvido para plataforma telegram</span><br /><span style=\" font-size:10pt; font-weight:600;\">comandos</span><span style=\" font-size:10pt;\"> - mostra todos comandos</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">start </span><span style=\" font-size:10pt;\">- inicia o bot</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">pin </span><span style=\" font-size:10pt;\">- Fixa uma mensagem no grupo(apenas admins)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">unpin </span><span style=\" font-size:10pt;\">- Desfixa a mensagem fixada no grupo(apenas admins)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">title</span><span style=\" font-size:10pt;\"> - Define o titulo do grupo(apenas admins)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">defregras</span><span style=\" font-size:10pt;\"> - define regras(apenas admins)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">ban</span><span style=\" font-size:10pt;\">- bane usuario(apenas admins)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">unban</span><span style=\" font-size:10pt;\"> - Desbane um usuario(apenas admins)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">mute </span><span style=\" font-size:10pt;\">- muta usuario(apenas admins)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">unmute</span><span style=\" font-size:10pt;\"> - Desrestringe um usuario(apenas admins)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">warn </span><span style=\" font-size:10pt;\">- Adverte um usuario(apenas admins)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">welcome </span><span style=\" font-size:10pt;\">- Define a mensagem de welcome(apenas admins)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">unwarn </span><span style=\" font-size:10pt;\">- Remove as advertencias do usuario(apenas admins)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">kick</span><span style=\" font-size:10pt;\"> - kicka usuario(apenas admins)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">regras</span><span style=\" font-size:10pt;\"> - ve as regras</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">config </span><span style=\" font-size:10pt;\">- informacoes serao enviadas no privado</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">admdebu</span><span style=\" font-size:10pt;\">g -  debug do admin</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">tr </span><span style=\" font-size:10pt;\">- Traduz um texto</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">yt </span><span style=\" font-size:10pt;\">- Pesquisa videos no YouTube</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">ytdl</span><span style=\" font-size:10pt;\"> - Baixa o audio de um video no YouTube</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">r</span><span style=\" font-size:10pt;\"> - pesquisa um termo no redit</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">coub</span><span style=\" font-size:10pt;\"> - Pesquisa de pequenas animacoes</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">dados</span><span style=\" font-size:10pt;\"> - jogo de dados</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">gif</span><span style=\" font-size:10pt;\"> - gif do giphy</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">git</span><span style=\" font-size:10pt;\"> - usuario do github</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">id</span><span style=\" font-size:10pt;\"> - id do usuario</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">ip</span><span style=\" font-size:10pt;\"> - informa dados de um ip</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">jsondump</span><span style=\" font-size:10pt;\"> - retorna dados formatados</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">stickerid</span><span style=\" font-size:10pt;\"> - pega id de um sticker</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">getsticker</span><span style=\" font-size:10pt;\"> - baixa um sticker(apenas admins)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">criar_sticker </span><span style=\" font-size:10pt;\">- cria um pacote de stickers(apenas admins)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">kibar  </span><span style=\" font-size:10pt;\">- copia um sticker para o pacote de stickers(apenas admins)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">pypi</span><span style=\" font-size:10pt;\"> - pesquisa libs python</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">rextester</span><span style=\" font-size:10pt;\"> - interpretador de varias linguagens de programa??o</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">mark</span><span style=\" font-size:10pt;\"> - Repete o texto informado usando Markdown</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">html </span><span style=\" font-size:10pt;\">- Repete o texto informado usando HTML</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">request </span><span style=\" font-size:10pt;\">- Faz uma requisicao a um site</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">site </span><span style=\" font-size:10pt;\">- exibe o site da equipe</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">facebook</span><span style=\" font-size:10pt;\"> - exibe o facebook da equipe, cadastre-se</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">netflix </span><span style=\" font-size:10pt;\">- exibe nosso site de netflix gratis</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">iptv </span><span style=\" font-size:10pt;\">- exibe nosso site de iptv gratis</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">anime</span><span style=\" font-size:10pt;\"> - exibe nosso site de anime gratis</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">pkg </span><span style=\" font-size:10pt;\">- exibe nosso site de pkg\'s para ps3 gratis</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">biblioteca</span><span style=\" font-size:10pt;\"> - exibe nossa biblioteca hacker</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">curso</span><span style=\" font-size:10pt;\"> - exibe nosso site de  cursos</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">doadores</span><span style=\" font-size:10pt;\"> - exibe instruces completas para doadores</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">painel </span><span style=\" font-size:10pt;\">- exibe nosso painel hacker</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">ban</span><span style=\" font-size:10pt;\"> - Bane um usuario(apenas admins)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">config</span><span style=\" font-size:10pt;\"> - Envia um menu de configuracoes(apenas admins)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">defregras</span><span style=\" font-size:10pt;\"> - Define as regras do grupo(apenas admins)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">kick </span><span style=\" font-size:10pt;\">- Kicka um inscrito(apenas admins)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">mute</span><span style=\" font-size:10pt;\"> - Restringe um usuario(apenas admins)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">coub</span><span style=\" font-size:10pt;\"> - Pesquisa de pequenas animacoes</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">echo</span><span style=\" font-size:10pt;\"> - Repete o texto informado</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">gif </span><span style=\" font-size:10pt;\">- Pesquisa de GIFs</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">git </span><span style=\" font-size:10pt;\">- Envia informaces de um user do GitHub</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">html</span><span style=\" font-size:10pt;\"> - Repete o texto informado usando HTML</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">ip </span><span style=\" font-size:10pt;\">- Exibe informaces sobre um IPdominio</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">jsondump</span><span style=\" font-size:10pt;\"> - Envia o json da mensagem</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">mark </span><span style=\" font-size:10pt;\">- Repete o texto informado usando Markdown</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">print</span><span style=\" font-size:10pt;\"> - Envia uma print de um site</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">pypi</span><span style=\" font-size:10pt;\"> - Pesquisa de modulos no PyPI</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">r</span><span style=\" font-size:10pt;\"> - Pesquisa de topicos no Reddit</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">request</span><span style=\" font-size:10pt;\"> - Faz uma requisicao a um site</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">shorten </span><span style=\" font-size:10pt;\">- Encurta uma URL</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">token</span><span style=\" font-size:10pt;\"> - Exibe informaces de um token de bot</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">tr </span><span style=\" font-size:10pt;\">- Traduz um texto</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">yt </span><span style=\" font-size:10pt;\">- Pesquisa v?deos no YouTube</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">ytdl </span><span style=\" font-size:10pt;\">- Baixa o ?udio de um v?deo no YouTube</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">admins </span><span style=\" font-size:10pt;\">- Mostra a lista de admins do chat</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">dados </span><span style=\" font-size:10pt;\">- Envia um numero aleatorio de 1 a 6</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">bug</span><span style=\" font-size:10pt;\"> - Reporta um bug ao meu desenvolvedor</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">id</span><span style=\" font-size:10pt;\"> - Exibe suas informaces ou de um usuario</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">ping </span><span style=\" font-size:10pt;\">- Responde com uma mensagem de ping</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">regras</span><span style=\" font-size:10pt;\"> - Exibe as regras do grupo</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">roleta</span><span style=\" font-size:10pt;\"> - Para jogar a Roleta Russa</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">backup</span><span style=\" font-size:10pt;\"> - Faz backup do bot(apenas dev)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">cmd</span><span style=\" font-size:10pt;\"> - Executa um comando(apenas dev)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">chat</span><span style=\" font-size:10pt;\"> - Obtem infos de um chat(apenas dev)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">del</span><span style=\" font-size:10pt;\"> - Deleta a mensagem respondida(apenas dev)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">doc</span><span style=\" font-size:10pt;\"> - Envia um documento do server(apenas dev)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">eval</span><span style=\" font-size:10pt;\"> - Executa uma função Python(apenas dev)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">exec </span><span style=\" font-size:10pt;\">- Executa um código Python(apenas dev)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">leave</span><span style=\" font-size:10pt;\"> - O bot sai do chat(apenas dev)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">plist </span><span style=\" font-size:10pt;\">- Lista os plugins ativos(apenas dev)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">promote</span><span style=\" font-size:10pt;\"> - Promove alguém a admin(apenas dev)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">restart</span><span style=\" font-size:10pt;\"> - Reinicia o bot(apenas dev)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">upgrade</span><span style=\" font-size:10pt;\"> - Atualiza a base do bot(apenas dev)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">upload</span><span style=\" font-size:10pt;\"> - Envia um arquivo para o servidor(apenas dev)</span></p></body></html>"))
        self.bot_token_manicomio.setText(_translate("MainWindow", "insira o token do bot"))
        self.bot_canalid_manicomio.setText(_translate("MainWindow", "insira id do canal do bot"))
        self.bot_idpessoal_manicomio.setText(_translate("MainWindow", "insira sua id do telegram"))
        self.botao_inicia_bot_manicomio.setText(_translate("MainWindow", "start"))
        self.label_2.setText(_translate("MainWindow", "configs"))
        self.rodape_desenvolvedor.setText(_translate("MainWindow", "manicomio | 2020"))
        self.rodape_versao.setText(_translate("MainWindow", "v1.0  "))
from PyQt5 import QtWebEngineWidgets
import files_rc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
