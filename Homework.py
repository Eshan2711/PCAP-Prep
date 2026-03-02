#Class 2:
#1:
class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
counter=Counter()
counter.increment()
print(counter.count)
#2:
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
student = Student("Eshan", 15)
print("Name:", student.name)
print("Age:", student.age)
#3:
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
rect = Rectangle(5, 4)
print(rect.area())
#4:
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print(account.balance)
#5:
class Phone:
    def __init__(self):
        self.battery = 100

    def call(self):
        self.battery -= 10
phone = Phone()
phone.call()
print(phone.battery)
#7:
class Engine:
    def start(self):
        print("Engine Started")
class Car():
    def __init__(self):
        self.engine = Engine()
    def start_car(self):
        self.engine.start()
car=Car()
car.start_car()
#8:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
p1 = Point(3, 4)
p2 = Point(3, 4)
print("p1 == p2:", p1 == p2)
print("p1 is p2:", p1 is p2)
#9:
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def increment_salary(self,percent):
        self.salary +=  self.salary * (percent/100)
emp = Employee("Alice", 50000)
emp.increment_salary(10)
print(emp.name)
print(emp.salary)
#10:
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    def discount(self):
        self.price = self.price * 0.8
b1 = Book("Eshan", 100)
b1.discount()
print(b1.title)
print(b1.price)
#11:
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def show_balance(self):
        return self.balance
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print("Balance:", account.show_balance())
#12:
class LimitedCounter:
    def __init__(self, limit):
        self.count = 0
        self.limit = limit
    def increment(self):
        if self.count < self.limit:
            self.count += 1
        else:
            print("Limit reached")
counter = LimitedCounter(3)
counter.increment()
print(counter.count)
#13:
class Course:
    def __init__(self, course_name):
        self.course_name = course_name
class Student:
    def __init__(self, name):
        self.name = name
        self.course = None
    def enroll(self, course):
        self.course = course
    def show_course(self):
        print(self.name, "is enrolled in", self.course.course_name)
course1 = Course("Computer Science")
student1 = Student("Eshan")
student1.enroll(course1)
student1.show_course()
#14:
class Laptop:
    def __init__(self, brand):
        self.brand = brand
l1 = Laptop("Dell")
l2 = l1
print("l1 is l2:", l1 is l2)
#15:
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
class Member:
    def __init__(self, name, member_id, borrowed_book=None):
        self.name = name
        self.member_id = member_id
        self.borrowed_book = borrowed_book
    def borrow_book(self, book):
        self.borrowed_book = book
    def show_book(self):
        print(self.name, "borrowed", self.borrowed_book.title)
class Library:
    def __init__(self, name, location, books):
        self.name = name
        self.location = location
        self.books = books
    def show_books(self):
        for book in self.books:
            print(book.title)
b1 = Book("Hi", "John", 20)
b2 = Book("Eshan", "John", 25)
#Class 3:
#1:
stack=[]
def push(num):
    stack.append(num)
def pop():
    del stack[-1]
def top():
    return stack[-1]
def peek():
    if len(stack) == ():
        print("Stack is empty. Nothing to peek.")
    else:
        print("Top element is", stack[-1])
push(1)
pop()
push(10)
top()
peek()
print(stack)
#2:
stack.append(99)
stack.pop(0)

print("Stack after insecure access:", stack)
#3:
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, num):
        self.stack.append(num)
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty. Cannot pop.")
        else:
            del self.stack[-1]
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty. Nothing to peek.")
        else:
            print("Top element is", self.stack[-1])
    def is_empty(self):
        return len(self.stack) == 0
s = Stack()
s.push(1)
s.pop()
s.push(10)
s.peek()
print(s.is_empty())
#4:
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
b1 = Book("Python Basics", 500)
#5:
class Init:
    def __init__(self):
        print("__init__() method is called automatically")
s1 = Init()
#6:
class MyClass:
    def __init__(self):
        self.secret = 42
obj = MyClass()
print(obj.secret)
#7:
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def get_balance(self):
        return self.balance
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
account.get_balance()
print(account.balance)
#8:
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, num):
        self.stack.append(num)
    def pop(self):
        val=self.stack[-1]
        del self.stack[-1]
        return val
    def is_empty(self):
        return len(self.stack) == 0
def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    result = ""
    while not stack.is_empty():
        popped_char = stack.pop()
        if popped_char is not None:
            result += popped_char
    return result
print(reverse_string("Eshan"))
#Class 04:
#1,2, and 3:
class Queue:
    def __init__(self):
        self.__queue_list = []
    def put(self,num):
        self.__queue_list.append(num)
    def get(self):
        if len(self.__queue_list)==0:
            print("Queue is empty")
            return None
        else:
            a=self.__queue_list[0]
            del self.__queue_list[0]
            print(a)
    def is_empty(self):
        if len(self.__queue_list) == 0:
            return len(self.__queue_list) == 0
            return None
    def size(self):
        return len(self.__queue_list)
q=Queue()
q.put("Eshan")
q.put("Sara")
q.put("Amit")
q.get()
q.get()
q.get()
#5:
class Queue:
    def __init__(self):
        self.queue_list = []
    def put(self,num):
        self.queue_list.append(num)
    def get(self):
        if len(self.queue_list)==0:
            print("Queue is empty")
            return None
        else:
            a=self.queue_list[0]
            del self.queue_list[0]
            return a
    def is_empty(self):
        if len(self.queue_list) == 0:
            return len(self.queue_list) == 0
        return False
    def size(self):
        return len(self.queue_list)
class Stack:
    def __init__(self):
        self.s = []

    def push(self, x):
        self.s.append(x)

    def pop(self):
        a=self.s[-1]
        del self.s[-1]
        return a

    def is_empty(self):
        return len(self.s) == 0

def reverse_queue(q):
    s = Stack()
    while not d.is_empty():
        s.push(q.get())
    while not s.is_empty():
        q.put(s.pop())

d=Queue()
d.put(1)
d.put(2)
d.put(3)
reverse_queue(d)
while not d.is_empty():
    print(d.get())