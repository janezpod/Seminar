import random
import math
random.seed(10)

blizje_srediscu = 0
n= 3

for i in range(10**n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    do_sredisca = math.sqrt(x**2 + y**2)
    if (do_sredisca < 1 - x and do_sredisca < 1 + y and
        do_sredisca < 1 + x  and do_sredisca < 1 - y):
        blizje_srediscu += 1

    razmerje = blizje_srediscu / 10**n

print('Približek verjetnosti je ', razmerje)

#+-----+----------  +
#| n   | Rezultat   |        
#+=====+==========  +
#|  3  | 0.229      |
#|  4  | 0.2247     |
#|  5  | 0.21732    |
#+----------------  +
#|  6  | 0.218713   |
#|  7  | 0.2187818  |
#|  8  | 0.21904325 |  
#|-----+----------  +
# 
# Točna vrednost
# 0.2189514164974602 
