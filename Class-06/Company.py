# # Company Role Management System using Python classes and inheritance.
# # The company has different types of employees:
# # Employee (base class)
# # Developer
# # Manager
# # HRManager (inherits from Manager)
# Create the Base Class Employee
# Create instance variables:
# name
# salary
# Create a class variable:
# total_employees (should count how many employee objects are created)
# The constructor must:
# Accept name and salary
# Increment total_employees
# Create a method
# work() → returns "General employee working"
# Override __str__() so that it returns:
# "Employee: <name>, Salary: <salary>
# 🔹 2️⃣ Create Class Developer
# Inherit from Employee
# Override work() → return "Writing code"
# Override __str__() using super() so output becomes:
# "Developer -> <parent __str__ output>"
# 🔹 3️⃣ Create Class Manager
# Inherit from Employee
# Override work() → return "Managing team"
# Override __str__() using super()
# 🔹 4️⃣ Create Class HRManager
# Inherit from Manager
# Override work() → return "Hiring employees"
# Override __str__() using super()
class Employee:
    total_employees = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        self.total_employees += 1
    def work(self):
        return "General Employee Working"
    def __str__(self):
        return "Employee:" + str(self.name) + "Salary:" + str(self.salary)
class Manager(Employee):
    def work(self):
        return "Manging team"
    def __str__(self):
        return "Manager -> Parent Class is: " + super().__str__()
class HRManager(Manager):
    def work(self):
        return "Hiring Employees"
    def __str__(self):
        return "HR_Manager -> Parent Class is: " + super().__str__()
class Developer(Employee):
    def work(self):
        return "Writing code"
    def __str__(self):
        return "Developer -> Parent Class is: " + super().__str__()
dev1 = Developer("Alice", 80000)
dev2 = Developer("Bob", 90000)
mgr1 = Manager("Charlie", 120000)
hr1 = HRManager("Diana", 110000)
print(dev1)
print(mgr1)
print(hr1)