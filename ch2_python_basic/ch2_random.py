import random

four_uniform_randoms = [random.random() for _ in range(4)]
print(four_uniform_randoms)

# using same random number
#random.seed(10)
print(random.random())

#random.seed(10)
print(random.random())

# shuffle
up_to_ten = list(range(10))
random.shuffle(up_to_ten)
print(up_to_ten)

# random choice
print(random.choice(["Lim", "Baek", "Hah", "Jeon", "Noh"]))

# random samples with no duplication
lottery_num = list(range(60))
winning_num = random.sample(lottery_num, 6)
print(winning_num)

# random samples with allowing duplication
four_with_replacement = [random.choice(range(10)) for _ in range(4)]
print(four_with_replacement)
