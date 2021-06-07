from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit
from PyQt5.QtGui import QFont
import sys

class MyWindow(QMainWindow):

    got_operation = QtCore.pyqtSignal(str)

    def __init__(self):
        super(MyWindow, self).__init__()
        self.button_height = 70
        self.button_width = 120
        self.font = QFont('TimesNewRoman', 13)

        self.operation = ""

        self.setGeometry(900, 200, 3 * self.button_width, 2 * self.button_height)
        self.setWindowTitle("Programmer Calculator")
        self.initUI()

    def initUI(self):
        # First column

        self.text_box = QLineEdit(self)
        self.text_box.move(0, self.button_height + 30)
        self.text_box.setFont(QFont('TimesNewRoman', 16))
        self.text_box.setMaxLength(49)
        self.text_box.resize(5 * self.button_width, self.button_height)
        self.text_box.hide()


        self.b_and = QtWidgets.QPushButton(self)
        self.b_and.setText("AND")
        self.b_and.setFont(self.font)
        self.b_and.setGeometry(0, 0 * self.button_height, self.button_width, self.button_height)
        self.b_and.clicked.connect(lambda: self.clicked_button_operation("AND"))

        self.b_nand = QtWidgets.QPushButton(self)
        self.b_nand.setText("NAND")
        self.b_nand.setFont(self.font)
        self.b_nand.setGeometry(0, 1 * self.button_height, self.button_width, self.button_height)
        self.b_nand.clicked.connect(lambda: self.clicked_button_operation("NAND"))

        # Second column

        self.b_or = QtWidgets.QPushButton(self)
        self.b_or.setText("OR")
        self.b_or.setFont(self.font)
        self.b_or.setGeometry(1 * self.button_width, 0 * self.button_height, self.button_width, self.button_height)
        self.b_or.clicked.connect(lambda: self.clicked_button_operation("OR"))

        self.b_nor = QtWidgets.QPushButton(self)
        self.b_nor.setText("NOR")
        self.b_nor.setFont(self.font)
        self.b_nor.setGeometry(1 * self.button_width, 1 * self.button_height, self.button_width, self.button_height)
        self.b_nor.clicked.connect(lambda: self.clicked_button_operation("NOR"))

        # Third column

        self.b_not = QtWidgets.QPushButton(self)
        self.b_not.setText("NOT")
        self.b_not.setFont(self.font)
        self.b_not.setGeometry(2 * self.button_width, 0 * self.button_height, self.button_width, self.button_height)
        self.b_not.clicked.connect(lambda: self.clicked_button_operation("NOT"))

        self.b_xor = QtWidgets.QPushButton(self)
        self.b_xor.setText("XOR")
        self.b_xor.setFont(self.font)
        self.b_xor.setGeometry(2 * self.button_width, 1 * self.button_height, self.button_width, self.button_height)
        self.b_xor.clicked.connect(lambda: self.clicked_button_operation("XOR"))

        self.show()

    def clicked_button_operation(self, operation):  # Other operations
        self.got_operation.emit(operation)

