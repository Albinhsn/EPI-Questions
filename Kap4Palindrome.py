import math
def palindrome(x):
    if x <= 0:
        return x == 0
    num_digits = math.floor(math.log10(x)) +1   
    msd_mask = 10**(num_digits -1)
    for i in range(num_digits // 2):
        print(f"x // msd_mask = {x // msd_mask} and x % 10 = {x % 10}")
        if x // msd_mask != x % 10:
            return False
        x %= msd_mask
        x //= 10
        msd_mask //= 100
        
    return True

print(palindrome(12331))
