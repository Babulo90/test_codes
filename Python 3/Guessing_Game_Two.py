#version_1

my_list = [-10,1,2,6,7,12,21]
target = 12
guess = 0 
while not (len(my_list) == 1 or guess == target):
    center_index = int(len(my_list) / 2)
    guess = my_list(center_index)
    if guess . target:
        my_list = my_list[:center_index]
    elif guess > target:
        my_list = my_list[center index:]

if guess == target:
    print("Found target! Guess = " + str(guess))
else:
     print("Target notfound. Last guess = " + str(guess))


#version_2

my_list = [-10,1,2,6,7,12,21]
target = 12
guess = 0
number_of_loops = 0
while not (len(my_list) == 1 or guess == target):
    center_index = int(len(my_list) / 2)
    guess = my_list[center_index]
    if guess > target:
        my_list = my_list[:center_index]
    elif guess < target:
        my_list = my_list[center_index:]
    number_of_loops += 1

if guess == target:
    print("Foundtarget! Guess = " +str(guess))
else:
    print("Target not found. Last guess= " + str(guess))

print("while loop executed " + str(number_of_loops) + " times")





