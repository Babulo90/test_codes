#Reverse_Exact_Words

import tracemalloc


S = input("Enter A String\n")

a = S[ : :-1]

print(a)

#Reverse_Word_Order

a = input("Enter A String\n")

def reverse(x):
    y = x.split()
    result = []
    for word in y:
        result.insert(0,word)
    return " ".join(result)

print(reverse(a))

#Reverse_Word_Order_2

b = input("Enter A String\n")

def reverse(x):
    y = x.split()
    y.reverse()
    return " ".join(y)

print(reverse(b))