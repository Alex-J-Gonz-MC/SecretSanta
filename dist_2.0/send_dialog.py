# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 338)
        Dialog.setStyleSheet("background-color:aliceblue;")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 20, 381, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border:none;")
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.serverEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serverEdit.sizePolicy().hasHeightForWidth())
        self.serverEdit.setSizePolicy(sizePolicy)
        self.serverEdit.setStyleSheet("background-color:white;")
        self.serverEdit.setObjectName("serverEdit")
        self.verticalLayout.addWidget(self.serverEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border:none;")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.emailEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emailEdit.sizePolicy().hasHeightForWidth())
        self.emailEdit.setSizePolicy(sizePolicy)
        self.emailEdit.setStyleSheet("background-color:white;")
        self.emailEdit.setObjectName("emailEdit")
        self.verticalLayout.addWidget(self.emailEdit)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border:none;")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.passwordEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordEdit.sizePolicy().hasHeightForWidth())
        self.passwordEdit.setSizePolicy(sizePolicy)
        self.passwordEdit.setStyleSheet("background-color:white;")
        self.passwordEdit.setObjectName("passwordEdit")
        self.verticalLayout.addWidget(self.passwordEdit)
        self.sendButton = QtWidgets.QPushButton(Dialog)
        self.sendButton.setGeometry(QtCore.QRect(140, 280, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sendButton.setFont(font)
        self.sendButton.setStyleSheet("background-color:steelblue;\n"
"border-radius:10px;")
        self.sendButton.setObjectName("sendButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit_5.setText(_translate("Dialog", "Server"))
        self.lineEdit_2.setText(_translate("Dialog", "Host Email"))
        self.lineEdit.setText(_translate("Dialog", "Host Password"))
        self.sendButton.setText(_translate("Dialog", "Send"))

