import random
def uniform_random(lower_bound, upper_bound):
    number_of_outcomes = upper_bound - lower_bound +1
    while True:
        result, i = 0, 0
        print("OH BOY HERE WE GO AGAIN")
        print("-----------")
        while (1 << i) < number_of_outcomes:
            r = random.randrange(0,2)
            result = (result << 1) | r
            print(f"r = {r}")
            print(f"result = {result}")
            i += 1
        if result < number_of_outcomes:
            break
    return result + lower_bound

print(uniform_random(1,6))
