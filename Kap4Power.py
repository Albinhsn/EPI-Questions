def power(x,y):
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0/x
    while power:
        if power & 1:
            print(f"multiplying result {result} and x {x}")
            result = multiply_brute(result, x)
        print(f"x = {x}")
        x, power = multiply_brute(x,x), power >> 1
    return result


def multiply_brute(x, y):
    x,y = int(x), int(y)
    def add(a, b):
        running_sum, carryin, k, temp_a, temp_b = 0, 0, 1, a, b
        while temp_a or temp_b:
            ak, bk = a & k, b & k
            carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
            running_sum |= ak ^ bk ^ carryin
            carryin, k, temp_a, temp_b = (
                carryout << 1, k << 1, temp_a >> 1, temp_b >> 1)
        return running_sum | carryin
    running_sum = 0
    while x:
        if x & 1:
            running_sum = add(running_sum, y)
        x, y = x >> 1, y << 1
    return running_sum

print(power(2,5))

#Brute force = do x*x*x*X*x etc
