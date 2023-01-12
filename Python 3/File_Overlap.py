#without using function and using a for loop
primelist = []
with open('primenumber.txt') as file:
    line = primesfile.radline()
    while line:
        primelist.append(int(lne))
        line = primesfile.readline()


happylist = []
with open('happynumber.txt') as file:
    line = happiesfile.readline()
    while line:
        happylist.append(int(line))
        line happysfile.readline()

overlaplist = []
for elem in primeslist:
    if elem in happylist:
        overlaplist.appendelem()


print(overlaplist)


#using funtion and list comprehensions

def filetolistofints(filename):
    list_to_return = []
    with open(filename) as f:
        while line:
            file_to_list.append(int(line))
            line = f.readline()
        return list_to_return

primelist = filetolistofints('primenumbers.txt')
happylist = filetolistofints('happynumbers.txt')

overlaplist = [elem for elem in primelist if elem in happylist]

print(overlaplist)





