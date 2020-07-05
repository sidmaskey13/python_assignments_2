# Imagine you are designing a banking application. What would a
# customer look like? What attributes would she have? What methods
# would she have?


class Bank:
    def __init__(self, name, address, gender, phone, balance):
        self.name = name
        self.address = address
        self.gender = gender
        self.phone = phone
        self.balance = balance

    def display_info(self):
        return f"""
-----------------------------------------
        Name: {self.name}
        Address: {self.address}
        Gender: {self.gender}
        Phone: {self.phone}
-----------------------------------------
        Balance: {self.balance}
        """

    def add_balance(self,x):
        self.balance += x
        return self.balance

    def withdraw_balance(self,x):
        self.balance -= x
        return self.balance

sid = Bank("Sid","baneshwor","male",9808888888,10000)
sita = Bank("Sita","koteshwor","female",9802222233,0)

sid.withdraw_balance(5000)
sita.add_balance(1200)

print(sid.display_info())
print(sita.display_info())


