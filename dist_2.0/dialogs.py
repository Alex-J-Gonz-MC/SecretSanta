import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class addDialog(QDialog):
    def __init__(self,main):
        super(addDialog,self).__init__()
        loadUi('add_edit_dialog.ui',self)
        self.homePage = main
        self.addToListButton.clicked.connect(self.addToList)
        self.cancelButton.clicked.connect(self.close)
    def addToList(self):
        text = str(self.lineEdit.text())
        name = ""
        email = ""
        for i in range(len(text)):
            if text[i] == ",":
                name = text[:i].strip()
                email = text[i+1:].strip()
                break
        self.homePage.listWidget.addItem("{},\t {}".format(name,email))
        self.close()

class editDialog(QDialog):
    def __init__(self,main):
        super(editDialog,self).__init__()
        loadUi('add_edit_dialog.ui',self)
        self.homePage = main
        self.addToListButton.clicked.connect(self.editListItem)
        self.cancelButton.clicked.connect(self.close)
        currentText = self.homePage.listWidget.currentItem().text()
        for i in range(len(currentText)):
            if currentText[i] == ",":
                name = currentText[:i].strip()
                email = currentText[i+1:].strip()
                currentText = "{}, {}".format(name,email)
                break
        self.lineEdit.setText(currentText)
    def editListItem(self):
        text = str(self.lineEdit.text())
        name = ""
        email = ""
        for i in range(len(text)):
            if text[i] == ",":
                name = text[:i].strip()
                email = text[i+1:].strip()
                break
        self.homePage.listWidget.currentItem().setText("{},\t {}".format(name,email))
        self.close()

class sendDialog(QDialog):
    def __init__(self,main):
        super(sendDialog,self).__init__()
        loadUi('send_dialog.ui',self)
        self.homePage = main
        self.sendButton.clicked.connect(self.send_matches)
    def send_matches(self):
        from send_functions import distributeSantas
        participants = []
        for index in range(self.homePage.listWidget.count()):
            participants.append([x.strip() for x in self.homePage.listWidget.item(index).text().split(',')])
        server = self.serverEdit.text().strip()
        email = self.emailEdit.text().strip()
        password = self.passwordEdit.text()
        distributeSantas(participants,server,email,password)
        self.close()
