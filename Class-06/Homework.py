# 1:
    # 1: Apple Device is powered on. Making calls and browsing Dell Device is powered on. Running heavy Applications.
    #2: True , False
    #3:True , False
    #4: True , False
    #5: 2
    #6: 3
    #7: True , False
    #8: True , False
    #9:
        #class GamingLaptop(Laptop):
            # def __str__(self):
                #return "High performance gaming machine!"
    #10: It would work becasue it is still a subclass of device and methods are passed down from parent to child classes
#2:
class Person:
    total_people = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.total_people += 1
    def get_role(self):
        return "Person"
    def activity(self):
        return "Doing general activities"
    def __str__(self):
        return f"Person: {self.name}, Age: {self.age}"
class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major
    def get_role(self):
        return "Student"
    def activity(self):
        return f"Studying {self.major}"
    def __str__(self):
        return f"Student -> {super().__str__()}, Major: {self.major}"
class Professor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department
    def get_role(self):
        return "Professor"
    def activity(self):
        return f"Teaching in {self.department} department"
    def __str__(self):
        return f"Professor -> {super().__str__()}, Department: {self.department}"
class ResearchProfessor(Professor):
    def __init__(self, name, age, department, research_field):
        super().__init__(name, age, department)
        self.research_field = research_field
    def get_role(self):
        return "Research Professor"
    def activity(self):
        return f"Researching {self.research_field}"
    def __str__(self):
        return f"Research Professor -> {super().__str__()}, Research Field: {self.research_field}"
s1 = Student("Alice", 20, "Computer Science")
s2 = Student("Bob", 22, "Mathematics")
p1 = Professor("Dr. Smith", 45, "Physics")
rp1 = ResearchProfessor("Dr. Brown", 50, "Biology", "Genetics")
print(s1)
print(p1)
print(rp1)
print(issubclass(Student, Person))
print(issubclass(ResearchProfessor, Professor))
print(issubclass(Professor, Student))
print(isinstance(s1, Person))
print(isinstance(rp1, Professor))
print(isinstance(p1, Student))
print(s1 is s2)
print(s1 is s1)
print(Person.total_people)
# Person.total_people increases by 1 every time a Person (or subclass)  is created.
print(s1.activity())
print(p1.activity())
print(rp1.activity())
#Becasue we overided them in the different subclasses
university = [s1, s2, p1, rp1]
for person in university:
    print(person)
    print(person.get_role())
    print(person.activity())
#3:
class Account:
    total_accounts = 0
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = balance
        Account.total_accounts += 1
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}"
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrawn {amount}"
        return "Insufficient funds"
    def account_type(self):
        return "Generic Account"
    def __str__(self):
        return f"Account Holder: {self.holder_name}, Balance: {self.balance}"
class SavingsAccount(Account):
    def __init__(self, holder_name, balance, interest_rate):
        super().__init__(holder_name, balance)
        self.interest_rate = interest_rate
    def account_type(self):
        return "Savings Account"
    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
        return "Interest applied"
    def __str__(self):
        return f"Savings -> {super().__str__()}, Rate: {self.interest_rate}"
class CurrentAccount(Account):
    def __init__(self, holder_name, balance, overdraft_limit):
        super().__init__(holder_name, balance)
        self.overdraft_limit = overdraft_limit
    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            return f"Withdrawn {amount}"
        return "Insufficient funds"
    def account_type(self):
        return "Current Account"
    def __str__(self):
        return f"Current -> {super().__str__()}, Overdraft: {self.overdraft_limit}"
class PremiumCurrentAccount(CurrentAccount):
    def account_type(self):
        return "Premium Current Account"
    def withdraw(self, amount):
        self.balance -= amount
        return f"Withdrawn {amount}"
    def __str__(self):
        return f"Premium -> {super().__str__()}"
acc1 = SavingsAccount("Alice", 1000, 0.10)
acc2 = CurrentAccount("Bob", 500, 300)
acc3 = PremiumCurrentAccount("Charlie", 200, 500)
print(acc1)
print(acc2)
print(acc3)
print(issubclass(SavingsAccount, Account))
print(issubclass(PremiumCurrentAccount, CurrentAccount))
print(issubclass(CurrentAccount, SavingsAccount))
print(isinstance(acc1, Account))
print(isinstance(acc3, CurrentAccount))
print(isinstance(acc2, SavingsAccount))
print(acc1 is acc2)
print(acc3 is acc3)
print(acc1.deposit(500))
print(acc1.withdraw(200))
print(acc2.withdraw(700))
print(acc3.withdraw(10000))
print(Account.total_accounts)
bank_accounts = [acc1, acc2, acc3]
for acc in bank_accounts:
    print(acc)
    print(acc.account_type())