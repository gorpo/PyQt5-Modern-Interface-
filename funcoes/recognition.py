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

import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2
import numpy as np
import sys


def funcoesRecognition(self):
    self.ui.botao_recognition_pessoas.clicked.connect(lambda: visualizarPessoas(self))
    self.ui.botao_recognition_completo.clicked.connect(lambda: visualizarCompleto(self))




def visualizarPessoas(self):
    try:
        if self.ui.camera_local_recognition.isChecked():
            camera = 0
        if self.ui.camera_droidcam_recognition.isChecked():
            camera = 'http://192.168.0.4:4747/video'
        video = cv2.VideoCapture(camera)
        while video.isOpened():
            self.status, self.imagem = video.read()
            # apply face detection
            face, confidence = cv.detect_face(self.imagem)
            # loop through detected faces
            for idx, f in enumerate(face):
                (startX, startY) = f[0], f[1]
                (endX, endY) = f[2], f[3]
                # draw rectangle over face
                cv2.rectangle(self.imagem, (startX, startY), (endX, endY), (0, 255, 0), 2)
                text = "{:.2f}%".format(confidence[idx] * 100)
                Y = startY - 10 if startY - 10 > 10 else startY + 10
                # write confidence percentage on top of face rectangle
                cv2.putText(self.imagem, text, (startX, Y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)


            # display output
            self.imagem = cv2.cvtColor(self.imagem, cv2.COLOR_BGR2RGB)  # converte a imagem para as cores da camera
            height, width, channel = self.imagem.shape
            step = channel * width
            qImg = QImage(self.imagem.data, width, height, step, QImage.Format_RGB888)
            imagem_ajustada = QtGui.QPixmap.fromImage(qImg)
            self.imagem_aumentada = imagem_ajustada.scaledToHeight(600)
            self.ui.area_video_recognition.setAlignment(Qt.AlignCenter)
            self.ui.area_video_recognition.setPixmap(self.imagem_aumentada)
            # press "Q" to stop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # release resources
        video.release()
        cv2.destroyAllWindows()
    except:
        self.ui.area_video_recognition.setPixmap(QtGui.QPixmap('images/bg_camera_indisponivel.png'))
        pass


def visualizarCompleto(self):
    try:
        if self.ui.camera_local_recognition.isChecked():
            camera = 0
        if self.ui.camera_droidcam_recognition.isChecked():
            camera = 'http://192.168.0.4:4747/video'
        video = cv2.VideoCapture(camera)
        while video.isOpened():
            self.status, self.imagem = video.read()
            self.imagem = cv2.cvtColor(self.imagem, cv2.COLOR_BGR2RGB) #converte a imagem para as cores da camera
            #somente com as duas linhas abaixo ja chamamos o sistema de detecção, o qual pode ser trocado para idade ou para pessoa facilmente!
            bbox, label, conf = cv.detect_common_objects(self.imagem, confidence=0.25, model='yolov3')  # -tiny
            self.out = draw_bbox(self.imagem, bbox, label, conf, write_conf=True)
            # display output
            height, width, channel = self.imagem.shape
            step = channel * width
            qImg = QImage(self.imagem.data, width, height, step, QImage.Format_RGB888)
            imagem_ajustada = QtGui.QPixmap.fromImage(qImg)
            self.imagem_aumentada = imagem_ajustada.scaledToHeight(600)
            self.ui.area_video.setAlignment(Qt.AlignCenter)
            self.ui.area_video_recognition.setPixmap(self.imagem_aumentada)
            # press "Q" to stop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # release resources
        video.release()
        cv2.destroyAllWindows()
    except:
        self.ui.area_video_recognition.setPixmap(QtGui.QPixmap('images/bg_camera_indisponivel.png'))
        pass





