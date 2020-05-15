import sys
from threading import Thread
from PyQt5.QtWidgets import QApplication

from pyqtconsole.console import PythonConsole

app = QApplication([])
console = PythonConsole()
console.show()
console.eval_in_thread()

sys.exit(app.exec_())