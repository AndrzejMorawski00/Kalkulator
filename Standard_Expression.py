class Expression:

    def __init__(self, expression):
        self.expression = expression

    def translate_expression(self):
        self.expression = self.expression.replace('×', '*')
        self.expression = self.expression.replace('÷', '/')
        self.expression = self.expression.replace("^1/", "**(1/)")
        self.expression = self.expression.replace('^', '**')

        self.translate_roots()




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

    def update(self, new_expression):
        self.expression = new_expression

    def get_expression(self):
        return self.expression

    def evaluate_expression(self):
        print(self.expression)
        try:
            self.expression = str(round(float(eval(self.expression)), 4))
            return self.expression
        except:
            return "ERROR"


