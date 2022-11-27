counter_dict = ()

with open('nameslist.txt') as f: #counts_the_different_names_in_lines_in_nameslist.txt

    line = f.readline()

    while line:

        line =line.strip()

        if line in counter_dict:

            counter_dict += 1

        else:
            counter_dict = 1

        line = f.readline()

print(counter_dict)