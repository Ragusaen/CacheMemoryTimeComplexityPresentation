import math
import matplotlib.pyplot as plt


def f(n: int):
    return sum(n / (2**(i - 1)) * math.sqrt(2**i) for i in range(1, int(math.log2(n))))

def g(n: int):
    return sum((n) / (i) * math.sqrt(i+1) for i in range(1, n))

plt.plot([f(n) for n in range(1, 1000000)])
# plt.plot([n * math.sqrt(n) for n in range(1, 1000)])
plt.show()
