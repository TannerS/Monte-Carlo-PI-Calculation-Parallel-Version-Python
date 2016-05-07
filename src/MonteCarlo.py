from os import getpid
from multiprocessing import Pool
import random
from time import time

def CarloDeMonte(n):
    sum = 0
    area = 4
    min = 0
    max = 1
    x_ran = 0
    y_ran = 0

    for i in range(0, n):
        x_ran = random.uniform(min, max)
        y_ran = random.uniform(min, max)
        if(((x_ran**2) + (y_ran**2)) <= 1):
            sum += 1
    return ((area * sum) / n)

if __name__ == '__main__':
    n = int(input("Enter number of nodes: "))
    size = int(input("Enter the amount of random numbers: "))
    p = Pool(n)
    print 'size', size
    print 'cpu', n



    blocks = (int)(size / n)
    print 'blocks', blocks
    mod = size % n
    print 'mod', mod
    list = []

    for i in range(0, n):
        print 'loop'
        list.append(blocks)
    if(mod != 0)
    list.append(mod)
    t1 = time()
    result = p.map(CarloDeMonte, list)
    t2 = time()
    p.close()
    print('time take: {} seconds:'.format(t2 - t1))
    print('Result: {} '.format(result))



















