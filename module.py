import time
def f_square(n):
    for i in 5:
        time.sleep(0.5)
        print("square=",n*n)

def f_cube(m):
    for i in 5:
        time.sleep(0.7)
        print("cub=",n*n*n)
t1=threading.Thread(target=f_square,args=(5))
t2=threading.Thread(target=f_cude,args=(10))
t1.start()
t2.start()
t1.join()
t2.join()
