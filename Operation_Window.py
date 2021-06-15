from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5.QtGui import QFont


class Operation_Window(QMainWindow):

    got_operation = QtCore.pyqtSignal(str)

    def __init__(self):
        """
        Konstruktor
        """
        super(Operation_Window, self).__init__()
        self.button_height = 70
        self.button_width = 120
        self.font = QFont('TimesNewRoman', 13)

        self.operation = ""

        self.setGeometry(900, 200, 4 * self.button_width, 1 * self.button_height)
        self.setWindowTitle("Operation Window")
        self.initUI()

    def initUI(self):
        """
        Funkcja odpowiedzialna za tworzenie interfejsu graficznego.
        :return:
        """

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

        # Second column

        self.b_or = QtWidgets.QPushButton(self)
        self.b_or.setText("OR")
        self.b_or.setFont(self.font)
        self.b_or.setGeometry(1 * self.button_width, 0 * self.button_height, self.button_width, self.button_height)
        self.b_or.clicked.connect(lambda: self.clicked_button_operation("OR"))

        # Third column

        self.b_not = QtWidgets.QPushButton(self)
        self.b_not.setText("NOT")
        self.b_not.setFont(self.font)
        self.b_not.setGeometry(2 * self.button_width, 0 * self.button_height, self.button_width, self.button_height)
        self.b_not.clicked.connect(lambda: self.clicked_button_operation("NOT"))

        self.b_xor = QtWidgets.QPushButton(self)
        self.b_xor.setText("XOR")
        self.b_xor.setFont(self.font)
        self.b_xor.setGeometry(3 * self.button_width, 0 * self.button_height, self.button_width, self.button_height)
        self.b_xor.clicked.connect(lambda: self.clicked_button_operation("XOR"))

    def clicked_button_operation(self, operation):  # Other operations
        """
        Funkcja odpowiedzialna za zwrócenie wartości wyrażenia.
        :param operation:
        :return:
        """
        self.got_operation.emit(operation)

