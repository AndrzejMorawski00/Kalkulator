from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt5.QtGui import QFont
import Standard_Expression
import sys


class MyWindow(QMainWindow):

    def __init__(self):
        self.button_height = 70
        self.button_width = 120
        self.font = QFont('TimesNewRoman', 13)

        self.k = 120

        self.result = ""
        self.experssion = ""
        self.ans_val = ""
        self.first_use = False
        self.switch = False

        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 5 * self.button_width, 10 * self.button_height)
        self.setWindowTitle("Calculator")
        self.initUI()

    def initUI(self):
        self.text_box = QLineEdit(self)
        self.text_box.move(0, self.button_height + 30)
        self.text_box.setFont(QFont('TimesNewRoman', 16))
        self.text_box.setMaxLength(49)
        self.text_box.resize(5 * self.button_width, self.button_height)

        self.b_sci = QtWidgets.QPushButton(self)
        self.b_sci.setText("Standard")
        self.b_sci.setFont(self.font)
        self.b_sci.setGeometry(0, 0, self.button_width + 15, self.button_height)

        self.b_prog = QtWidgets.QPushButton(self)
        self.b_prog.setText("Programmer")
        self.b_prog.setFont(self.font)
        self.b_prog.setGeometry(self.button_width + 15, 0, self.button_width + 15, self.button_height)
        self.b_prog.clicked.connect(self.clicked_button)

        self.b_new = QtWidgets.QPushButton(self)
        self.b_new.setText("...")
        self.b_new.setFont(self.font)
        self.b_new.setGeometry(2 * self.button_width + 30, 0, self.button_width + 15, self.button_height)
        self.b_new.clicked.connect(self.clicked_button)

        self.b_new_1 = QtWidgets.QPushButton(self)
        self.b_new_1.setText("...")
        self.b_new_1.setFont(self.font)
        self.b_new_1.setGeometry(3 * self.button_width + 45, 0, self.button_width + 15, self.button_height)
        self.b_new_1.clicked.connect(self.clicked_button)

        # First column

        self.switch_button = QtWidgets.QPushButton(self)
        self.switch_button.setText("Switch")
        self.switch_button.setFont(self.font)
        self.switch_button.setGeometry(0, 3 * self.button_height, self.button_width, self.button_height)
        self.switch_button.clicked.connect(self.clicked_button_switch)

        self.pow_2 = QtWidgets.QPushButton(self)
        self.pow_2.setText("x^2")
        self.pow_2.setFont(self.font)
        self.pow_2.setGeometry(0, 4 * self.button_height, self.button_width, self.button_height)
        self.pow_2.clicked.connect(lambda: self.clicked_button_expression("x^2"))

        self.pow_3 = QtWidgets.QPushButton(self)
        self.pow_3.setText("x^3")
        self.pow_3.setFont(self.font)
        self.pow_3.setGeometry(0, 4 * self.button_height, self.button_width, self.button_height)
        self.pow_3.clicked.connect(lambda: self.clicked_button_expression("x^3"))

        self.root_2 = QtWidgets.QPushButton(self)
        self.root_2.setText("√x")
        self.root_2.setFont(self.font)
        self.root_2.setGeometry(0, 5 * self.button_height, self.button_width, self.button_height)
        self.root_2.clicked.connect(lambda: self.clicked_button_expression("√x"))

        self.root_3 = QtWidgets.QPushButton(self)
        self.root_3.setText("3√x")
        self.root_3.setFont(self.font)
        self.root_3.setGeometry(0, 5 * self.button_height, self.button_width, self.button_height)
        self.root_3.clicked.connect(lambda: self.clicked_button_expression("3√x"))

        self.pow_n = QtWidgets.QPushButton(self)
        self.pow_n.setText("x^y")
        self.pow_n.setFont(self.font)
        self.pow_n.setGeometry(0, 6 * self.button_height, self.button_width, self.button_height)
        self.pow_n.clicked.connect(lambda: self.clicked_button_expression("x^y"))

        self.pow_1_n = QtWidgets.QPushButton(self)
        self.pow_1_n.setText("x^1/y")
        self.pow_1_n.setFont(self.font)
        self.pow_1_n.setGeometry(0, 6 * self.button_height, self.button_width, self.button_height)
        self.pow_1_n.clicked.connect(lambda: self.clicked_button_expression("x^1/y"))

        self.ten_pow = QtWidgets.QPushButton(self)
        self.ten_pow.setText("10^x")
        self.ten_pow.setFont(self.font)
        self.ten_pow.setGeometry(0, 7 * self.button_height, self.button_width, self.button_height)
        self.ten_pow.clicked.connect(lambda: self.clicked_button_expression("10^x"))

        self.two_pow = QtWidgets.QPushButton(self)
        self.two_pow.setText("2^x")
        self.two_pow.setFont(self.font)
        self.two_pow.setGeometry(0, 7 * self.button_height, self.button_width, self.button_height)
        self.two_pow.clicked.connect(lambda: self.clicked_button_expression("2^x"))

        self.log_n = QtWidgets.QPushButton(self)
        self.log_n.setText("log")
        self.log_n.setFont(self.font)
        self.log_n.setGeometry(0, 8 * self.button_height, self.button_width, self.button_height)
        self.log_n.clicked.connect(lambda: self.clicked_button_expression("log"))

        self.log_x_y = QtWidgets.QPushButton(self)
        self.log_x_y.setText("logxy")
        self.log_x_y.setFont(self.font)
        self.log_x_y.setGeometry(0, 8 * self.button_height, self.button_width, self.button_height)
        self.log_x_y.clicked.connect(lambda: self.clicked_button_expression("logxy"))

        self.b_ln = QtWidgets.QPushButton(self)
        self.b_ln.setText("ln")
        self.b_ln.setFont(self.font)
        self.b_ln.setGeometry(0, 9 * self.button_height, self.button_width, self.button_height)
        self.b_ln.clicked.connect(lambda: self.clicked_button_expression("ln"))

        self.b_e_x = QtWidgets.QPushButton(self)
        self.b_e_x.setText("e^x")
        self.b_e_x.setFont(self.font)
        self.b_e_x.setGeometry(0, 9 * self.button_height, self.button_width, self.button_height)
        self.b_e_x.clicked.connect(lambda: self.clicked_button_expression("e^x"))

        # Second column

        self.pi_button = QtWidgets.QPushButton(self)
        self.pi_button.setText("π")
        self.pi_button.setFont(self.font)
        self.pi_button.setGeometry(1 * self.button_width, 3 * self.button_height, self.button_width, self.button_height)
        self.pi_button.clicked.connect(lambda: self.clicked_button_expression("π"))

        self.b_inv = QtWidgets.QPushButton(self)
        self.b_inv.setText("1/x")
        self.b_inv.setFont(self.font)
        self.b_inv.setGeometry(1 * self.button_width, 4 * self.button_height, self.button_width, self.button_height)
        self.b_inv.clicked.connect(lambda: self.clicked_button_expression("1/x"))

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

        self.b_ans = QtWidgets.QPushButton(self)
        self.b_ans.setText("ANS")
        self.b_ans.setFont(self.font)
        self.b_ans.setGeometry(1 * self.button_width, 9 * self.button_height, self.button_width, self.button_height)
        self.b_ans.clicked.connect(lambda: self.clicked_button_ans())

        # Third column

        self.b_e = QtWidgets.QPushButton(self)
        self.b_e.setText("e")
        self.b_e.setFont(self.font)
        self.b_e.setGeometry(2 * self.button_width, 3 * self.button_height, self.button_width, self.button_height)
        self.b_e.clicked.connect(lambda: self.clicked_button_expression("e"))

        self.abs_val = QtWidgets.QPushButton(self)
        self.abs_val.setText("|x|")
        self.abs_val.setFont(self.font)
        self.abs_val.setGeometry(2 * self.button_width, 4 * self.button_height, self.button_width, self.button_height)
        self.abs_val.clicked.connect(lambda: self.clicked_button_abs())

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

        self.b_c = QtWidgets.QPushButton(self)
        self.b_c.setText("C")
        self.b_c.setFont(self.font)
        self.b_c.setGeometry(3 * self.button_width, 3 * self.button_height, self.button_width, self.button_height)
        self.b_c.clicked.connect(lambda: self.clicked_button_operation("C"))

        self.b_ce = QtWidgets.QPushButton(self)
        self.b_ce.setText("CE")
        self.b_ce.setFont(self.font)
        self.b_ce.setGeometry(3 * self.button_width, 4 * self.button_height, self.button_width, self.button_height)
        self.b_ce.clicked.connect(lambda: self.clicked_button_operation("CE"))

        self.n_fact = QtWidgets.QPushButton(self)
        self.n_fact.setText("n!")
        self.n_fact.setFont(self.font)
        self.n_fact.setGeometry(3 * self.button_width, 5 * self.button_height, self.button_width, self.button_height)
        self.n_fact.clicked.connect(lambda: self.clicked_button_expression("n!"))

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

        self.b_dot = QtWidgets.QPushButton(self)
        self.b_dot.setText(",")
        self.b_dot.setFont(self.font)
        self.b_dot.setGeometry(3 * self.button_width, 9 * self.button_height, self.button_width, self.button_height)
        self.b_dot.clicked.connect(lambda: self.clicked_button_expression("."))

        # Fifth column

        self.b_del = QtWidgets.QPushButton(self)
        self.b_del.setText("DEL")
        self.b_del.setFont(self.font)
        self.b_del.setGeometry(4 * self.button_width, 3 * self.button_height, self.button_width, self.button_height)
        self.b_del.clicked.connect(lambda: self.clicked_button_operation("DEL"))

        self.b_mod = QtWidgets.QPushButton(self)
        self.b_mod.setText("%")
        self.b_mod.setFont(self.font)
        self.b_mod.setGeometry(4 * self.button_width, 4 * self.button_height, self.button_width, self.button_height)
        self.b_mod.clicked.connect(lambda: self.clicked_button_expression("%"))

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
        self.b_eq.clicked.connect(lambda: self.clicked_button_result())

        # Functions

    def clicked_button(self):
        print("Clicked button!!!")

        # Clicked function (Switch ln -> e ^ x)

    def clicked_button_switch(self):  # Default switch is False

        # logx  -> log base 10 of x
        # lnx   -> log base e of x
        # logxy -> log base x of y

        if (self.switch == True):
            self.switch = False
            self.pow_2.hide()
            self.pow_3.show()

            self.root_2.hide()
            self.root_3.show()

            self.pow_n.hide()
            self.pow_1_n.show()

            self.ten_pow.hide()
            self.two_pow.show()

            self.log_n.hide()
            self.log_x_y.show()

            self.b_ln.hide()
            self.b_e_x.show()

        else:
            self.switch = True
            self.pow_2.show()
            self.pow_3.hide()

            self.root_2.show()
            self.root_3.hide()

            self.pow_1_n.show()
            self.pow_n.hide()

            self.ten_pow.show()
            self.two_pow.hide()

            self.log_n.show()
            self.log_x_y.hide()

            self.b_ln.show()
            self.b_e_x.hide()

    def clicked_button_operation(self, arg):
        print("Clicked operation button!!! ")

    def clicked_button_expression(self, arg):
        print("Clicked expression!!! " + arg)
        if (len(self.experssion) < 49):
            self.experssion += arg

        self.text_box.setText(self.experssion)

    def clicked_button_abs(self):
        print("Clikced abs!!!")

    def clicked_button_ans(self):
        print("Clicked ans!!!")

    def clicked_button_result(self):
        print("Cliecked result!!!")


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()


window()
