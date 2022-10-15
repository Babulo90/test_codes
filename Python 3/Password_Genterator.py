#Version_1

import random

s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+|}{[];/?><,"

passlen = 8

Password = "".join(random.sample(s, passlen))

print(Password)

#Version_2

import random

import string

def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))

print(pw_gen(int(input("How many Chars in your password?"))))
