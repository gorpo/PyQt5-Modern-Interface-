
[![Build](https://img.shields.io/badge/dev-gorpo-brightgreen.svg)]()
[![Stage](https://img.shields.io/badge/Release-Stable-brightgreen.svg)]()
[![Build](https://img.shields.io/badge/python-v3.7-blue.svg)]()
[![Build](https://img.shields.io/badge/windows-7%208%2010-blue.svg)]()
[![Build](https://img.shields.io/badge/Linux-Ubuntu%20Debian-orange.svg)]()
[![Build](https://img.shields.io/badge/arquiterura-64bits-blue.svg)]()<br>
  <h6 align="center">
   <img src="https://raw.githubusercontent.com/gorpo/Manicomio-Boot-Theme/master/manicomio/boot.png" width="55%"></img>
       <h2 align="center">Manicomio |PyQt5 Modern Interface v1.0 | Deep Learning | Machine Learning</h2>
  </h6>
<h3>Simples e facil interface grafica feita com Qt Design + PyQt5</h3><br>
<img src="https://raw.githubusercontent.com/gorpo/PyQt5-Modern-Interface-/master/images/examples/01.jpg" width="100%"></img>
<p>Este programa conta com alguns exemplos de programação prontas, mas seu foco é ajudar as pessoas com sua interface amigavel e de facil compreensão. Além do magnifico layout este programa conta com a manipulação de imagens com OpenCV, Torch, Torchvision, Numpy e Pillow, sistema de camera integrada com reconhecimento facial, reconhecimento de objetos e pessoas além de um servidor flask e sistema de banco de dados ele disponibiliza em sua source um bot com a base do Telepot! O sistema de manipulação de imagem que cria imagens *** seguindo um padrão especifico, pois faz a leitura e treinamento com arquivos .lib, os quais devem ser feitos o download e inseridos posteriormente na pasta /checkpoints.</p>

# Requisitos:
- Python3.7 (não testado em outros)
- OpenCV
- Torch
- Torchvision
- Numpy
- Pyllow
- Face Recognition
- Telepot
- PyQt5
- Outras lib's ver arquivos ou logs de erro
- Subistitua a API do telegram no arquivo main.py

# Instalações previas das libs que cumprem os requisitos para windows10:<br>
--> Torch:<br>
<code>pip install https://download.pytorch.org/whl/cu90/torch-1.1.0-cp37-cp37m-win_amd64.whl</code><br>
-->Torchvision<br>
<code>pip install https://download.pytorch.org/whl/cu90/torchvision-0.3.0-cp37-cp37m-win_amd64.whl </code><br>
--> Pillow<br>
<code>pip install Pillow==6.1</code><br>
--> OpenCV<br>
<code>pip install opencv-python</code><br>
--> Numpy<br>
<code>pip install numpy</code><br>
--> Numpy<br>
<code>pip install numpy</code><br>
--> OpenCV<br>
<code>https://docs.opencv.org/master/d5/de5/tutorial_py_setup_in_windows.html</code><br>
--> OpenCV Tutorial<br>
<code>https://cv-tricks.com/how-to/installation-of-opencv-4-1-0-in-windows-10-from-source/</code><br>
--> Face Recognition<br>
*install windows https://github.com/ageitgey/face_recognition/issues/175#issue-257710508  <br>
<code>https://github.com/ageitgey/face_recognition</code><br>
--> PyQt Console<br>
<code>pip install pyqtconsole</code><br>
--> CMake<br>
<code>https://cmake.org/</code><br>
--> Atualize seu Setup Tools<br>
<code>pip install --upgrade setuptools</code>
--> Visual Studio<br>
* Referencia: https://stackoverflow.com/questions/29846087/microsoft-visual-c-14-0-is-required-unable-to-find-vcvarsall-bat
<code>https://www.visualstudio.com/downloads/#build-tools-for-visual-studio-2017</code>


# Lib's adicionais e obrigatórias:
<p> Precisamos adicionar os arquivos cm.lib, mm.lib e mn.lib dentro da pasta "/checkpoints", para isto basta fazer o download abaixo de cada uma delas, ou caso contrario o script não irá rodar e irá apresentar o seguinte erro:</p>
---> Iremos ter o erro:<br>
<code>FileNotFoundError: [Errno 2] No such file or directory: 'checkpoints/cm.lib'
libpng warning: iCCP: known incorrect sRGB profile</code>
--correção:<br>
	--> Por os arquivos abaixo na pasta checkpoints:<br>
CM lib>> https://drive.google.com/file/d/1wNo3Rjd_F4I8kh25HZ0rfnfRcBy5wept/view<br>
MM lib>> https://drive.google.com/file/d/15fylXbJYqXbmfKoo-KX2SpvYGtlMcITE/view<br>
Mn lib>> https://drive.google.com/file/d/1VWwc8TQcPgUlE_MVZm0je1xn3MeCiuJ_/view<br>

# Executando:
<p>Após ter todas as Lib's instaladas basta rodar o arquivo main.py e usasr a interface grafica.</p>


# Editando:
<p>Todos arquivos editaveis estão com este material, dentre eles o arquivo mainwindow.ui para ser editado no Qt Design e arquivos photoshop com imagens que foram usadas neste projeto. Todas funções foram colocadas em arquivos separados para facil compreensão e o widget central que mostra as telas chama-se: stackedWidget.<br>As cores e estilos foram feitos todos em CSS dentro do arquivo mainwindow.ui do QT Design mas podem ser alterados no arquivo mainwindow.py tranquilamente!</p>
 # Comandos para serem executados no teminal ou cmd para gerar os arquivos python feitos no QT Design:
 <p>criar arquivo mainwindow.py:<br>
    <code>pyuic5 -x mainwindow.ui -o mainwindow.py</code><br>
criar arquivo files_rc_rc.py<br>
    <code>pyrcc5 -o files_rc_rc.py files_rc.qrc</code></p>
    
 # Tempo de execução:
 <p>O tempo de execução de todo processo e qualidade varia de maquina para maquina, este script usa duas formas para fazer seue processo, ou uso da Memoria Ram ou uso da GPU. Para acelerar o processo aconselho uso de GPU porém ira se comportar tranquilamente com uso da memoria ram.

 # Demonstração do layout e algumas funções:
 <h2 align="center">PAINEL NORMAL</h2>
<img src="https://raw.githubusercontent.com/gorpo/PyQt5-Modern-Interface-/master/images/examples/01.jpg" width="100%"></img>
 <h2 align="center">MENU ESQUERDA E SUBMENUS COM SUBMENUS</h2>
<img src="https://raw.githubusercontent.com/gorpo/PyQt5-Modern-Interface-/master/images/examples/02.jpg" width="100%"></img>
 <h2 align="center">"MENU INICIAR COM SUBMENUS"</h2>
<img src="https://raw.githubusercontent.com/gorpo/PyQt5-Modern-Interface-/master/images/examples/03.jpg" width="100%"></img>
 <h2 align="center">WEB BROWSER INTEGRADO FEITO EM PYTHON</h2>
<img src="https://raw.githubusercontent.com/gorpo/PyQt5-Modern-Interface-/master/images/examples/browser.jpg" width="100%"></img>
 <h2 align="center">INTERPRETADOR PYTHON FEITO EM PYTHON</h2>
<img src="https://raw.githubusercontent.com/gorpo/PyQt5-Modern-Interface-/master/images/examples/python.jpg" width="100%"></img>
 <h2 align="center">SERVIDOR FLASK INTEGRADO</h2>
<img src="https://raw.githubusercontent.com/gorpo/PyQt5-Modern-Interface-/master/images/examples/flask.jpg" width="100%"></img>
 <h2 align="center">BANCO DE DADOS INTEGRADO FEITO COM SQLITE3</h2>
<img src="https://raw.githubusercontent.com/gorpo/PyQt5-Modern-Interface-/master/images/examples/bancodedados.jpg" width="100%"></img>


 <h2 align="center">OUTRAS FERRAMENTAS SERÃO LANÇADAS NA VERSAO 2.0</h2>


