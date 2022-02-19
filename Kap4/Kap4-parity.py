import time


def parity1_0(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    if result == 1:
        print("EVEN")
        return
    print("ODD")

def parity1_1(x):
    result = 0
    while x:
        result ^=1
        x &= x - 1
    if result == 1:
        print("EVEN")
        return
    print("ODD")    

def parity1_2(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    if x & 0x1 == 1:
        print("EVEN")
        return
    print("ODD")

def parity1_3(x):
    x = x | (x-1)
    print(bin(x))
    print(x)
    y = x % 64
    print(y)
    z = 1
    while z<y:
        z *=2
    if z == y:
        print("TRUE")
    else:
        print("FALSE")
#O(n) time
a = time.time()
parity1_0(100)
print(time.time() - a)


#O(k) time (number of ones)
a = time.time()
parity1_1(100)
print(time.time() - a)


a = time.time()
parity1_2(100)
print(time.time() - a)


parity1_3(81)
