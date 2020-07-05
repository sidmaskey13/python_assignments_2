# Write a program that serves as a basic calculator. It asks for two
# numbers, then it asks for an operator. Gracefully deal with input that
# doesn't cleanly convert to numbers. Deal with division by zero errors.

while True:
    try:
        GIVEN_NUMBER1 = int(input("Enter first number: "))
        GIVEN_NUMBER2 = int(input("Enter second number: "))
    except ValueError:
        print("Not valid integer. TRY AGAIN!!")
        continue
    else:
        break

GIVEN_OPERATOR = input('Enter Operator [ + , - , / , * ]: ')


class Calculator:
    def __init__(self, x, y, operator):
        self.x = x
        self.y = y
        self.operator = operator
        self.selector()

    def add(self):
        ans = self.x + self.y
        return f"Summation is {ans}"

    def mul(self):
        return f"Multiplication is {self.x * self.y}"

    def div(self):
        try:
            ans = self.x / self.y
            return f"Division is {ans}"
        except ZeroDivisionError:
            return "Error: Division by zero!"

    def sub(self):
        return f"Subtract is {self.x - self.y}"

    def selector(self):
        if self.operator == "*":
            print(self.mul())
        elif self.operator == "/":
            print(self.div())
        elif self.operator == "-":
            print(self.sub())
        elif self.operator == "+":
            print(self.add())
        else:
            print("Please enter correct operator")


cal = Calculator(GIVEN_NUMBER1, GIVEN_NUMBER2, GIVEN_OPERATOR)




