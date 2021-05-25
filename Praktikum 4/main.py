

import sys
from importUI import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*


class DemoQtDesainer(QDialog) :
    def _init_(self,parent = None) :
        QDialog. _init_(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.hallo.clicked.connect(self.halloClicked)
    
    def halloClicked(self):
        QMessageBox.information(self, 'Demo QtDesigner','Hallo %s, apa kabar?' % self.ui.namaEdit.text())

if _name_ == "_main_":
    a = QApplication(sys.argv)
    form = DemoQtDesainer()
    form.show()
    a.exec_()