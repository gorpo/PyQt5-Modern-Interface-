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


def funcoesWindowsSO(self):
    self.ui.botao_menu_iniciar.clicked.connect(lambda: abreMenuIniciar(self))


def abreMenuIniciar(self):
    #self.ui.menu_iniciar_aberto.setMinimumSize(QtCore.QSize(281, 251))
    self.ui.menu_iniciar_aberto.setGeometry(QtCore.QRect(0, 340, 281, 261))
    self.ui.botao_menu_iniciar.clicked.connect(lambda: fechaMenuIniciar(self))


def fechaMenuIniciar(self):
    self.ui.menu_iniciar_aberto.setGeometry(QtCore.QRect(0, 340, 0, 0))
    self.ui.botao_menu_iniciar.clicked.connect(lambda: abreMenuIniciar(self))