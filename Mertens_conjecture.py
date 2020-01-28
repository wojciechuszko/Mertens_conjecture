import numpy as np
import matplotlib.pyplot as plt
n = int(input("Enter a positive integer: "))
moebius = []
moebius.append(1)

for i in np.arange(2,n+1,1):
    j = 2
    prime_factors = []
    while j * j <= i:
        if i % j != 0:
            j += 1
        else:
            i //= j
            prime_factors.append(j)
    if i > 1:
        prime_factors.append(i) 

    if len(prime_factors) != len(np.unique(prime_factors)):
        moebius.append(0)
    elif len(prime_factors) % 2 == 0:
        moebius.append(1)
    else:
        moebius.append(-1)

mertens = []
mertens.append(1)
for k in np.arange(1,n,1):
    mertens.append(moebius[k] + mertens[k-1])

x = np.linspace(0,n,1000)
sqrt_plus = x**0.5
sqrt_minus = -x**0.5

plt.figure()
plt.plot(x, sqrt_plus, 'r-', label='+/- square root')
plt.plot(x, sqrt_minus, 'r-')
plt.plot(np.arange(1,n+1,1), mertens, 'b-', label='Mertens function')
plt.legend(loc='upper left')
plt.show()
