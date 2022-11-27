#uses for loop

def List(x):

    y = []

    for i in x:

        if i not in y:

            y.append(i)

        return y
        print (List(a))
#uses sets

def List2(x):

    return list(set(x))


a = [1,2,3,4,3,2,1]
print (a)

    print (List2(a))
