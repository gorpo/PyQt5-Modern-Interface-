#!/usr/bin/env python
# -*- coding: utf-8 -*-
#███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
#████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
#██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
#██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
#██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
#╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#            @GorpoOrko | Manicomio TCXS Project | 2020


from main import *


#funcoes principais-------------->
def menusJanela(self):
    funcoesJanela(self)
    menuEsquerda(self)
    menusCamera(self)
    menuBots(self)
    menuIniciar(self)

#funçoes extras ------------------>
def funcoesJanela(self):
    # sistema de redimensionamento da tela---------------->
    self.ui.botao_fechar.clicked.connect(lambda: sys.exit())
    self.ui.botao_maximizar.clicked.connect(lambda: maximizarPrograma(self))
    self.ui.botao_minimizar.clicked.connect(lambda: self.showMinimized())
    self.sizegrip = QSizeGrip(self.ui.redimensionador)
    self.sizegrip.setStyleSheet("width: 17px; height: 17px; margin 0px; padding: 0px;")
    self.sizegrip.setVisible(True)
def maximizarPrograma(self):
    self.ui.botao_maximizar.setStyleSheet("QPushButton {\n"
                                       "    \n"
                                       "    background-image: url('images/volta_full_screen.png');\n"
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
    self.showMaximized()
    self.ui.botao_maximizar.clicked.connect(lambda: janela_normal(self))
def janela_normal(self):
    self.ui.botao_maximizar.setStyleSheet("QPushButton {\n"
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
    self.showNormal()
    self.ui.botao_maximizar.clicked.connect(lambda: maximizarPrograma(self))

#abre/fecha menu esquerda--------->
def menuEsquerda(self):
    self.ui.botao_abrir_menu.clicked.connect(lambda: abreMenu(self))
    # botao homepage------------------------------------------>
    self.ui.botao_home.clicked.connect(lambda: paginaHome(self))
    # botao web browser---------------------------------------->
    self.ui.botao_browser.clicked.connect(lambda: paginaBrowser(self))
    #botao interpretador python
    self.ui.botao_python.clicked.connect(lambda: paginaPython(self))
    #botao database---------------------------------------------->
    self.ui.botao_database.clicked.connect(lambda: paginaDatabase(self))
    # botao server flask deep nude------------------------------->
    self.ui.botao_server_deepfake.clicked.connect(lambda: paginaServerDeepnude(self))
    # botao abre e fecha menu da camera----------------------->
    self.ui.botao_menu_camera1.clicked.connect(lambda: abreMenuCamera(self))
    #botao abre e fecha menu dos bots---------------------------->
    self.ui.botao_menu_bot1.clicked.connect(lambda: abreMenuBots(self))



def menuIniciar(self):
    self.ui.botao_iniciar_browser.clicked.connect(lambda: paginaBrowser(self))
    self.ui.botao_iniciar_server.clicked.connect(lambda: paginaServerDeepnude(self))
    self.ui.botao_iniciar_camera.clicked.connect(lambda : paginaCamera(self))
    self.ui.botao_iniciar_facerecog.clicked.connect(lambda: paginaFacerecognition(self))
    self.ui.botao_iniciar_recognition.clicked.connect(lambda: paginaRecognition(self))
    self.ui.botao_iniciar_deepnude.clicked.connect(lambda: paginaBotdeepnude(self))
    self.ui.botao_iniciar_bancodados.clicked.connect(lambda: paginaDatabase(self))
    self.ui.botao_iniciar_botmanicomio.clicked.connect(lambda: paginaBotmanicomio(self))
    self.ui.botao_iniciar_configuracoes.clicked.connect(lambda: paginaConfiguracoes(self))

def abreMenu(self):
    self.ui.menu_esquerda.setMinimumSize(QtCore.QSize(210, 0))
    self.ui.botao_abrir_menu.clicked.connect(lambda : fechaMenu(self))
def fechaMenu(self):
    self.ui.menu_esquerda.setMinimumSize(QtCore.QSize(50, 0))
    self.ui.botao_abrir_menu.clicked.connect(lambda : abreMenu(self))
#INDEXAÇÃO DAS PAGINAS------------->

#homepage ------------------------->
def paginaHome(self):
    self.ui.status.setText('bem vindo')
    self.ui.status_pagina_atual.setText('home')
    self.ui.stackedWidget.setCurrentIndex(0)
    self.ui.rodape.hide()
#browser--------------------------->
def paginaBrowser(self):
    self.ui.status_pagina_atual.setText('browser')
    self.ui.status.setText('navegador em python | digite um site para iniciar a pesquisa')
    self.ui.stackedWidget.setCurrentIndex(7)
    file = 'https://google.com'
    self.ui.web_browser.load(QtCore.QUrl(file))
    self.ui.rodape.show()
#pagina python--------------------->
def paginaPython(self):
    self.ui.status.setText('Python Interpreter | Interpretador python feito em python')
    self.ui.status_pagina_atual.setText('python')
    self.ui.stackedWidget.setCurrentIndex(8)
#pagina database------------------->
def paginaDatabase(self):
    self.ui.status_pagina_atual.setText('database')
    self.ui.status.setText('database sqlite3 python | salvo codigos dos mais variados neste pequeno servidor sqllite3')
    self.ui.stackedWidget.setCurrentIndex(9)
    self.ui.rodape.show()

#server flask deepnude------------->
def paginaServerDeepnude(self):
    self.ui.status_pagina_atual.setText('servidor')
    self.ui.status.setText('servidor flask python | inicie o servidor, serão fornecidos link localhost e ngrok')
    self.ui.stackedWidget.setCurrentIndex(5)
    file = 'https://flask.palletsprojects.com/en/1.1.x/'
    self.ui.web_browser_flask.load(QtCore.QUrl(file))
    self.ui.rodape.show()

#camera---------------------------->
def menusCamera(self):
    self.ui.botao_menu_camera2.clicked.connect(lambda: paginaCamera(self))
    self.ui.botao_menu_camera3.clicked.connect(lambda: paginaDeepfake(self))
    self.ui.botao_menu_camera4.clicked.connect(lambda: paginaRecognition(self))
    self.ui.botao_menu_camera5.clicked.connect(lambda: paginaFacerecognition(self))
def paginaCamera(self):
    self.ui.area_video.setPixmap(QtGui.QPixmap('images/bg_camera.png'))
    self.ui.status.setText('camera feita em open cv2 | salva fotos com o Image PIL (pillow)')
    self.ui.status_pagina_atual.setText('camera')
    self.ui.stackedWidget.setCurrentIndex(1)
    self.ui.rodape.show()
def abreMenuCamera(self):
    self.ui.texto_menu_camera1.setText("menu camera")
    self.ui.menus_camera.setGeometry(QtCore.QRect(0, 250, 250, 350))
    self.ui.botao_menu_camera1.clicked.connect(lambda: fechaMenuCamera(self))
def fechaMenuCamera(self):
    self.ui.texto_menu_camera1.setText("camera")
    self.ui.menus_camera.setGeometry(QtCore.QRect(0, 250, 250, 50))
    self.ui.botao_menu_camera1.clicked.connect(lambda: abreMenuCamera(self))
#deepfake--------------->
def paginaDeepfake(self):
    self.ui.status_pagina_atual.setText('deep fake')
    self.ui.status.setText('deep learning | manipulação de imagens com opencv pytorch numpy')
    self.ui.stackedWidget.setCurrentIndex(2)
    self.ui.rodape.show()
#recognition------------>
def paginaRecognition(self):
    self.ui.status_pagina_atual.setText('recognition')
    self.ui.status.setText('deep learning |sistema de reconhecimento baseado em machine learning')
    self.ui.stackedWidget.setCurrentIndex(3)
    self.ui.rodape.show()
#facerecognition-------->
def paginaFacerecognition(self):
    self.ui.status_pagina_atual.setText('face recognition')
    self.ui.status.setText('deep learning | reconhecimento de rostos com machine learning')
    self.ui.stackedWidget.setCurrentIndex(4)
    self.ui.rodape.show()

#bots--------------------------->
def menuBots(self):
    self.ui.botao_menu_bot2.clicked.connect(lambda: paginaBotdeepnude(self))
    self.ui.botao_menu_bot3.clicked.connect(lambda: paginaBotmanicomio(self))
def abreMenuBots(self):
    self.ui.texto_menu_bot1.setText("menu chatbot's")
    self.ui.menus_bots.setGeometry(QtCore.QRect(0, 300, 250, 350))
    self.ui.botao_menu_bot1.clicked.connect(lambda: fechaMenuBots(self))
def fechaMenuBots(self):
    self.ui.texto_menu_bot1.setText("chatbot's")
    self.ui.menus_bots.setGeometry(QtCore.QRect(0, 300, 250, 50))
    self.ui.botao_menu_bot1.clicked.connect(lambda: abreMenuBots(self))
def paginaBotdeepnude(self):
    self.ui.status.setText('Marcinho | python telegram chatbot  | gera deep fakes com machine learning e deep learning')
    self.ui.status_pagina_atual.setText('chatbot')
    self.ui.stackedWidget.setCurrentIndex(6)
def paginaBotmanicomio(self):
    self.ui.status.setText('Manicomio | python telegram chatbot  | um dos mais completos bots do telegram')
    self.ui.status_pagina_atual.setText('chatbot')
    self.ui.stackedWidget.setCurrentIndex(10)



#configuraçoes----------------------->
def paginaConfiguracoes(self):
    self.ui.status_pagina_atual.setText('configurações')
    self.ui.status.setText('area de treinamento | widgets e outros itens do qt designer')
    self.ui.stackedWidget.setCurrentIndex(11)
    self.ui.rodape.show()

















