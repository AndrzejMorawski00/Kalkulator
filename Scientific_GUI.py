from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt5.QtGui import QFont
from  PyQt5.uic import loadUi
import sys



class MyWindow(QMainWindow):

    def __init__(self):
        self.button_height = 70
        self.button_width = 120
        self.font = QFont('TimesNewRoman', 13)
        self.experssion = ""
        self.k = 120
        self.result = ""


        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 4 * self.button_width, 9 * self.button_height - 10)
        self.setWindowTitle("Kalkulator")
        self.initUI()

    def initUI(self):
        self.text_box = QLineEdit(self)
        self.text_box.move(0, self.button_height + 30)
        self.text_box.setFont(QFont('TimesNewRoman', 16))
        self.text_box.setMaxLength(49)
        self.text_box.resize(4 * self.button_width, self.button_height)

        self.b_sci = QtWidgets.QPushButton(self)
        self.b_sci.setText("Scientific")
        self.b_sci.setFont(self.font)
        self.b_sci.setGeometry(0, 0, self.button_width, self.button_height)
        self.b_sci.clicked.connect(self.clicked_button)

        self.b_prog = QtWidgets.QPushButton(self)
        self.b_prog.setText("Programmer")
        self.b_prog.setFont(self.font)
        self.b_prog.setGeometry(self.button_width, 0, self.button_width, self.button_height)
        self.b_prog.clicked.connect(self.clicked_button)

        self.b_new = QtWidgets.QPushButton(self)
        self.b_new.setText("...")
        self.b_new.setFont(self.font)
        self.b_new.setGeometry(2 * self.button_width, 0, self.button_width, self.button_height)
        self.b_new.clicked.connect(self.clicked_button)

        self.b_new_1 = QtWidgets.QPushButton(self)
        self.b_new_1.setText("...")
        self.b_new_1.setFont(self.font)
        self.b_new_1.setGeometry(3 * self.button_width, 0, self.button_width, self.button_height)
        self.b_new_1.clicked.connect(self.clicked_button)

        # First column

        self.k = self.k + 80

        # self.b_mod = QtWidgets.QPushButton(self)
        # self.b_mod.setText("%")
        # self.b_mod.setFont(self.font)
        # self.b_mod.setGeometry(0, self.k, self.button_width, self.button_height)
        # self.b_mod.clicked.connect(self.clicked_button)
        #
        # self.b_inv = QtWidgets.QPushButton(self)
        # self.b_inv.setText("1/x")
        # self.b_inv.setFont(self.font)
        # self.b_inv.setGeometry(0, self.k + self.button_height, self.button_width, self.button_height)
        # self.b_inv.clicked.connect(self.clicked_button)
        #
        # self.b_7 = QtWidgets.QPushButton(self)
        # self.b_7.setText("7")
        # self.b_7.setFont(self.font)
        # self.b_7.setGeometry(0, self.k + 2 * self.button_height, self.button_width, self.button_height)
        # self.b_7.clicked.connect(self.clicked_button)
        #
        # self.b_4 = QtWidgets.QPushButton(self)
        # self.b_4.setText("4")
        # self.b_4.setFont(self.font)
        # self.b_4.setGeometry(0, self.k + 3 * self.button_height, self.button_width, self.button_height)
        # self.b_4.clicked.connect(self.clicked_button)
        #
        # self.b_1 = QtWidgets.QPushButton(self)
        # self.b_1.setText("1")
        # self.b_1.setFont(self.font)
        # self.b_1.setGeometry(0, self.k + 4 * self.button_height, self.button_width, self.button_height)
        # self.b_1.clicked.connect(self.clicked_button)
        #
        # self.b_ans = QtWidgets.QPushButton(self)
        # self.b_ans.setText("ANS")
        # self.b_ans.setFont(self.font)
        # self.b_ans.setGeometry(0, self.k + 5 * self.button_height, self.button_width, self.button_height)
        # self.b_ans.clicked.connect(self.clicked_button)

        # Second Column

        self.b_ce = QtWidgets.QPushButton(self)
        self.b_ce.setText("CE")
        self.b_ce.setFont(self.font)
        self.b_ce.setGeometry(self.button_width, self.k, self.button_width, self.button_height)
        self.b_ce.clicked.connect(self.clicked_button)

        self.b_pow_2 = QtWidgets.QPushButton(self)
        self.b_pow_2.setText("x^2")
        self.b_pow_2.setFont(self.font)
        self.b_pow_2.setGeometry(self.button_width, self.k + self.button_height, self.button_width, self.button_height)
        self.b_pow_2.clicked.connect(self.clicked_button)

        self.b_8 = QtWidgets.QPushButton(self)
        self.b_8.setText("8")
        self.b_8.setFont(self.font)
        self.b_8.setGeometry(self.button_width, self.k + 2 * self.button_height, self.button_width, self.button_height)
        self.b_8.clicked.connect(self.clicked_button)

        self.b_5 = QtWidgets.QPushButton(self)
        self.b_5.setText("5")
        self.b_5.setFont(self.font)
        self.b_5.setGeometry(self.button_width, self.k + 3 * self.button_height, self.button_width, self.button_height)
        self.b_5.clicked.connect(self.clicked_button)

        self.b_2 = QtWidgets.QPushButton(self)
        self.b_2.setText("2")
        self.b_2.setFont(self.font)
        self.b_2.setGeometry(self.button_width, self.k + 4 * self.button_height, self.button_width, self.button_height)
        self.b_2.clicked.connect(self.clicked_button)

        self.b_0 = QtWidgets.QPushButton(self)
        self.b_0.setText("0")
        self.b_0.setFont(self.font)
        self.b_0.setGeometry(self.button_width, self.k + 5 * self.button_height, self.button_width, self.button_height)
        self.b_0.clicked.connect(self.clicked_button)

        # Third Column

        self.b_c = QtWidgets.QPushButton(self)
        self.b_c.setText("C")
        self.b_c.setFont(self.font)
        self.b_c.setGeometry(2 * self.button_width, self.k, self.button_width, self.button_height)
        self.b_c.clicked.connect(self.clicked_button)

        self.b_sq_root = QtWidgets.QPushButton(self)
        self.b_sq_root.setText("√x")
        self.b_sq_root.setFont(self.font)
        self.b_sq_root.setGeometry(2 * self.button_width, self.k + self.button_height, self.button_width,
                                   self.button_height)
        self.b_sq_root.clicked.connect(self.clicked_button)

        self.b_9 = QtWidgets.QPushButton(self)
        self.b_9.setText("9")
        self.b_9.setFont(self.font)
        self.b_9.setGeometry(2 * self.button_width, self.k + 2 * self.button_height, self.button_width,
                             self.button_height)
        self.b_9.clicked.connect(self.clicked_button)

        self.b_6 = QtWidgets.QPushButton(self)
        self.b_6.setText("6")
        self.b_6.setFont(self.font)
        self.b_6.setGeometry(2 * self.button_width, self.k + 3 * self.button_height, self.button_width,
                             self.button_height)
        self.b_6.clicked.connect(self.clicked_button)

        self.b_3 = QtWidgets.QPushButton(self)
        self.b_3.setText("3")
        self.b_3.setFont(self.font)
        self.b_3.setGeometry(2 * self.button_width, self.k + 4 * self.button_height, self.button_width,
                             self.button_height)
        self.b_3.clicked.connect(self.clicked_button)

        self.b_dot = QtWidgets.QPushButton(self)
        self.b_dot.setText(",")
        self.b_dot.setFont(self.font)
        self.b_dot.setGeometry(2 * self.button_width, self.k + 5 * self.button_height, self.button_width,
                               self.button_height)
        self.b_dot.clicked.connect(self.clicked_button)

        # Foutrh Column

        self.b_del = QtWidgets.QPushButton(self)
        self.b_del.setText("DEL")
        self.b_del.setFont(self.font)
        self.b_del.setGeometry(3 * self.button_width, self.k, self.button_width, self.button_height)
        self.b_del.clicked.connect(self.clicked_button)

        self.b_div = QtWidgets.QPushButton(self)
        self.b_div.setText("÷")
        self.b_div.setFont(self.font)
        self.b_div.setGeometry(3 * self.button_width, self.k + self.button_height, self.button_width,
                               self.button_height)
        self.b_div.clicked.connect(self.clicked_button)

        self.b_mult = QtWidgets.QPushButton(self)
        self.b_mult.setText("×")
        self.b_mult.setFont(self.font)
        self.b_mult.setGeometry(3 * self.button_width, self.k + 2 * self.button_height, self.button_width,
                                self.button_height)
        self.b_mult.clicked.connect(self.clicked_button)

        self.b_sub = QtWidgets.QPushButton(self)
        self.b_sub.setText("-")
        self.b_sub.setFont(self.font)
        self.b_sub.setGeometry(3 * self.button_width, self.k + 3 * self.button_height, self.button_width,
                               self.button_height)
        self.b_sub.clicked.connect(self.clicked_button)

        self.b_add = QtWidgets.QPushButton(self)
        self.b_add.setText("+")
        self.b_add.setFont(self.font)
        self.b_add.setGeometry(3 * self.button_width, self.k + 4 * self.button_height, self.button_width,
                               self.button_height)
        self.b_add.clicked.connect(self.clicked_button)

        self.b_eq = QtWidgets.QPushButton(self)
        self.b_eq.setText("=")
        self.b_eq.setFont(self.font)
        self.b_eq.setGeometry(3 * self.button_width, self.k + 5 * self.button_height, self.button_width,
                              self.button_height)
        self.b_eq.clicked.connect(lambda: self.clicked_button_test("k"))

    def clicked_button(self):
        print("Clicked!!!")


    def clicked_button_test(self, var):
        self.experssion += str(var)
        self.text_box.setText(self.experssion)






def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()