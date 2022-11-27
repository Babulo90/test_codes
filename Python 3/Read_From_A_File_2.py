counter_dict = ()

with open('traning.txt') as f: #how_many_each_category_are_there_in_training.txt

    line = f.readline()

    while line:

        line = line[3:-26]

        if line in counter_dict:

            counter_dict[line] += 1

        else:
            counter_dict = 1

        line = f.readline()

print(counter_dict)
