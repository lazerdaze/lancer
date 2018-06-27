import sys
from Qt import QtCore, QtWidgets, QtGui

app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton("Hello World")
button.show()
app.exec_()

