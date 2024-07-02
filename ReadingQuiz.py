# Running code for the reading quiz

from random import uniform
from statistics import mean
from timeit import default_timer as timer

t0 = timer()
mean(uniform(0, 10) for i in range(1000000))
t1 = timer()

print(t1-t0)
