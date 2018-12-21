
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QGridLayout, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton)
import sys

def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

class MainWindow(QWidget):
    """
    Original: http://d.hatena.ne.jp/mFumi/20141112/1415806010
    Adapted from: https://stackoverflow.com/questions/44096507/pyqt5-create-list-of-qlineedit

    """


    def __init__(self, input_dic, parent=None):
        super(MainWindow, self).__init__(parent)

        self.input_dic = input_dic

        lineLayout = QGridLayout()
        mainLayout = QHBoxLayout()

        c = 0

        for inpkey in input_dic:

            if input_dic[inpkey]["type"] == "info":
                continue

            elif input_dic[inpkey]["type"] == "input":

                input_dic[inpkey]["input_id"] = c
                
                input_name = input_dic[inpkey]["description"]
                input_unit = input_dic[inpkey]["unit"]
                input_field = input_name + "[" + input_unit + "]"

                self.inputLine = QLineEdit()
                lineLayout.addWidget(QLabel(input_field), 0+c, 0)
                lineLayout.addWidget(self.inputLine, 0+c, 1)
                mainLayout.addLayout(lineLayout)

                c += 1
        
        print(input_dic)

        self.setLayout(mainLayout)
        self.setWindowTitle(input_dic["Project"]["name"])

    def access_widget(inpkey):
        
        item = layout.itemAtPosition(int)
        line_edit = item.widget()
        return line_edit


def StartProgram(input_dic):
    app = QApplication(sys.argv)
    main_window = MainWindow(input_dic)

    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':

    d = {}
    d["Project"] = {}
    d["Project"] = {
        "name":"Beta project", 
        "description": "Trying stuff out", 
        "type":"info"}

    d["Length"] = {}
    d["Length"] = {
        "format":float, 
        "unit":"m", 
        "description": "Input length", 
        "type":"input"}

    d["Weight"] = {}
    d["Weight"] = {
        "format":float, 
        "unit":"m", 
        "description": "Input weight", 
        "type":"input"}

    d["Include sheath"] = {}
    d["Include sheath"] = {
        "format":bool, 
        "unit": "-",
        "description": "Whether (1) or not (0) to include sheath", 
        "type":"input"}

    StartProgram(d)