# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_edit_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(466, 198)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 100, 421, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 30, 421, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setLineWidth(0)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.plainTextEdit.setBackgroundVisible(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.addToListButton = QtWidgets.QPushButton(Dialog)
        self.addToListButton.setGeometry(QtCore.QRect(80, 150, 131, 31))
        self.addToListButton.setObjectName("addToListButton")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(260, 150, 131, 31))
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.plainTextEdit.setDocumentTitle(_translate("Dialog", "Add/Edit Participant"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "Enter the name and email of the participant below, respectively, seperating them with a comma. \n"
"Ex: (Santa Claus, sclaus@northpole.org)"))
        self.addToListButton.setText(_translate("Dialog", "Add Participant"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))

