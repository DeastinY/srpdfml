import os
import sys
import configparser
from pdf_parser import parse
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMessageBox, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QPushButton, QLineEdit, QLabel


class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.config = configparser.ConfigParser()
        self.config_file = 'config.ini'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createLayout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox, 1)
        windowLayout.addWidget(self.contentArea, 100)
        self.setLayout(windowLayout)
        self.readConfig()

        self.show()

    
    def createLayout(self):
        self.horizontalGroupBox = QGroupBox("Enter the search query")
        layout = QHBoxLayout()
 
        self.lineEdit = QLineEdit(self)
        layout.addWidget(self.lineEdit)
 
        #self.buttonSearch = QPushButton('Search', self)
        #self.buttonSearch.clicked.connect(self.mousePressEvent)
        #self.lineEdit.returnPressed.connect(self.buttonSearch.click)
        self.lineEdit.textChanged.connect(self.search)
        #layout.addWidget(self.buttonSearch)
 
        self.horizontalGroupBox.setLayout(layout)
        self.contentArea = QLabel(self)

    def mousePressEvent(self, event):
        if self.sender() == self.buttonSearch:
            self.search()

    def search(self):
        print(self.lineEdit.text())

    def readConfig(self):
        if not os.path.exists(self.config_file):
            self.config['GENERAL'] = {}
            self.config['GENERAL']['RulebookLocation'] = self.openPdfDialog()
            with open(self.config_file, 'w') as confout:
                self.config.write(confout)
        self.config.read(self.config_file)

 
    def openPdfDialog(self):    
        QMessageBox.question(self, "Process rulebooks", "Not set up yet. Select directory containing PDF files to process. This may take up to 5 minutes", QMessageBox.Ok)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        directoryName = QFileDialog.getExistingDirectory(self, options=options)
        if directoryName:
            return directoryName

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())