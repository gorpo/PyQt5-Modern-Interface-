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
import subprocess
import time

def funcoesBotdeepnude(self):
    self.ui.botao_inicia_bot_deepnude.clicked.connect(lambda: ativaBot(self))



def ativaBot(self):
    if self.ui.bot_token.text() == 'insira o token bot':
        api = 'INSIRA SUA API'
        self.ui.bot_token.setText('Bot Ativado, confira o Telegram.')
        self.ui.endereco_bot_api.setText(f'https://api.telegram.org/bot{api}/getUpdates')  # seta o texto da variavel
        ler = open('funcoes/base_bot.txt', 'r')
        lido = ler.read()
        trocar = 'replace'
        gravacao = lido.replace(trocar,api)
        gravar = open('funcoes/bot.py', 'w')
        gravar.write(gravacao)
        ler.close()
        gravar.close()
        time.sleep(3)
        #abre o bot
        subprocess.Popen('python funcoes/bot.py', stdout=subprocess.PIPE)
    else:
        api = self.ui.bot_token.text()  # le oque foi escrito na caixa de texto
        api_stripada = api.strip()
        self.ui.bot_token.setText('Bot Ativado, confira o Telegram.')
        self.ui.endereco_bot_api.setText(f'https://api.telegram.org/bot{api}/getUpdates') # seta o texto da variavel
        # pega os dados em um documento de texto e cria o bot com a API
        ler = open('funcoes/base_bot.txt', 'r')
        lido = ler.read()
        trocar = 'replace'
        gravacao = lido.replace(trocar, api_stripada)
        gravar = open('funcoes/bot.py', 'w')
        gravar.write(gravacao)
        ler.close()
        gravar.close()
        time.sleep(3)
        # abre o bot
        subprocess.Popen('python funcoes/bot.py', stdout=subprocess.PIPE)