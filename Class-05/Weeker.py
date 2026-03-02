class Weeker:
    __days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

    def __init__(self,day):
        self.day = day
        self.ind = self.__days.index(day)
    def __str__(self):
        return self.day
    def add_days(self, n):
        a = (self.ind +n) % 7
        self.day = self.__days[a]
    def subtract_days(self, n):
        a = (self.ind - n) % 7
        self.day = self.__days[a]
try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except ValueError:
    print("Sorry, I can't serve your request.")