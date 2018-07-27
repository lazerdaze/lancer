# Running on Python 2.7, Pyside 2, Qt.py

import sys
from Qt import QtCore, QtWidgets, QtGui

app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton("Hello World")
button.show()
app.exec_()

