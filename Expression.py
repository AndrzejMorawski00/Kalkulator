class Expression:

    def __init__(self, expression):
        self.expression = expression

    def translatate_expression(self):
        self.expression = self.expression.replace('×','*')
        self.expression = self.expression.replace('÷','/')
        self.expression = self.expression.replace('^','**')

        if (self.expression.find("√") != -1):
            idx = self.expression.find("√")
            self.expression = self.expression.replace("√", "")
            exp_1 = self.expression[0: idx]
            exp_2 = self.expression[idx: len(self.expression)] + "**0.5"
            self.expression = exp_1 + exp_2



    def update(self, new_expression):
        self.expression = new_expression

    def get_expression(self):
        return self.expression

    def evaluate_expression(self):
        try:
            self.expression = str(round(float(eval(self.expression)), 4))
            return self.expression
        except:
            return "ERROR"



