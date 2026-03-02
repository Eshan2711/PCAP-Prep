class Queue:
    def __init__(self):
        self.__queue_list = []
    def put(self,num):
        self.__queue_list.append(num)
    def get(self):
        a=self.__queue_list[0]
        del self.__queue_list[0]
        return a
    def is_empty(self):
        return len(self.__queue_list) == 0
s1=Queue()
for x in range (20):
    s1.put(x)
for x in range (10):
    print(s1.get())

