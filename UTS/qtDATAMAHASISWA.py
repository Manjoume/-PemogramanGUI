# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtDATAMAHASISWA.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from uts1 import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 587)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 40, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(90, 70, 371, 241))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 330, 311, 16))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 330, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 350, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 370, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 350, 311, 16))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 370, 311, 16))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 390, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 390, 311, 16))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 410, 61, 23))
        
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pushButtonTambah)
    
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 410, 61, 23))

        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.pushButtonEdit)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 410, 61, 23))

        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 410, 61, 23))

        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.pushButtonHapus)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Data Mahasiswa"))
        self.label_2.setText(_translate("MainWindow", "NIM "))
        self.label_3.setText(_translate("MainWindow", "Nama "))
        self.label_4.setText(_translate("MainWindow", "Jurusan"))
        self.label_5.setText(_translate("MainWindow", "No.Telp"))
        self.pushButton.setText(_translate("MainWindow", "TAMBAH"))
        self.pushButton_2.setText(_translate("MainWindow", "EDIT"))
        self.pushButton_3.setText(_translate("MainWindow", "CLEAR"))
        self.pushButton_4.setText(_translate("MainWindow", "HAPUS"))

        def pushButtontambah(self):
        self.listView.addItem(
            self.nimEdit.text() + ' - ' +
            self.namaEdit.text() + ' - ' +
            self.jurusanEdit.text() + ' - ' +
            self.notelpEdit.text())

        def pushButtonEdit(self):
        if self.listView.currentRow() < 0: return
        self.uts1 = pushButtonEdit ()
        s = str(self.listView.currentItem().text())
        idx = s.index('-')
        self.uts1.nim.setText(s[:(idx - 1)])
        self.uts1.nama.setText(s[(idx - 2):])
        self.uts1.jurusan.setText(s[(idx - 3):])
        self.uts1.telp.setText(s[(idx - 4):])

        if self.uts1.exec_() == QDialog.Accepted:
            self.listView.currentItem().setText(
                self.uts1.nim.text() + ' - ' +
                self.uts1.nama.text() + ' - ' +
                self.uts1.jurusan.text() + ' - ' +
                self.uts1.telp.text())

    def pushButtonHapus(self):
        row = self.listView.currentRow()
        if row >= 0:
            self.listView.takeItem(row)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

