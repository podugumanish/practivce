# # # # # # # # # # # # # # # # # # # multithread
# # # # # # # # # # # # # # # # # # import threading
# # # # # # # # # # # # # # # # # # print('checking current thread',threading.current_thread().getName())

# # # # # # # # # # # # # # # # # # # creating threads in python without using any class where we are unsure of the ordering of the executions 
# # # # # # # # # # # # # # # # # # from threading import *
# # # # # # # # # # # # # # # # # # def display():
# # # # # # # # # # # # # # # # # #     for i in range(1,11):
# # # # # # # # # # # # # # # # # #         print(f'child thread=>{i}')

# # # # # # # # # # # # # # # # # # t =Thread(target=display)
# # # # # # # # # # # # # # # # # # # t.start()

# # # # # # # # # # # # # # # # # # for i in range(1,11):
# # # # # # # # # # # # # # # # # #     # print('Main Thread')
# # # # # # # # # # # # # # # # # #     pass

# # # # # # # # # # # # # # # # # # # creating thread by extending thread class
# # # # # # # # # # # # # # # # # # class MyThread(Thread):
# # # # # # # # # # # # # # # # # #     # overriding run() method in superclass 
# # # # # # # # # # # # # # # # # #     def run(self):
# # # # # # # # # # # # # # # # # #         for i in range(10) :
# # # # # # # # # # # # # # # # # #             print('child Thread')

# # # # # # # # # # # # # # # # # # t= MyThread()
# # # # # # # # # # # # # # # # # # # t.start()
# # # # # # # # # # # # # # # # # # for i in range(10):
# # # # # # # # # # # # # # # # # #     # print('Main Thread')
# # # # # # # # # # # # # # # # # #     pass

# # # # # # # # # # # # # # # # # # # creating thread without extending thread class
# # # # # # # # # # # # # # # # # # from threading import *
# # # # # # # # # # # # # # # # # # class Test:
# # # # # # # # # # # # # # # # # #     def display(self):
# # # # # # # # # # # # # # # # # #         for i in range(10):
# # # # # # # # # # # # # # # # # #             print(f'child Thread{i}')
# # # # # # # # # # # # # # # # # # obj = Test()
# # # # # # # # # # # # # # # # # # t = Thread(target=obj.display)
# # # # # # # # # # # # # # # # # # # t.start()
# # # # # # # # # # # # # # # # # # for i in range(10):
# # # # # # # # # # # # # # # # # #     # print(f'main thread {i}')
# # # # # # # # # # # # # # # # # #     pass

# # # # # # # # # # # # # # # # # # # creating multiple child threads
# # # # # # # # # # # # # # # # # # class Thread1:
# # # # # # # # # # # # # # # # # #     def functhread1(self):
# # # # # # # # # # # # # # # # # #         for i in range (10):
# # # # # # # # # # # # # # # # # #             print(f'functhread1=> {i}')
# # # # # # # # # # # # # # # # # # class Thread2:
# # # # # # # # # # # # # # # # # #     def functhread2(self):
# # # # # # # # # # # # # # # # # #         for i in range (10):
# # # # # # # # # # # # # # # # # #             print(f'functhread2=> {i}')
# # # # # # # # # # # # # # # # # # import time
# # # # # # # # # # # # # # # # # # begin =time.time()
# # # # # # # # # # # # # # # # # # print('checking beginning',begin)
# # # # # # # # # # # # # # # # # # Tar1,Tar2 = Thread1(),Thread2()
# # # # # # # # # # # # # # # # # # T1,T2 =Thread(target=Tar1.functhread1),Thread(target=Tar2.functhread2)
# # # # # # # # # # # # # # # # # # T1.start()
# # # # # # # # # # # # # # # # # # l = enumerate()
# # # # # # # # # # # # # # # # # # for t in l:
# # # # # # # # # # # # # # # # # #     print(t.name)
# # # # # # # # # # # # # # # # # # T2.start()
# # # # # # # # # # # # # # # # # # T1.join()
# # # # # # # # # # # # # # # # # # print(active_count())
# # # # # # # # # # # # # # # # # # T2.join()
# # # # # # # # # # # # # # # # # # print('timetaken total',time.time()-begin)
# # # # # # # # # # # # # # # # # # print(T2.name,"is Alive :",T2.isAlive())

# # # # # # # # # # # # # # # # # # # setting and getting names of thread
# # # # # # # # # # # # # # # # # # print(current_thread().getName())
# # # # # # # # # # # # # # # # # # print(current_thread().setName('Manish'))
# # # # # # # # # # # # # # # # # # print(current_thread().getName())
# # # # # # # # # # # # # # # # # # print(current_thread().name,current_thread().ident)

# # # # # # # # # # # # # # # # # # # active_count()
# # # # # # # # # # # # # # # # # # print(active_count())

# # # # # # # # # # # # # # # # # # l = enumerate()
# # # # # # # # # # # # # # # # # # for t in l:
# # # # # # # # # # # # # # # # # #     print(t.name)

# # # # # # # # # # # # # # # # # from threading import * 
# # # # # # # # # # # # # # # # # import time 
# # # # # # # # # # # # # # # # # def display(): 
# # # # # # # # # # # # # # # # #     for i in range(10): 
# # # # # # # # # # # # # # # # #         print("Seetha Thread") 
# # # # # # # # # # # # # # # # #     # time.sleep(2) 

# # # # # # # # # # # # # # # # # t1=Thread(target=display) 
# # # # # # # # # # # # # # # # # t2=Thread(target=display) 
# # # # # # # # # # # # # # # # # t1.start() 
# # # # # # # # # # # # # # # # # t2.start()
# # # # # # # # # # # # # # # # # t2.join(2)#This Line executed by Main Thread 
# # # # # # # # # # # # # # # # # for i in range(10): 
# # # # # # # # # # # # # # # # #      print("Rama Thread")

# # # # # # # # # # # # # # # # from threading import *
# # # # # # # # # # # # # # # # def job():
# # # # # # # # # # # # # # # #     for i in range(190):
# # # # # # # # # # # # # # # #         print('hello')
# # # # # # # # # # # # # # # # t = Thread(target=job)
# # # # # # # # # # # # # # # # # Garbage collection works as daemon thread at runtime when there is a memory suffciency issues occur in PVM
# # # # # # # # # # # # # # # # print(t.isDaemon())
# # # # # # # # # # # # # # # # t.setDaemon(True)
# # # # # # # # # # # # # # # # print(t.isDaemon())
# # # # # # # # # # # # # # # # whenever lasty non daemon thread terminates for that partiuclar program then daemon runruntime terminates for same.
# # # # # # # # # # # # # # # from threading import * 
# # # # # # # # # # # # # # # import time 
# # # # # # # # # # # # # # # def job(): 
# # # # # # # # # # # # # # #     for i in range(10): 
# # # # # # # # # # # # # # #         print("Lazy Thread") 
# # # # # # # # # # # # # # #     time.sleep(2) 

# # # # # # # # # # # # # # # t=Thread(target=job) 
# # # # # # # # # # # # # # # #t.setDaemon(True)===>Line-1 
# # # # # # # # # # # # # # # t.start() 
# # # # # # # # # # # # # # # time.sleep(5) 
# # # # # # # # # # # # # # # print("End Of Main Thread")


# # # # # # # # # # # # # # # focusing on syncronization activities
# # # # # # # # # # # # # # from threading import *
# # # # # # # # # # # # # # import time
# # # # # # # # # # # # # # def wish(n):
# # # # # # # # # # # # # #     for i in range(10):
# # # # # # # # # # # # # #         print('good evening',end='')
# # # # # # # # # # # # # #         time.sleep(2)
# # # # # # # # # # # # # #         print(n)
# # # # # # # # # # # # # # t1,t2=Thread(target=wish,args=('manish',)),Thread(target=wish,args=('vikash',))
# # # # # # # # # # # # # # t1.start()
# # # # # # # # # # # # # # t2.start()


# # # # # # # # # # # # # # syncronization for removing incosistancy mostly used in transactions actions running in parallel
# # # # # # # # # # # # # # lock can be occupied by only one thread and once relased can be used by others acquire(), release()
# # # # # # # # # # # # # from threading import *
# # # # # # # # # # # # # # l = Lock()
# # # # # # # # # # # # # # def madd():
# # # # # # # # # # # # # #     l.acquire()
# # # # # # # # # # # # # #     for i in range(10):
# # # # # # # # # # # # # #         print('all',i)
# # # # # # # # # # # # # #     l.release()

# # # # # # # # # # # # # # madd()
# # # # # # # # # # # # # #  RLock for recurring functions and availavble for only owner thread and not for others
# # # # # # # # # # # # # # number of acquire and numbner of release should match
# # # # # # # # # # # # # # The below are working for single threaded functions
# # # # # # # # # # # # # R = RLock()
# # # # # # # # # # # # # R.acquire()
# # # # # # # # # # # # # R.acquire()
# # # # # # # # # # # # # R.release()
# # # # # # # # # # # # # R.release()

# # # # # # # # # # # # # # for multithreaded function reuqreiments semaphonre
# # # # # # # # # # # # # # the below can handle 3 threads for lock and acquire
# # # # # # # # # # # # # import time
# # # # # # # # # # # # # s= Semaphore(3)
# # # # # # # # # # # # # def wish(name):
# # # # # # # # # # # # #     s.acquire()
# # # # # # # # # # # # #     for i in range(10):
# # # # # # # # # # # # #         print('good word')
# # # # # # # # # # # # #         time.sleep(2)
# # # # # # # # # # # # #         print(name)

# # # # # # # # # # # # #     s.release()
# # # # # # # # # # # # # t1=Thread(target=wish,args=("Dhoni",)) 
# # # # # # # # # # # # # t2=Thread(target=wish,args=("Yuvraj",)) 
# # # # # # # # # # # # # t3=Thread(target=wish,args=("Kohli",)) 
# # # # # # # # # # # # # t4=Thread(target=wish,args=("Rohit",)) 
# # # # # # # # # # # # # t5=Thread(target=wish,args=("Pandya",)) 
# # # # # # # # # # # # # t1.start() 
# # # # # # # # # # # # # t2.start() 
# # # # # # # # # # # # # t3.start() 
# # # # # # # # # # # # # t4.start() 
# # # # # # # # # # # # # t5.start()
# # # # # # # # # # # # # # incase bounded semaphore relese should be equal to acquired
# # # # # # # # # # # # from threading import *
# # # # # # # # # # # # s =Semaphore(2)
# # # # # # # # # # # # s.acquire()
# # # # # # # # # # # # s.acquire()
# # # # # # # # # # # # s.release()
# # # # # # # # # # # # s.release()
# # # # # # # # # # # # s.release()

# # # # # # # # # # # # s =BoundedSemaphore(2)
# # # # # # # # # # # # s.acquire()
# # # # # # # # # # # # s.acquire()
# # # # # # # # # # # # s.release()
# # # # # # # # # # # # s.release()
# # # # # # # # # # # # # s.release()

# # # # # # # # # # # # # inter-thread communication where event will be set to true than event occurs else wait() else clear() to turn to false so no event will occur
# # # # # # # # # # # # import threading
# # # # # # # # # # # # event = threading.Event()
# # # # # # # # # # # # #consumer thread has to wait until event is set
# # # # # # # # # # # # # event.wait()
# # # # # # # # # # # # # #producer thread can set or clear event
# # # # # # # # # # # # # event.set()
# # # # # # # # # # # # # event.clear()


# # # # # # # # # # # # # practical of inter-thread communication
# # # # # # # # # # # # def producer():
# # # # # # # # # # # #     print("Producer producing items")
# # # # # # # # # # # #     print('notifying by setting the event')
# # # # # # # # # # # #     event.set()

# # # # # # # # # # # # def consumer():
# # # # # # # # # # # #     print('Consumer thread waiting for the updation')
# # # # # # # # # # # #     event.wait()
# # # # # # # # # # # #     print('Got notification and consuming ')

# # # # # # # # # # # # t1 =Thread(target=consumer)
# # # # # # # # # # # # t2= Thread(target=producer)
# # # # # # # # # # # # t1.start()
# # # # # # # # # # # # t2.start()
# # # # # # # # # # # # import time
# # # # # # # # # # # # # requirement: Traffic and timeline green-> 10, red ->20
# # # # # # # # # # # # def traffic():

# # # # # # # # # # # #     time.sleep(10)
# # # # # # # # # # # #     print('Green signal')
# # # # # # # # # # # #     event.set()
# # # # # # # # # # # #     time.sleep(20)
# # # # # # # # # # # #     print('Red signal')
# # # # # # # # # # # #     event.clear()

# # # # # # # # # # # # def driver():
# # # # # # # # # # # #     num = 0
# # # # # # # # # # # #     while True:
# # # # # # # # # # # #         print('driver waiting for signal')
# # # # # # # # # # # #         event.wait()
# # # # # # # # # # # #         print('Traffic signal green.. vehicle can move')
# # # # # # # # # # # #         event.is_set()

# # # # # # # # # # # #         num = num+1
# # # # # # # # # # # #         print('vehicle no',num,'crossing the signal')
# # # # # # # # # # # #         time.sleep(2)
# # # # # # # # # # # # event = Event()
# # # # # # # # # # # # # t1 = Thread(target=traffic)
# # # # # # # # # # # # # t2 = Thread(target=driver)
# # # # # # # # # # # # # t1.start()
# # # # # # # # # # # # # t2.start()


# # # # # # # # # # # # conditioned events with help of state change
# # # # # # # # # # # # acquire() and release() wait() notify() notifyall()



# # # # # # # # # # # from threading import * 
# # # # # # # # # # # def consume(c): 
# # # # # # # # # # #     c.acquire() 
# # # # # # # # # # #     print("Consumer waiting for updation") 
# # # # # # # # # # #     c.wait() 
# # # # # # # # # # #     print("Consumer got notification & consuming the item") 
# # # # # # # # # # #     c.release() 

# # # # # # # # # # # def produce(c): 
# # # # # # # # # # #  c.acquire() 
# # # # # # # # # # #  print("Producer Producing Items") 
# # # # # # # # # # #  print("Producer giving Notification") 
# # # # # # # # # # #  c.notify() 
# # # # # # # # # # #  c.release() 

# # # # # # # # # # # c=Condition() 
# # # # # # # # # # # t1=Thread(target=consume,args=(c,)) 
# # # # # # # # # # # t2=Thread(target=produce,args=(c,)) 
# # # # # # # # # # # t1.start() 
# # # # # # # # # # # t2.start()
# # # # # # # # # # from threading import * 
# # # # # # # # # # import time 
# # # # # # # # # # import random 
# # # # # # # # # # items=[] 
# # # # # # # # # # def produce(c): 
# # # # # # # # # #     while True: 
# # # # # # # # # #         c.acquire() 
# # # # # # # # # #         item=random.randint(1,100) 
# # # # # # # # # #         print("Producer Producing Item:",item) 
# # # # # # # # # #         items.append(item) 
# # # # # # # # # #         print("Producer giving Notification") 
# # # # # # # # # #         c.notify() 
# # # # # # # # # #         c.release() 
# # # # # # # # # #         time.sleep(5) 
 
# # # # # # # # # # def consume(c): 
# # # # # # # # # #     while True: 
# # # # # # # # # #         c.acquire() 
# # # # # # # # # #         print("Consumer waiting for updation") 
# # # # # # # # # #         c.wait() 
# # # # # # # # # #         print("Consumer consumed the item",items.pop()) 
# # # # # # # # # #         c.release() 
# # # # # # # # # #         time.sleep(5) 
 
# # # # # # # # # # c=Condition() 
# # # # # # # # # # t1=Thread(target=consume,args=(c,)) 
# # # # # # # # # # t2=Thread(target=produce,args=(c,)) 
# # # # # # # # # # t1.start() 
# # # # # # # # # # t2.start()

# # # # # # # # # from threading import * 
# # # # # # # # # import time 
# # # # # # # # # lock=Lock() 
# # # # # # # # # def wish(name): 
# # # # # # # # #     with lock: 
# # # # # # # # #         for i in range(10): 
# # # # # # # # #             print("Good Evening:",end='') 
# # # # # # # # #             time.sleep(2) 
# # # # # # # # #             print(name) 
# # # # # # # # # t1=Thread(target=wish,args=("Dhoni",)) 
# # # # # # # # # t2=Thread(target=wish,args=("Yuvraj",)) 
# # # # # # # # # t3=Thread(target=wish,args=("Kohli",)) 
# # # # # # # # # t1.start() 
# # # # # # # # # t2.start() 
# # # # # # # # # t3.start() 


# # # # # # # # # file handling
# # # # # # # # # modes -> r,r+,w+,w,a,a+, x
# # # # # # # # with  open('abc.txt','w') as f:
# # # # # # # #     f.write('mad')
# # # # # # # #     f.write('maddy')
# # # # # # # #     f.write('maddy2')
    
    


# # # # # # # # import os
# # # # # # # # if os.path.isfile('abc.txt'):
# # # # # # # # # print(a)

# # # # # # # #     with  open('abc.txt','r+') as f:
# # # # # # # #         reading = f.read() 
# # # # # # # #         print(reading)
# # # # # # # #         print("The Current Cursor Position: ",f.tell())
# # # # # # # #         f.seek(200) 
# # # # # # # #         print("The Current Cursor Position: ",f.tell())

# # # # # # # #         # for i in reading:
# # # # # # # #         #     print(i,'hjellp')

# # # # # # # import os,sys 
# # # # # # # fname=input("Enter File Name: ") 
# # # # # # # if os.path.isfile(fname): 
# # # # # # #     print("File exists:",fname) 
# # # # # # #     f=open(fname,"r") 
# # # # # # # else: 
# # # # # # #     print("File does not exist:",fname) 
# # # # # # #     sys.exit(0) 
# # # # # # # lcount=wcount=ccount=0 
# # # # # # # for line in f: 
# # # # # # #  lcount=lcount+1 
# # # # # # #  ccount=ccount+len(line) 
# # # # # # #  words=line.split() 
# # # # # # #  wcount=wcount+len(words) 
# # # # # # #  print("The number of Lines:",lcount) 
# # # # # # #  print("The number of Words:",wcount) 
# # # # # # #  print("The number of characters:",ccount) 

# # # # # # # f1 = open('newplot.png','rb')
# # # # # # # f2 = open('upcom.png','wb')
# # # # # # # byter = f1.read()
# # # # # # # f2.write(byter)
# # # # # # import csv
# # # # # # with open('mad.csv','w',newline='') as f:
# # # # # #     w = csv.writer(f)
# # # # # #     w.writerow(['mad','xad'])
# # # # # #     w.writerow([1,2])
# # # # # # with open('mad.csv','r') as f:
# # # # # #     rea = csv.reader(f)
# # # # # #     for i in rea:
# # # # # #         print(i)
# # # # from zipfile import *
# # # # # f= ZipFile('file.zip','w',ZIP_DEFLATED)
# # # # # f.write('mad.csv')
# # # # # f.write('upcom.png')
# # # # # f.close()

# # # # f= ZipFile('file.zip','r',ZIP_STORED)
# # # # names = f.namelist()
# # # # for i in names:
# # # #     print('file name',i)
# # # #     f1 = open(i,'r')
# # # #     print(f1.read())

# # import os
# # # print(os.getcwd())
# # # # if  not os.mkdir("mysub"):
# # # #     os.mkdir("mysub")
# # # os.makedirs("sub1/sub2/sub3")
# # # os.rename('mysub','newdir')
# # print(os.listdir("."))
# # for dirpath,dirnames,filenames in os.walk('.'):
# #     print(dirpath,dirnames,filenames)
# # stats = os.stat("abc.txt")
# # print(stats)
# # process of writing state of object is called pcikling and reading the same called unpickling
# class Employee: 
#     def __init__(self,eno,ename,esal,eaddr): 
#         self.eno=eno; 
#         self.ename=ename; 
#         self.esal=esal; 
#         self.eaddr=eaddr; 
#     def display(self): 

#         print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.eaddr) 

# import pickle
# f=open("emp.dat","wb")
# n=int(input("Enter The number of Employees:")) 
# for i in range(n): 
#     eno=int(input("Enter Employee Number:")) 
#     ename=input("Enter Employee Name:") 
#     esal=float(input("Enter Employee Salary:")) 
#     eaddr=input("Enter Employee Address:") 
#     e=Employee(eno,ename,esal,eaddr) 
#     pickle.dump(e,f)
# f=open("emp.dat","rb") 
# while True:
#     try: 
#         obj=pickle.load(f)
#     except EOFError:
#         print('done')
# # e = Employee('manish','rayagada')
# # with open('mad.dat','wb') as f:
# #     add = pickle.dump(e,f)
# # with open('mad.dat','rb') as f:
# #     add = pickle.load(f)
# #     add.display()
# set,dict,list are mutable
a = {'+a+':1}
print(a['+a+'])
print(type(a))
a = {1}
a = frozenset(a)
# froset will add validation policy to condition of the set usage
a,b=[1],[1]
print(a is b,a==b)
# pylint check code standard