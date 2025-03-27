# import threading
# import time
# import multiprocessing

# def fun1():
#     time.sleep(3)
#     print("fun1")

# def fun2():
#     time.sleep(3)
#     print("fun2")

# def fun3():
#     time.sleep(3)
#     print("fun3")

# if __name__=="__main__":
#     t1 = threading.Thread(target=fun1)
#     t2 = threading.Thread(target=fun2)
#     t3 = threading.Thread(target=fun3)
#     t1.start()
#     t2.start()
#     t3.start()
#     print("Total cores available: ",multiprocessing.cpu_count())

import multiprocessing
import multiprocessing.process
import time

def cpu_task():
    start = time.time()
    total = sum(i * i for i in range(10**8))  # Heavy CPU work
    print(f"Task done in {time.time() - start:.2f} seconds")

if __name__=="__main__":
    t1 = multiprocessing.Process(target=cpu_task)
    t2 = multiprocessing.Process(target=cpu_task) 
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()
