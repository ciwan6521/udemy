# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets,QtGui

def pencere():
    
    app = QtWidgets.QApplication(sys.argv)
    
    pencere = QtWidgets.QWidget()
    
    pencere.setWindowTitle("PyQt5 Ders 1")
    etiket1 = QtWidgets.QLabel(pencere)
    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("python.png"))
    etiket1.setText("Hello Naber")
    etiket1.move(200,30)
    etiket2.move(70,100)
    pencere.setGeometry(100,100,500,500)
    
    pencere.show()
    
    sys.exit(app.exec_())
    
pencere()






