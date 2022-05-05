import random
import math
random.seed(10)

blizje_srediscu = 0
n=5

for i in range(10**n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    do_sredisca = math.sqrt(x**2 + y**2)
    if (do_sredisca < 1 - x and do_sredisca < 1 + y and
        do_sredisca < 1 + x  and do_sredisca < 1 - y):
        blizje_srediscu += 1

    razmerje = blizje_srediscu / 10**n

print('Približek verjetnosti je ', razmerje)