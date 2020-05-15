#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
# ████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
# ██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
# ██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
# ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
# ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#            @GorpoOrko | Manicomio TCXS Project | 2020

import sys
from threading import Thread
from pyqtconsole.console import PythonConsole
import pyqtconsole.highlighter as hl
from PyQt5.QtWidgets import QApplication
from main import *
from PyQt5.QtCore import *


def mostraConsolePython(self):
    self.console = Consolepython(self.ui.area_consolepython)


def Consolepython(self):
    self.ui.rodape.show()
    console = PythonConsole(self.ui.area_consolepython,formats={
    'keyword':    hl.format('magenta', 'bold'),
    'operator':   hl.format('red'),
    'brace':      hl.format('DeepSkyBlue'),
    'defclass':   hl.format('green', 'bold'),
    'string':     hl.format('magenta'),
    'string2':    hl.format('darkMagenta'),
    'comment':    hl.format('DeepSkyBlue', 'italic'),
    'self':       hl.format('DeepSkyBlue', 'italic'),
    'numbers':    hl.format('white'),
    'inprompt':   hl.format('DeepSkyBlue', 'bold'),
    'outprompt':  hl.format('LimeGreen', 'bold'),
})
    console.resize(842,602)
    #self.console.setGeometry(QtCore.QRect(0, 0, 150, 125))
    console.show()
    console.eval_in_thread()


