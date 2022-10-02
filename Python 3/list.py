import multiprocessing as mp
import time

starttime = time.time()

Result_1 = []
Result_2 = []
Result_3 = []

def Calculation_1():
    numbers = list(range(0, 10000000))
    for num in numbers:
        Result_1.append(num ** 0.5)
print(Result_1)
def Calculation_2():
    numbers = list(range(0, 10000000))
    for num in numbers:
        Result_2.append(num ** 2)

def Calculation_3():
    numbers = list(range(0, 10000000))
    for num in numbers:
        Result_3.append(num ** 3)

if __name__ == "__main__":

    p1 = mp.Process(target = Calculation_1)
    p2 = mp.Process(target = Calculation_2)
    p3 = mp.Process(target = Calculation_3)
    
    p1.start()
    p2.start()
    p3.start()
    
    p1.join()
    p2.join()
    p3.join()
    
    endtime = time.time()
    print("Time =", "{:.2f}".format((endtime - starttime) * (10 ** 3)), "ms")