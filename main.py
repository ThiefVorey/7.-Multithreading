import funcat as ct
import threading as th
import time
import keyboard
class Thr1(th.Thread): # Создаём экземпляр потока Thread
    def __init__(self, var):
        th.Thread.__init__(self)
        self.daemon = True # Указываем, что этот поток - демон
        self.var = var # это интервал, передаваемый в качестве аргумента

    def run(self): # метод, который выполняется при запуске потока
        num = 1.0
        while True:
            if keyboard.is_pressed('q'):
                print('конец поток 1')
                break
            ct.VETDATE.vetinput()
            time.sleep(self.var) # Ждём указанное количество секунд
class Thr2(th.Thread): # Создаём экземпляр потока Thread
    def __init__(self, var):
        th.Thread.__init__(self)
        self.daemon = True # Указываем, что этот поток - демон
        self.var = var # это интервал, передаваемый в качестве аргумента

    def run(self): # метод, который выполняется при запуске потока
        num = 1.0
        while True:
            if keyboard.is_pressed('w'):
                print('конец поток 2')
                break
            ct.VETDATE.nobus()
            time.sleep(self.var) # Ждём указанное количество секунд
class Thr3(th.Thread): # Создаём экземпляр потока Thread
    def __init__(self, var):
        th.Thread.__init__(self)
        self.daemon = True # Указываем, что этот поток - демон
        self.var = var # это интервал, передаваемый в качестве аргумента

    def run(self): # метод, который выполняется при запуске потока
        num = 1.0
        while True:
            if keyboard.is_pressed('e'):
                print('конец поток 3')
                break            
            ct.CATDATE.catinput()
            time.sleep(self.var) # Ждём указанное количество секунд
class Thr4(th.Thread): # Создаём экземпляр потока Thread
    def __init__(self, var):
        th.Thread.__init__(self)
        self.daemon = True # Указываем, что этот поток - демон
        self.var = var # это интервал, передаваемый в качестве аргумента

    def run(self): # метод, который выполняется при запуске потока
        num = 1.0
        while True:
            if keyboard.is_pressed('r'):
                print('конец поток 4')
                break            
            ct.treatment.gear()
            time.sleep(self.var) # Ждём указанное количество секунд
x = Thr1(3.0)
z = Thr2(1.1)
y = Thr3(3.9)
v = Thr4(6.0)
x.start()
z.start()
y.start()
v.start()


