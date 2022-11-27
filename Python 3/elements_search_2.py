l = input()


def find(ordered_list, element_to_find):

    for elements in ordered_list:

        if elements == element_to_find:

            return True

        return False

    
if __name__=="__main__":

    l = [2,4,6,3,7]

    print(find(l, 8))