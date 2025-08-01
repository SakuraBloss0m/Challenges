import random

# create lists
my_numbers = []
winning_numbers = []

# create loop range for random numbers 
for i in range(5):
    my_numbers.append(random.randint(1, 69))
    winning_numbers.append(random.randint(1, 69))

# add another number to each list
my_numbers.append(random.randint(1, 26))
winning_numbers.append(random.randint(1, 26))

# print numbers
print("My Numbers:", my_numbers)
print("Winning Numbers:", winning_numbers)