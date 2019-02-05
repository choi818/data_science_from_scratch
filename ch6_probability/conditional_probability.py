import random

def random_kid():
    return random.choice(["boy", "girl"])

both_grils = 0
older_girl = 0
either_girl = 0

random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older = random_kid()

    if older == "girl":
        older_girl += 1
    if older == "girl" and younger == "girl":
        both_grils += 1
    if older == "girl" or younger == "girl":
        either_girl += 1

print("P(both|older):", both_grils / older_girl)
print("P(both|either):", both_grils / either_girl)
