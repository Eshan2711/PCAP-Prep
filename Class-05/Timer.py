from torch.utils.throughput_benchmark import format_time

def format_time(h, m, s):
    return f"{h:02d}:{m:02d}:{s:02d}"

class Timer:
    def __init__(self,hours,mint,sec):
        self.__hours = hours
        self.__mint =  mint
        self.__sec =  sec
    def __str__(self):
        return format_time(self.__hours, self.__mint, self.__sec)
    def next_second(self):
        self.__sec += 1
        if self.__sec == 60:
            self.__sec = 0
            self.__mint +=1
        if self.__mint == 60:
            self.__mint = 0
            self.__hours += 1
        if self.__hours == 24:
            self.__hours = 0
    def prev_second(self):
        self.__sec -=1
        if self.__sec == -1:
            self.__sec = 59
            self.__mint -= 1
        if self.__mint == -1:
            self.__mint = 59
            self.__hours -= 1
        if self.__hours == -1:
            self.__hours = 23
#23:59:59
timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
