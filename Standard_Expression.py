class Standard_Expression:
    def __init__(self, expression):
        """
        Konstruktor
        :param expression:
        """
        self.expression = expression

    def translate_expression(self):
        """
        Funkcja odpowiedzialna za przekształcenie wyrażenia do postaci gotowej do ewaluacji.
        :return:
        """
        self.expression = self.expression.replace('×', '*')
        self.expression = self.expression.replace('÷', '/')
        self.expression = self.expression.replace("^1/", "**(1/)")
        self.expression = self.expression.replace('^', '**')
        self.translate_roots()

    def translate_roots(self):
        """
        Funkcja odpowiedzialna za przetłumaczenie pierwiastków
        :return:
        """
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
        """
        Funkcja odpowiedzialna za aktualizację wyrażenia.
        :param new_expression:
        :return:
        """
        self.expression = new_expression

    def evaluate_expression(self):
        """
        Funkcja odpowiedzialna za ewaluację i zwrócenie wyrażenia.
        :return:
        """
        print(self.expression)
        try:
            self.expression = str(round(float(eval(self.expression)), 4))
            return self.expression
        except:
            return "ERROR"


