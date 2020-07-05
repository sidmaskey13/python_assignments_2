givenNumber1 = int(input('Enter first number: '))
givenNumber2 = intinput('Enter second number: ')
givenOperator = input('Enter Operator [ + , - , / , * ]: ')


class Calculator:
    def __init__(self, x, y, operator):
        self.x = int(x)
        self.y = int(y)
        self.operator = operator
        self.selector()

    def add(self):
        ans = self.x + self.y
        return f"Summation is {ans}"

    def selector(self):
        if self.operator == "+":
            print(self.add())
        else:
            print("Please enter correct operator")


cal = Calculator(givenNumber1, givenNumber2, givenOperator)




