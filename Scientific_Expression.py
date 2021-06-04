import numpy as np
import math


class Expression:

    def __init__(self, expression):
        self.expression = expression
        self.e = str(math.e)
        self.pi = str(math.pi)

    def update(self, new_expression):
        self.expression = new_expression

    def translate_expression(self):
        self.expression = self.expression.replace('×', '*')
        self.expression = self.expression.replace('÷', '/')
        self.translate_pow()
        self.expression = self.expression.replace("^", "**")
        self.expression = self.expression.replace("e", self.e)
        self.expression = self.expression.replace("π", self.pi)

        self.translate_roots()
        self.translate_logs()
        self.translate_fact()

    def translate_pow(self):

        while (self.expression.find("^1/") != -1):
            idx = self.expression.find("^1/") + 3
            new_number = ""
            start_idx = idx
            end_idx = idx

            while (idx < len(self.expression) and (
                    (48 <= ord(self.expression[idx]) <= 57) or self.expression[idx] == ".")):
                new_number += self.expression[idx]
                end_idx += 1
                idx += 1
            exp_1 = self.expression[0: start_idx]
            exp_2 = self.expression[start_idx: len(self.expression)]
            exp_2 = exp_2.replace(new_number, new_number + ")", 1)

            self.expression = exp_1 + exp_2

            self.expression = self.expression.replace("^1/", "**(1/", 1)

    def translate_roots(self):
        while (self.expression.find("3√") != -1):

            idx = self.expression.find("3√") + 2
            new_number = ""

            while (idx < len(self.expression) and (
                    (48 <= ord(self.expression[idx]) <= 57) or self.expression[idx] == ".")):
                new_number += self.expression[idx]
                idx += 1

            self.expression = self.expression.replace(new_number, new_number + "**(1/3)", 1)
            self.expression = self.expression.replace("3√", "", 1)

        while (self.expression.find("√") != -1):
            idx = self.expression.find("√") + 1
            new_number = ""

            while (idx < len(self.expression) and (
                    (48 <= ord(self.expression[idx]) <= 57) or self.expression[idx] == ".")):
                new_number += self.expression[idx]
                idx += 1

            self.expression = self.expression.replace(new_number, new_number + "**(1/2)", 1)
            self.expression = self.expression.replace("√", "", 1)

    def translate_fact(self):
        while (self.expression.find("!") != -1):
            idx = self.expression.find("!") - 1
            new_number = ""

            while (idx >= 0 and ((48 <= ord(self.expression[idx]) <= 57) or self.expression[idx] == ".")):
                new_number += self.expression[idx]
                idx -= 1

            new_number = new_number[::-1]
            fact_val = str(self.fact_n(new_number))
            self.expression = self.expression.replace(new_number, fact_val, 1)
            self.expression = self.expression.replace("!", "", 1)

    def translate_logs(self):

        # logx  -> log base 10 of x
        # lnx   -> log base e of x
        # logxy -> log base x of y
        while (self.expression.find("ln") != -1):
            idx = self.expression.find("ln") + 2
            new_number = ""

            while (idx < len(self.expression) and (
                    (48 <= ord(self.expression[idx]) <= 57) or self.expression[idx] == ".")):
                new_number += self.expression[idx]
                idx += 1
            try:
                new_number = float(new_number)
                new_log = round(np.log(new_number), 4)
                self.expression = self.expression.replace(str(new_number), str(new_log))
                self.expression = self.expression.replace("ln", "", 1)
            except:
                return "ERROR"

        while (self.expression.find("log") != -1):
            idx = self.expression.find("log") + 3
            new_number = ""

            while (idx < len(self.expression) and (
                    (48 <= ord(self.expression[idx]) <= 57) or self.expression[idx] == "." or self.expression[
                idx] == "_")):
                new_number += self.expression[idx]

                idx += 1

            tab_number = new_number.split("_")
            if (len(tab_number) == 1):
                new_log = round(math.log10(float(tab_number[0])), 4)
            elif (len(tab_number) == 2):
                new_log = round(math.log(float(tab_number[1]), float(tab_number[0])))

            self.expression = self.expression.replace(new_number, str(new_log))
            self.expression = self.expression.replace("log", "", 1)

    def fact_n(self, n):
        try:
            n = int(n)
        except:
            return "ERROR"
        result = 1
        for i in range(1, n + 1):
            result *= i

        return result

    def get_expression(self):
        print(self.expression)

    def evaluate_expression(self):
        try:
            self.expression = str(round(float(eval(self.expression)), 4))
            return self.expression
        except:
            return "ERROR"


k = "5^1/5+4^1/43423423+4^1/3123"

k = Expression(k)
k.translate_expression()
k.get_expression()
print(k.evaluate_expression())