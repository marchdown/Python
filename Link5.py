import sys
from PyQt4 import QtCore, QtGui, uic

form_class = uic.loadUiType("Link5.ui")[0]                 # Load the UI

class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        for i in range(20):
            for j in range(20):
                self.cellClicked (i+1,j+1).connect(self.cell_clicked)  # Bind the event handlers

        for i in range(20):
            for j in range(20):
                self.cellDoubleClicked (i+1,j+1).connect(self.cell_double_clicked)

    def cell_clicked(self,int,int):             # Cell i j clicked event handler
                                                # Set image or whatever


    def cell_double_clicked(self,int,int)       



app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()