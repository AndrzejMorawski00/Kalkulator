import Converter_Expression


class Programmer_Expression:

    def __init__(self, expression, system):
        self.expression = expression
        self.system = system

    def translate_expression(self):
        self.expression = self.expression.replace("×", "*")
        self.expression = self.expression.replace("÷", "/")
        self.expression = self.expression.replace("AND", "&")
        self.expression = self.expression.replace("XOR", "^")
        self.expression = self.expression.replace("OR", "|")
        self.expression = self.expression.replace("NOT", "~")

    def get_expression(self):

        new_expression = Converter_Expression.Converter_Expression(self.expression,"10",self.system)
        new_expression.translate_expression()
        self.expression = new_expression.get_expression()

        return str(self.expression)

    def get_system(self):
        print(self.system)
        return str(self.system)

    def check_system(self):

        system_dict = {
            "0": "2", "1": "2",
            "2": "8", "3": "8",
            "4": "8", "5": "8",
            "6": "8", "7": "8",
            "8": "10", "9": "10",
            "A": "16", "B": "16",
            "C": "16", "D": "16",
            "E": "16", "F": "16",
        }

        for i in range(len(self.expression)):
            try:
                if int(self.system) < int(system_dict[self.expression[i]]):
                    self.system = system_dict[self.expression[i]]
            except:
                pass

    def evaluate_expression(self):

        self.translate_expression()
        self.check_system()

        expression_copy = self.expression
        new_number = ""

        for i in range(len(self.expression)):
            if ((48 <= ord(self.expression[i]) <= 57) or (65 <= ord(self.expression[i]) <= 70)):
                new_number += self.expression[i]
            else:
                new_expression = Converter_Expression.Converter_Expression(new_number, self.system,"10")
                new_expression.translate_expression()
                new_expression = new_expression.get_expression()
                expression_copy = expression_copy.replace(new_number, new_expression, 1)
                new_number = ""
        new_expression = Converter_Expression.Converter_Expression(new_number, self.system, "10")
        new_expression.translate_expression()
        new_expression = new_expression.get_expression()
        expression_copy = expression_copy.replace(new_number, new_expression, 1)

        self.expression = expression_copy
        print(expression_copy)
        self.evaluate_bit_operations()

    def evaluate_bit_operations(self):
        try:
            self.expression = str(eval(self.expression))
        except:
            self.expression = "ERROR"

    def update(self, expression, system):
        self.expression = expression
        self.system = system


