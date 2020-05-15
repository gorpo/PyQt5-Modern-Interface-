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


# Funções minimizar maximizar e fechar personalizadas---------------------->
def fecharPrograma(self):
    sys.exit()

def minimizarPrograma(self):
    window.showMinimized()

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
    self.window.showMaximized()

    #self.ui.botao_maximizar.clicked.connect(self.janela_normal)

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
    window.showNormal()
    self.ui.botao_maximizar.clicked.connect(self.maximizarPrograma)

