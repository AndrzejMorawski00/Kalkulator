class Converter_Expression:

    def __init__(self, expression, from_operation, to_operation):
        """
        Konstruktor
        :param expression:
        :param from_operation:
        :param to_operation:
        """
        self.expression = expression
        self.from_operation = from_operation
        self.to_operation = to_operation

    def translate_expression(self):
        """
        Funkcja odpowiedzialna za przekształcanie wyrażenia.
        :return:
        """
        try:
            if self.from_operation != self.to_operation:
                if self.from_operation == "16":
                    if self.to_operation == "10":
                        self.expression = str(int(self.expression, int(self.from_operation)))

                    elif self.to_operation == "8":
                        self.expression = int(self.expression, int(self.from_operation))
                        self.expression = oct(self.expression)

                    elif self.to_operation == "2":
                        self.expression = int(self.expression, int(self.from_operation))
                        self.expression = bin(self.expression)

                elif self.from_operation == "10":
                    self.expression = int(self.expression)

                    if self.to_operation == "16":
                        self.expression = hex(self.expression)

                    elif self.to_operation == "8":
                        self.expression = oct(self.expression)

                    elif self.to_operation == "2":
                        self.expression = bin(self.expression)

                    self.expression = str(self.expression)

                elif self.from_operation == "8":
                    if self.to_operation == "10":
                        self.expression = str(int(self.expression, int(self.from_operation)))

                    elif self.to_operation == "16":
                        self.expression = int(self.expression, int(self.from_operation))
                        self.expression = hex(self.expression)

                    elif self.to_operation == "2":
                        self.expression = int(self.expression, int(self.from_operation))
                        self.expression = bin(self.expression)

                elif self.from_operation == "2":
                    if self.to_operation == "10":
                        self.expression = str(int(self.expression, int(self.from_operation)))

                    elif self.to_operation == "16":
                        self.expression = int(self.expression, int(self.from_operation))
                        self.expression = hex(self.expression)

                    elif self.to_operation == "8":
                        self.expression = int(self.expression, int(self.from_operation))
                        self.expression = oct(self.expression)

            if self.to_operation == "16":
                self.expression = self.expression.replace("0x", "", 1)
            elif self.to_operation == "8":
                self.expression = self.expression.replace("0o", "", 1)
            elif self.to_operation == "2":
                self.expression = self.expression.replace("0b", "", 1)

            self.expression = self.expression.upper()
        except:
            "ERROR"

    def update(self, expression, from_operation, to_operation):
        """
        Funkcja odpowiedzialna za aktualizację wyrażenia.
        :param expression:
        :param from_operation:
        :param to_operation:
        :return:
        """
        self.expression = expression
        self.from_operation = from_operation
        self.to_operation = to_operation

    def get_expression(self):
        """
        Funkcja zwracająca przekształcone wyrażenie.
        :return:
        """
        return self.expression
