from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFont
from PyQt5.QtCore import *
import Standard_Expression
import sys

import Scientific_GUI
import Programmer_GUI
import Standard_GUI

import Converter_Expression


class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.button_height = 70
        self.button_width = 120
        self.font = QFont('TimesNewRoman', 13)

        self.result = ""
        self.experssion = ""

        self.from_operation = ""
        self.to_operation = ""

        self.first_use = True

        self.setGeometry(200, 200, 4 * self.button_width, 9 * self.button_height - 10)
        self.setWindowTitle("Calculator")
        self.initUI()

    def initUI(self):
        self.b_sta = QtWidgets.QPushButton(self)
        self.b_sta.setText("Standard")
        self.b_sta.setFont(self.font)
        self.b_sta.setGeometry(0, 0, 160, self.button_height)
        self.b_sta.clicked.connect(self.go_standard_calculator)

        self.b_sci = QtWidgets.QPushButton(self)
        self.b_sci.setText("Scientific")
        self.b_sci.setFont(self.font)
        self.b_sci.setGeometry(160, 0, 160, self.button_height)
        self.b_sci.clicked.connect(self.go_scientific_calculator)

        self.b_prog = QtWidgets.QPushButton(self)
        self.b_prog.setText("Programmer")
        self.b_prog.setFont(self.font)
        self.b_prog.setGeometry(320, 0, 160, self.button_height)
        self.b_prog.clicked.connect(self.go_programmer_calculator)

        self.text_label = QtWidgets.QLabel(self)
        self.text_label.setText("Input:")
        self.text_label.setFont(self.font)
        self.text_label.move(0, self.button_height)

        self.text_box = QtWidgets.QLineEdit(self)
        self.text_box.move(0, self.button_height + 30)
        self.text_box.setFont(QFont('TimesNewRoman', 16))
        self.text_box.setMaxLength(49)
        self.text_box.resize(4 * self.button_width, self.button_height)

        self.result_label = QtWidgets.QLabel(self)
        self.result_label.setText("Output:")
        self.result_label.setFont(self.font)
        self.result_label.move(0, 2 * self.button_height + 30)

        self.result_box = QtWidgets.QLineEdit(self)
        self.result_box.move(0, 2 * self.button_height + 60)
        self.result_box.setFont(QFont('TimesNewRoman', 16))
        self.result_box.setMaxLength(49)
        self.result_box.resize(4 * self.button_width, self.button_height)
        self.result_box.setDisabled(True)
        # First column

        self.bw = 40
        self.bh = 320

        self.from_label = QtWidgets.QLabel(self)
        self.from_label.setText("From:")
        self.from_label.setFont(self.font)
        self.from_label.move(self.bw + 10, self.bh - 40)

        self.hex_box_g = QtWidgets.QPushButton(self)
        self.hex_box_g.setText("HEX")
        self.hex_box_g.setFont(self.font)
        self.hex_box_g.setGeometry(self.bw, self.bh, self.button_width, self.button_height)
        self.hex_box_g.clicked.connect(lambda: self.set_from_operation("16"))

        self.dec_box_g = QtWidgets.QPushButton(self)
        self.dec_box_g.setText("DEC")
        self.dec_box_g.setFont(self.font)
        self.dec_box_g.setGeometry(self.bw, self.bh + self.button_height, self.button_width, self.button_height)
        self.dec_box_g.clicked.connect(lambda: self.set_from_operation("10"))

        self.oct_box_g = QtWidgets.QPushButton(self)
        self.oct_box_g.setText("OCT")
        self.oct_box_g.setFont(self.font)
        self.oct_box_g.setGeometry(self.bw, self.bh + 2 * self.button_height, self.button_width, self.button_height)
        self.oct_box_g.clicked.connect(lambda: self.set_from_operation("8"))

        self.bin_box_g = QtWidgets.QPushButton(self)
        self.bin_box_g.setText("BIN")
        self.bin_box_g.setFont(self.font)
        self.bin_box_g.setGeometry(self.bw, self.bh + 3 * self.button_height, self.button_width, self.button_height)
        self.bin_box_g.clicked.connect(lambda: self.set_from_operation("2"))

        # Second column
        self.bw += 280

        self.to_label = QtWidgets.QLabel(self)
        self.to_label.setText("To:")
        self.to_label.setFont(self.font)
        self.to_label.move(self.bw + 10, self.bh - 40)

        self.hex_box_r = QtWidgets.QPushButton(self)
        self.hex_box_r.setText("HEX")
        self.hex_box_r.setFont(self.font)
        self.hex_box_r.setGeometry(self.bw, self.bh, self.button_width, self.button_height)
        self.hex_box_r.clicked.connect(lambda: self.set_to_operation("16"))

        self.dec_box_r = QtWidgets.QPushButton(self)
        self.dec_box_r.setText("DEC")
        self.dec_box_r.setFont(self.font)
        self.dec_box_r.setGeometry(self.bw, self.bh + self.button_height, self.button_width, self.button_height)
        self.dec_box_r.clicked.connect(lambda: self.set_to_operation("10"))

        self.oct_box_r = QtWidgets.QPushButton(self)
        self.oct_box_r.setText("OCT")
        self.oct_box_r.setFont(self.font)
        self.oct_box_r.setGeometry(self.bw, self.bh + 2 * self.button_height, self.button_width, self.button_height)
        self.oct_box_r.clicked.connect(lambda: self.set_to_operation("8"))

        self.bin_box_r = QtWidgets.QPushButton(self)
        self.bin_box_r.setText("BIN")
        self.bin_box_r.setFont(self.font)
        self.bin_box_r.setGeometry(self.bw, self.bh + 3 * self.button_height, self.button_width, self.button_height)
        self.bin_box_r.clicked.connect(lambda: self.set_to_operation("2"))

        self.b_convert = QtWidgets.QPushButton(self)
        self.b_convert.setText("CONVERT")
        self.b_convert.setFont(QFont('TimesNewRoman', 15))
        self.b_convert.setGeometry(self.bw - 160, self.bh, self.button_width + 40, self.button_height)
        self.b_convert.clicked.connect(lambda: self.clicked_button_convert())

        self.show()

    def go_standard_calculator(self):
        self.new_window = Standard_GUI.MyWindow()
        self.new_window.show()
        self.close()

    def go_scientific_calculator(self):
        self.new_window = Scientific_GUI.MyWindow()
        self.new_window.show()
        self.close()

    def go_programmer_calculator(self):
        self.new_window = Programmer_GUI.MyWindow()
        self.new_window.show()
        self.close()

    def set_from_operation(self, arg):
        self.from_operation = arg

    def set_to_operation(self, arg):
        self.to_operation = arg

    def clicked_button_convert(self):

        self.experssion = self.text_box.text()
        self.experssion = self.experssion.upper()

        if self.first_use == True:
            self.new_class = Converter_Expression.Expression(self.experssion, self.from_operation,self.to_operation)
            self.new_class.translate_expression()
            self.experssion = self.new_class.get_expression()
            self.experssion = self.experssion[2::]
            self.first_use = False

        elif self.first_use == False:

            self.new_class.update(self.experssion, self.from_operation,self.to_operation)
            self.new_class.translate_expression()
            self.experssion = self.new_class.get_expression()
            self.experssion = self.experssion[2::]

        self.result_box.setText(self.experssion)
        self.result_box.setDisabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
