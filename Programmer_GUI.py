from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QApplication
from PyQt5.QtGui import QFont


import Scientific_GUI
import Standard_GUI
import Converter_GUI

import Operation_Window
import Programmer_Expression


class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.button_height = 70
        self.button_width = 120
        self.font = QFont('TimesNewRoman', 13)

        self.result = ""
        self.experssion = ""
        self.ans_val = ""
        self.system = ""
        self.first_use = False

        self.operation_window = Operation_Window.MyWindow()
        self.operation_window.got_operation.connect(self.set_operation)

        self.setGeometry(200, 200, 5 * self.button_width, 10 * self.button_height)
        self.setWindowTitle("Programmer Calculator")
        self.initUI()

    def initUI(self):
        self.text_box = QLineEdit(self)
        self.text_box.move(0, self.button_height + 30)
        self.text_box.setFont(QFont('TimesNewRoman', 16))
        self.text_box.setMaxLength(49)
        self.text_box.resize(5 * self.button_width, self.button_height)

        self.b_sta = QtWidgets.QPushButton(self)
        self.b_sta.setText("Standard")
        self.b_sta.setFont(self.font)
        self.b_sta.setGeometry(0, 0, 200, self.button_height)
        self.b_sta.clicked.connect(self.go_standard_calculator)

        self.b_sci = QtWidgets.QPushButton(self)
        self.b_sci.setText("Scientific")
        self.b_sci.setFont(self.font)
        self.b_sci.setGeometry(200, 0, 200, self.button_height)
        self.b_sci.clicked.connect(self.go_scientific_calculator)

        self.b_conv = QtWidgets.QPushButton(self)
        self.b_conv.setText("Converter")
        self.b_conv.setFont(self.font)
        self.b_conv.setGeometry(400, 0, 200, self.button_height)
        self.b_conv.clicked.connect(self.go_converter_calculator)

        self.b_hex = QtWidgets.QPushButton(self)
        self.b_hex.setText("HEX")
        self.b_hex.setFont(self.font)
        self.b_hex.setGeometry(1 * self.button_width, 3 * self.button_height, self.button_width, self.button_height)
        self.b_hex.clicked.connect(lambda: self.clicked_button_system("16"))

        self.b_dec = QtWidgets.QPushButton(self)
        self.b_dec.setText("DEC")
        self.b_dec.setFont(self.font)
        self.b_dec.setGeometry(2 * self.button_width, 3 * self.button_height, self.button_width, self.button_height)
        self.b_dec.clicked.connect(lambda: self.clicked_button_system("10"))

        self.b_oct = QtWidgets.QPushButton(self)
        self.b_oct.setText("OCT")
        self.b_oct.setFont(self.font)
        self.b_oct.setGeometry(3 * self.button_width, 3 * self.button_height, self.button_width, self.button_height)
        self.b_oct.clicked.connect(lambda: self.clicked_button_system("8"))

        self.b_bin = QtWidgets.QPushButton(self)
        self.b_bin.setText("BIN")
        self.b_bin.setFont(self.font)
        self.b_bin.setGeometry(4 * self.button_width, 3 * self.button_height, self.button_width, self.button_height)
        self.b_bin.clicked.connect(lambda: self.clicked_button_system("2"))

        # First column

        self.b_a = QtWidgets.QPushButton(self)
        self.b_a.setText("A")
        self.b_a.setFont(self.font)
        self.b_a.setGeometry(0, 4 * self.button_height, self.button_width, self.button_height)
        self.b_a.clicked.connect(lambda: self.clicked_button_expression("A"))

        self.b_b = QtWidgets.QPushButton(self)
        self.b_b.setText("B")
        self.b_b.setFont(self.font)
        self.b_b.setGeometry(0, 5 * self.button_height, self.button_width, self.button_height)
        self.b_b.clicked.connect(lambda: self.clicked_button_expression("B"))

        self.b_c = QtWidgets.QPushButton(self)
        self.b_c.setText("C")
        self.b_c.setFont(self.font)
        self.b_c.setGeometry(0, 6 * self.button_height, self.button_width, self.button_height)
        self.b_c.clicked.connect(lambda: self.clicked_button_expression("C"))

        self.b_d = QtWidgets.QPushButton(self)
        self.b_d.setText("D")
        self.b_d.setFont(self.font)
        self.b_d.setGeometry(0, 7 * self.button_height, self.button_width, self.button_height)
        self.b_d.clicked.connect(lambda: self.clicked_button_expression("D"))

        self.b_e = QtWidgets.QPushButton(self)
        self.b_e.setText("E")
        self.b_e.setFont(self.font)
        self.b_e.setGeometry(0, 8 * self.button_height, self.button_width, self.button_height)
        self.b_e.clicked.connect(lambda: self.clicked_button_expression("E"))

        self.b_f = QtWidgets.QPushButton(self)
        self.b_f.setText("F")
        self.b_f.setFont(self.font)
        self.b_f.setGeometry(0, 9 * self.button_height, self.button_width, self.button_height)
        self.b_f.clicked.connect(lambda: self.clicked_button_expression("F"))

        # Second column
        self.b_new_2 = QtWidgets.QPushButton(self)
        self.b_new_2.setText("...")
        self.b_new_2.setFont(self.font)
        self.b_new_2.setGeometry(1 * self.button_width, 4 * self.button_height, self.button_width, self.button_height)
        self.b_new_2.clicked.connect(lambda: self.clicked_button_new_button("new 2"))

        self.l_bracket = QtWidgets.QPushButton(self)
        self.l_bracket.setText("(")
        self.l_bracket.setFont(self.font)
        self.l_bracket.setGeometry(1 * self.button_width, 5 * self.button_height, self.button_width, self.button_height)
        self.l_bracket.clicked.connect(lambda: self.clicked_button_expression("("))

        self.b_7 = QtWidgets.QPushButton(self)
        self.b_7.setText("7")
        self.b_7.setFont(self.font)
        self.b_7.setGeometry(1 * self.button_width, 6 * self.button_height, self.button_width, self.button_height)
        self.b_7.clicked.connect(lambda: self.clicked_button_expression("7"))

        self.b_4 = QtWidgets.QPushButton(self)
        self.b_4.setText("4")
        self.b_4.setFont(self.font)
        self.b_4.setGeometry(1 * self.button_width, 7 * self.button_height, self.button_width, self.button_height)
        self.b_4.clicked.connect(lambda: self.clicked_button_expression("4"))

        self.b_1 = QtWidgets.QPushButton(self)
        self.b_1.setText("1")
        self.b_1.setFont(self.font)
        self.b_1.setGeometry(1 * self.button_width, 8 * self.button_height, self.button_width, self.button_height)
        self.b_1.clicked.connect(lambda: self.clicked_button_expression("1"))

        self.b_bit_operation = QtWidgets.QPushButton(self)
        self.b_bit_operation.setText("Operation")
        self.b_bit_operation.setFont(self.font)
        self.b_bit_operation.setGeometry(1 * self.button_width, 9 * self.button_height, self.button_width,
                                         self.button_height)
        self.b_bit_operation.clicked.connect(self.show_operation)

        # Third column

        self.b_new_1 = QtWidgets.QPushButton(self)
        self.b_new_1.setText("...")
        self.b_new_1.setFont(self.font)
        self.b_new_1.setGeometry(2 * self.button_width, 4 * self.button_height, self.button_width, self.button_height)
        self.b_new_1.clicked.connect(lambda: self.clicked_button_new_button("new 1"))

        self.r_bracket = QtWidgets.QPushButton(self)
        self.r_bracket.setText(")")
        self.r_bracket.setFont(self.font)
        self.r_bracket.setGeometry(2 * self.button_width, 5 * self.button_height, self.button_width, self.button_height)
        self.r_bracket.clicked.connect(lambda: self.clicked_button_expression(")"))

        self.b_8 = QtWidgets.QPushButton(self)
        self.b_8.setText("8")
        self.b_8.setFont(self.font)
        self.b_8.setGeometry(2 * self.button_width, 6 * self.button_height, self.button_width, self.button_height)
        self.b_8.clicked.connect(lambda: self.clicked_button_expression("8"))

        self.b_5 = QtWidgets.QPushButton(self)
        self.b_5.setText("5")
        self.b_5.setFont(self.font)
        self.b_5.setGeometry(2 * self.button_width, 7 * self.button_height, self.button_width, self.button_height)
        self.b_5.clicked.connect(lambda: self.clicked_button_expression("5"))

        self.b_2 = QtWidgets.QPushButton(self)
        self.b_2.setText("2")
        self.b_2.setFont(self.font)
        self.b_2.setGeometry(2 * self.button_width, 8 * self.button_height, self.button_width, self.button_height)
        self.b_2.clicked.connect(lambda: self.clicked_button_expression("2"))

        self.b_0 = QtWidgets.QPushButton(self)
        self.b_0.setText("0")
        self.b_0.setFont(self.font)
        self.b_0.setGeometry(2 * self.button_width, 9 * self.button_height, self.button_width, self.button_height)
        self.b_0.clicked.connect(lambda: self.clicked_button_expression("0"))

        # Fourth column

        self.b_c_op = QtWidgets.QPushButton(self)
        self.b_c_op.setText("C")
        self.b_c_op.setFont(self.font)
        self.b_c_op.setGeometry(3 * self.button_width, 4 * self.button_height, self.button_width, self.button_height)
        self.b_c_op.clicked.connect(lambda: self.clicked_button_operation("C"))

        self.b_ce = QtWidgets.QPushButton(self)
        self.b_ce.setText("CE")
        self.b_ce.setFont(self.font)
        self.b_ce.setGeometry(3 * self.button_width, 5 * self.button_height, self.button_width, self.button_height)
        self.b_ce.clicked.connect(lambda: self.clicked_button_operation("CE"))

        self.b_9 = QtWidgets.QPushButton(self)
        self.b_9.setText("9")
        self.b_9.setFont(self.font)
        self.b_9.setGeometry(3 * self.button_width, 6 * self.button_height, self.button_width, self.button_height)
        self.b_9.clicked.connect(lambda: self.clicked_button_expression("9"))

        self.b_6 = QtWidgets.QPushButton(self)
        self.b_6.setText("6")
        self.b_6.setFont(self.font)
        self.b_6.setGeometry(3 * self.button_width, 7 * self.button_height, self.button_width, self.button_height)
        self.b_6.clicked.connect(lambda: self.clicked_button_expression("6"))

        self.b_3 = QtWidgets.QPushButton(self)
        self.b_3.setText("3")
        self.b_3.setFont(self.font)
        self.b_3.setGeometry(3 * self.button_width, 8 * self.button_height, self.button_width, self.button_height)
        self.b_3.clicked.connect(lambda: self.clicked_button_expression("3"))

        self.b_ans = QtWidgets.QPushButton(self)
        self.b_ans.setText("ANS")
        self.b_ans.setFont(self.font)
        self.b_ans.setGeometry(3 * self.button_width, 9 * self.button_height, self.button_width, self.button_height)
        self.b_ans.clicked.connect(self.clicked_button_ans)

        # Fifth column
        self.b_del = QtWidgets.QPushButton(self)
        self.b_del.setText("DEL")
        self.b_del.setFont(self.font)
        self.b_del.setGeometry(4 * self.button_width, 4 * self.button_height, self.button_width, self.button_height)
        self.b_del.clicked.connect(lambda: self.clicked_button_operation("DEL"))

        self.b_div = QtWidgets.QPushButton(self)
        self.b_div.setText("÷")
        self.b_div.setFont(self.font)
        self.b_div.setGeometry(4 * self.button_width, 5 * self.button_height, self.button_width, self.button_height)
        self.b_div.clicked.connect(lambda: self.clicked_button_expression("÷"))

        self.b_mult = QtWidgets.QPushButton(self)
        self.b_mult.setText("×")
        self.b_mult.setFont(self.font)
        self.b_mult.setGeometry(4 * self.button_width, 6 * self.button_height, self.button_width, self.button_height)
        self.b_mult.clicked.connect(lambda: self.clicked_button_expression("×"))

        self.b_sub = QtWidgets.QPushButton(self)
        self.b_sub.setText("-")
        self.b_sub.setFont(self.font)
        self.b_sub.setGeometry(4 * self.button_width, 7 * self.button_height, self.button_width, self.button_height)
        self.b_sub.clicked.connect(lambda: self.clicked_button_expression("-"))

        self.b_add = QtWidgets.QPushButton(self)
        self.b_add.setText("+")
        self.b_add.setFont(self.font)
        self.b_add.setGeometry(4 * self.button_width, 8 * self.button_height, self.button_width, self.button_height)
        self.b_add.clicked.connect(lambda: self.clicked_button_expression("+"))

        self.b_eq = QtWidgets.QPushButton(self)
        self.b_eq.setText("=")
        self.b_eq.setFont(self.font)
        self.b_eq.setGeometry(4 * self.button_width, 9 * self.button_height, self.button_width, self.button_height)
        self.b_eq.clicked.connect(self.clicked_button_result)

        self.show()

    def go_standard_calculator(self):
        self.new_window = Standard_GUI.MyWindow()
        self.new_window.show()
        self.close()

    def go_scientific_calculator(self):
        self.new_window = Scientific_GUI.MyWindow()
        self.new_window.show()
        self.close()

    def go_converter_calculator(self):
        self.new_window = Converter_GUI.MyWindow()
        self.new_window.show()
        self.close()

    def clicked_button_ans(self):
        print("ANS val: ", self.ans_val)
        if len(self.experssion + self.ans_val) < 49:
            self.experssion += self.ans_val
        self.text_box.setText(self.experssion)

    def clicked_button_system(self, arg):
        self.system = arg
        print(self.system)

    def clicked_button_operation(self, arg):  # Other operations
        if arg == "DEL":
            self.experssion = self.experssion[0: len(self.experssion) - 1]
        elif arg == "C":
            self.experssion = ""
        elif arg == "CE":
            self.experssion = ""
            self.ans_val = ""

        self.text_box.setText(self.experssion)

    def update_expression(self, arg):
        if len(self.experssion + arg) < 49:
            self.experssion += arg
        self.text_box.setText(self.experssion)

    def clicked_button_new_button(self, arg):
        print("Clicked new button!!! ", arg)

    def clicked_button_expression(self, arg):
        if len(self.experssion + arg) < 49:
            self.experssion += arg

        self.text_box.setText(self.experssion)

    def show_operation(self):
        self.operation_window.show()

    def set_operation(self, operation):
        if len(self.experssion + operation) < 49:
            self.experssion += operation

        self.text_box.setText(self.experssion)

    def clicked_button_result(self):  # EQ button
        if (self.first_use == False):
            print(self.experssion, " ", self.system)
            self.experssion_class = Programmer_Expression.Expression(str(self.experssion), str(self.system))
            self.experssion_class.translate_expression()
            self.experssion_class.check_system()
            self.experssion_class.evaluate_expression()
            self.result = str(self.experssion_class.get_expression())
            self.text_box.setText(str(self.result))
            self.ans_val = self.result
            self.experssion = self.result
            self.first_use = True
        else:
            self.experssion_class = Programmer_Expression.Expression(str(self.experssion), str(self.system))
            self.experssion_class.translate_expression()
            self.experssion_class.check_system()
            self.experssion_class.evaluate_expression()
            self.result = str(self.experssion_class.get_expression())
            self.text_box.setText(str(self.result))
            self.ans_val = self.result
            self.experssion = self.result
            self.first_use = True

