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

def funcoesBotmanicomio(self):
    self.ui.botao_inicia_bot_manicomio.clicked.connect(lambda: ativaBot(self))


def ativaBot(self):
    if self.ui.bot_token_manicomio.text() == 'insira o token do bot' and self.ui.bot_canalid_manicomio.text() == 'insira id do canal do bot' and self.ui.bot_idpessoal_manicomio.text() == 'insira sua id do telegram':
        api = 'SUA API DO TELEGRAM'   #api crowley 1186597860:AAHZTQT--xYhNHhkO8SbxlSxrdwVnkvi38s  #api gorpobot 1096480409:AAH6LhyWjRBk4KUFxaDmb46Lr3CG3x0MpzA
        id_canal = '-100 ID DO CANAL APOS O -100' #COLOQUE NAS ASPAS A ID DO CANAL + -100 NA FRENTE
        id_usuario = 'SUA ID DE USUARIO DO TELEGRAM'
        self.ui.bot_token_manicomio.setText('Bot Ativado, confira o Telegram.')
        self.ui.bot_canalid_manicomio.setText('Logs serão enviados no canal')
        self.ui.bot_idpessoal_manicomio.setText(f'https://api.telegram.org/bot{api}/getUpdates')  # seta o texto da variavel
        ler = open('funcoes/base_bot_manicomio.txt', 'r')
        lido = ler.read()
        trocar_api = lido.replace('replace_api', api)
        trocar_canal = trocar_api.replace('replace_canal', id_canal)
        trocar_usuario = trocar_canal.replace('replace_usuario', id_usuario)
        gravar = open('funcoes/manicomio_bot/config.py', 'w')
        gravar.write(trocar_usuario)
        ler.close()
        gravar.close()
        time.sleep(3)
        #abre o bot
        subprocess.Popen('python funcoes/manicomio_bot/manicomio.py', stdout=subprocess.PIPE)
    else:
        api = self.ui.bot_token_manicomio.text()  # le oque foi escrito na caixa de texto
        api_stripada = api.strip()
        id_canal = self.ui.bot_canalid_manicomio.text()
        id_canal_stripada = id_canal.strip()
        id_usuario = self.ui.bot_idpessoal_manicomio.text()
        id_usuario_stripada = id_usuario.strip()
        self.ui.bot_token_manicomio.setText('Bot Ativado, confira o Telegram.')
        self.ui.bot_canalid_manicomio.setText('Logs serão enviados no canal')
        self.ui.bot_idpessoal_manicomio.setText( f'https://api.telegram.org/bot{api}/getUpdates')  # seta o texto da variavel
        ler = open('funcoes/base_bot_manicomio.txt', 'r')
        lido = ler.read()
        trocar_api = lido.replace('replace_api', api_stripada)
        trocar_canal = trocar_api.replace('replace_canal', id_canal_stripada)
        trocar_usuario = trocar_canal.replace('replace_usuario', id_usuario_stripada)
        gravar = open('funcoes/manicomio_bot/config.py', 'w')
        gravar.write(trocar_usuario)
        ler.close()
        gravar.close()
        time.sleep(3)
        # abre o bot
        subprocess.Popen('python funcoes/manicomio_bot/manicomio.py', stdout=subprocess.PIPE)


