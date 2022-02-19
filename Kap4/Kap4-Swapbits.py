def swap_bits(x,i,j):
    if (x >> i) & 1  != (x >> j) & 1:
        bit_mask = (1 << i ) | (1 << j)
        x ^= bit_mask
    return x 
print(bin(73))
print(f"swapping {bin(73)[5]} @ index 3 and {bin(73)[7]} @ index 5")
x = swap_bits(73, 3, 5)
print(bin(x))




