import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QFileDialog
from PyQt5.uic import loadUi

class MainPage(QMainWindow):
    def __init__(self):
        super(MainPage,self).__init__()
        loadUi('secretsanta.ui',self)
        self.addButton.clicked.connect(self.addParticipant)
        self.removeButton.clicked.connect(self.removeParticipant)
        self.editButton.clicked.connect(self.editParticipant)
        self.sendButton.clicked.connect(self.sendEmails)
        self.loadFromCSV_Button.triggered.connect(self.loadCSV)
        self.saveToCSV_Button.triggered.connect(self.saveCSV)
    def addParticipant(self):
        #print("here")
        from dialogs import addDialog
        dialogbox = addDialog(self)
        dialogbox.exec_()
    def removeParticipant(self):
        item = self.listWidget.currentItem()
        if not item: return
        self.listWidget.takeItem(self.listWidget.row(item))
    def editParticipant(self):
        from dialogs import editDialog
        dialogbox = editDialog(self)
        dialogbox.exec_()
    def sendEmails(self):
        from dialogs import sendDialog
        dialogbox = sendDialog(self)
        dialogbox.exec_()
    def loadCSV(self):
        import csv
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Load From CSV","C:\\\\","Comma Separated Value files (*.csv)")
        if fileName:
            with open(fileName, mode='r') as csv_file:
                csv_reader = csv.reader(csv_file,delimiter=',')
                for row in csv_reader:
                    self.listWidget.addItem("{},\t {}".format(row[0],row[1]))
    def saveCSV(self):
        import csv
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Save To CSV","C:\\\\","Comma Separated Value files (*.csv)")
        if fileName:
            with open(fileName, mode='w') as csv_file:
                csv_writer = csv.writer(csv_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
                for index in range(self.listWidget.count()):
                    csv_writer.writerow([x.strip() for x in self.listWidget.item(index).text().split(',')])





app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())
