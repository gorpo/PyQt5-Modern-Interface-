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

def funcoesCamera(self):
    # cria um timer para segurar o video parado, assim pude definir um botao de inicio e pausa
    self.timer = QTimer()
    self.timer.timeout.connect(lambda: visualizarCamera(self))
    self.ui.botao_inica_video.clicked.connect(lambda: controleTimer(self))
    self.ui.botao_bate_foto.clicked.connect(lambda: bateFoto(self))



def visualizarCamera(self):
    try:
        self.ret, self.image = self.cap.read()
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB) #converte a imagem para as cores da camera
        height, width, channel = self.image.shape
        step = channel * width
        qImg = QImage(self.image.data, width, height, step, QImage.Format_RGB888)
        imagem = QtGui.QPixmap.fromImage(qImg)
        self.imagem_aumentada = imagem.scaledToHeight(650)
        self.ui.area_video.setAlignment(Qt.AlignCenter)
        self.ui.area_video.setPixmap(self.imagem_aumentada)
    except:
        self.ui.area_video.setPixmap(QtGui.QPixmap('images/bg_camera_indisponivel.png'))
        pass

def controleTimer(self):
    if not self.timer.isActive():
        try:
            if self.ui.camera_local.isChecked():
                camera = 0
            if self.ui.camera_droidcam.isChecked():
                camera = 'http://192.168.0.4:4747/mjpegfeed'
            self.cap = cv2.VideoCapture(camera) #'http://localhost:4747/mjpegfeed'
            self.timer.start(20)
            self.ui.botao_inica_video.setText("parar video")
        except:
            pass
    else:
        self.timer.stop()
        self.cap.release()
        self.ui.botao_inica_video.setText("iniciar video")


def bateFoto(self):
    try:
        janela4 = QWidget()
        janela4.resize(800, 600)
        janela4.move(100, 200)
        options = QFileDialog.Options()
        fileName = QFileDialog.getSaveFileName(janela4, "MANICOMIO | DEEP FAKE | Salvar sua imagem", "captura", "JPG (*.jpg);;PNG (*.png)", options=options)
        self.imagem_filtrada = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB) #passa o filtro mais uma vez para desfazer ele e deixar a imagem normal
        cv2.imwrite(filename=fileName[0], img=self.imagem_filtrada)
    except:
        pass