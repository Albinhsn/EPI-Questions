def multiply_brute(x,y):
    def add(a,b):
        running_sum, carryin, k, temp_a, temp_b = 0, 0, 1, a, b
        while temp_a or temp_b:
            ak, bk = a & k, b & k
            carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
            running_sum |= ak ^ bk ^ carryin
            carryin, k, temp_a, temp_b = (carryout << 1, k << 1, temp_a >> 1, temp_b  >> 1)
        return running_sum | carryin
    running_sum = 0
    while x:
        if x & 1:
            print(f"Adding {y} to {running_sum}")
            running_sum = add(running_sum, y)
            
        x, y = x >> 1, y << 1
        print(f"running_sum = {running_sum}, x = {x},y  = {y}")
    return running_sum
print(f"x = {bin(9)}")
print(f"y = {bin(6)}")
print(multiply_brute(9,6))
