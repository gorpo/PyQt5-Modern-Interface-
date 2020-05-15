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
from funcoes import deepfake


def funcoesDeepfake(self):
    self.ui.botao_imagem_deepnude.clicked.connect(lambda: selecionarImagem(self))
    self.ui.botao_criar_deepnude.clicked.connect(lambda: ativaDeepNudes(self))

def selecionarImagem(self):
    self.imagem_recebida = []
    try:
        janela2 = QWidget()
        janela2.resize(800, 600)
        janela2.move(100, 200)
        janela2.setWindowTitle('Manicômio | Deep Nude')
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(janela2, "MANICOMIO | DEEP FAKE | Escolha sua imagem", "", "All Files (*);;JPG (*.jpg);;PNG (*.png)", options=options)
        if fileName:
            self.ui.imagem_normal_deepnude.setPixmap(QtGui.QPixmap(fileName).scaled(800, 450, QtCore.Qt.KeepAspectRatio))  # aumentar imagem com qtcore .scaled(200,200, QtCore.Qt.KeepAspectRatio)
            self.ui.imagem_renderizada_deepnude.setPixmap(QtGui.QPixmap('images/processando.png').scaled(300, 450, QtCore.Qt.KeepAspectRatio))  # aumentar imagem com qtcore .scaled(200,200, QtCore.Qt.KeepAspectRatio)
            if fileName in self.imagem_recebida:
                # print(fileName)
                # print(self.imagem_recebida)
                self.imagem_recebida.clear()
            else:
                # print(self.imagem_recebida)
                self.imagem_recebida.clear()
                self.imagem_recebida.append(fileName)
        # carrega na variavel do Image do pilow (PIL) a imagem aberta
        im1 = Image.open(self.imagem_recebida[0])
        # salva a imagem usando a extensao que quisermos
        im1 = im1.save("images/file.jpg")
    except:
        pass

def ativaDeepNudes(self):
    #subprocess.run('python deepfake.py', shell=True)
    #if __name__ == '__main__': nao precisa chamar assim se estiver dentro de uma funçao
    inputpath = 'images/file.jpg'
    outputpath = 'images/renderizada.jpg'
    deepfake.main(inputpath, outputpath)

    self.ui.imagem_renderizada_deepnude.setPixmap(QtGui.QPixmap('images/renderizada.jpg').scaled(800, 450,QtCore.Qt.KeepAspectRatio))  # aumentar imagem com qtcore .scaled(200,200, QtCore.Qt.KeepAspectRatio)
