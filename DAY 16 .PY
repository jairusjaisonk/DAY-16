# class point:
#     def __init__(self,x = 0,y= 0):
#         self.x = x
#         self.y = y 

# from abc import ABC,abstractmethod
# class animal(ABC):
#     def __init__(self):
#         pass
#     # @abstractmethord
#     def makesound (self):
#         print('animal makes sounds')
# class Dog(animal):
#     def __init__(self):
#         pass
#     def makesound(self):
#         print("woff woof ")
# d= Dog()
# d.makesound()

# Q).Write a Python class Queue that implements a basic queue data structure with the enqueue
#  and dequeue methods. 
# The enqueue method should add an element to the rear of the queue, and the dequeue
#  method should remove and return the remaining element from the queue.
# Additionally, include a method is_empty to check if the queue is empty.


# class queue:
#     def __init__(self):
#         self.q = []
#     def enque(self):
#         while True:
#             a= input("enter an element(typr ' stop ' to finish):")
#             if a.lower() == ' stop ':
#                 break
#             self.q.append(a)
#             print(" current state:" , self.q)
#     def deque(self):
#         if len(self.q) == 0 :
#             print("queue is empty") 
#         else:
#             print("removed:", self.q.pop(0))
#             print(" current queue;",self.q)
# q = queue()
# q.enque()
# q.deque()


import time 
def totaltime(fun):
    def wrapper(*args,**kwargs):
        start= time.time
        fun(*args,**kwargs)
        stop = time.time