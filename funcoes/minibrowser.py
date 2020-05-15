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


def funcoesBrowser(self):
    self.ui.botao_envia_site.clicked.connect(lambda: navegador(self))
    self.ui.input_site.returnPressed.connect(lambda: navegador(self))  # faz o botao enter enviar
    self.ui.voltar_site.clicked.connect(self.ui.web_browser.back)
    self.ui.avanca_site.clicked.connect(self.ui.web_browser.forward)
    self.ui.atualiza_site.clicked.connect(self.ui.web_browser.reload)

def navegador(self):
    site = self.ui.input_site.text()
    self.ui.web_browser.load(QtCore.QUrl(site))

