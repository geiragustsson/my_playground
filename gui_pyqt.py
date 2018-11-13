"""
Inspired by:
https://pythonspot.com/gui/
"""

import sys
from PyQt5.QtWidgets import QInputDialog, QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 menu - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        mainMenu = self.menuBar() 
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        searchMenu = mainMenu.addMenu('Search')
        toolsMenu = mainMenu.addMenu('Tools')
        helpMenu = mainMenu.addMenu('Help')
 
        # Title bar
        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        # Input dialogs
        #self.getInteger()
        #self.getText()
        #self.getDouble()
        #self.getChoice()

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
 
        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20,60)
 
        # Connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
 
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")
 
    def getInteger(self):
        i, okPressed = QInputDialog.getInt(self, "Get integer","Percentage:", 28, 0, 100, 1)
        if okPressed:
            print(i)
 
    def getDouble(self):
        d, okPressed = QInputDialog.getDouble(self, "Get double","Value:", 10.50, 0, 100, 10)
        if okPressed:
            print( d)
 
    def getChoice(self):
        items = ("Red","Blue","Green")
        item, okPressed = QInputDialog.getItem(self, "Get item","Color:", items, 0, False)
        if okPressed and item:
            print(item)
 
    def getText(self):
        text, okPressed = QInputDialog.getText(self, "Get text","Your name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            print(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())