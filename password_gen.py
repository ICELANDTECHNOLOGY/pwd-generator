__name__ = "__main__"

import random

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = lowercase_letters.upper()
digits = "1234567890"
symbols = "!@#$%^*({]+_-"

lower, upper, nums, syms = True, True, True, True

all = ""

if lower:
    all += lowercase_letters
if upper:
    all += uppercase_letters
if nums:
    all += digits
if syms:
    all += symbols


length = 12
amount = 15

for n in range(15):
    password = "".join(random.sample(all, length))
print(password)

