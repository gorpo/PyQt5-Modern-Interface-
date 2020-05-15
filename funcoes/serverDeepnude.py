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
from pyngrok import ngrok
import subprocess
import time

def funcoesServerDeepnude(self):
    self.sdp = self.ui.inicia_server_deepnude.clicked.connect(lambda: serverFlask(self))

def serverFlask(self):
    subprocess.Popen('python funcoes/deepnude_flask/deepnude_flask.py', stdout=subprocess.PIPE)
    time.sleep(3)
    self.ui.web_browser_flask.load(QtCore.QUrl('http://127.0.0.1:5000/'))
    link_ngrok = ngrok.connect(5000)
    print(f'Link compartilhavel: {link_ngrok}')
    self.ui.endereco_localhost.setText('http://127.0.0.1:5000/')
    self.ui.endereco_ngrok.setText(f'{link_ngrok}')

