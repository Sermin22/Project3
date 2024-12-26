import os
#import math


def clear_and_sum():
    PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "nums.txt")
    with open(PATH_TO_FILE, "r") as file:
        rows = (row.split("#")[0].rstrip() for row in file)
        nums = (n for n in rows if n)
        #nums = (n for n in nums if math.isfinite(n)), заменил строкой ниже
        nums = (float(n) for n in nums if n.isdigit())
        nums = (0 if n < 0 else n for n in nums)
        total_sum = sum(nums)
        return f"the sum is {total_sum}"


if __name__ == "__main__":
    print(clear_and_sum())
