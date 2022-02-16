print(bin(100))
print(100)
#Python solution
print(bin(int('{:64b}'.format(100)[::-1], 2)))
print(int('{:64b}'.format(100)[::-1], 2))

def swap_bits(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i ) | (1 << j)
        x ^= bit_mask        
    return x
x = 100
print(bin(100))
j = len(bin(x)[2:])-1 
for i in range((len(bin(x)[2:])+1)//2):
    x = swap_bits(x, i, j)
    j -= 1
print(x)
print(bin(x))