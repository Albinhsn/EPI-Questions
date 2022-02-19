def divide(x,y):
    result, power = 0, 32
    y_power = y << power
    print(f"y_power = {y_power}")
    while x>=y:
        print("----------")
        print(f"y_power > x")
        print(f"y_power = {y_power} - x = {x}")
        while y_power > x:
            y_power >>= 1
            power -= 1
            print(f"y_power = {y_power}, power = {power}")
        print(f"1 << power = {1 << power}")
        result += 1 << power
        x -= y_power
        print(f"result is {result}, x is {x}")
    return result

print(divide(27,4))


#27 4
# power = 32
# y_power = y << power
# shift right until x**y_power < y, y_power = 2
# x -= y_power = 11 (2**4)
# y_power >> 1 = 4 = result

# new y_power = 16
# new x = 11
# only one shift so  power = 1
# power << 1 = 2
# add 2 - result = 6
# now x = 3 = 11-8
# x < y so break
# result = 6
