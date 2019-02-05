x = [4, 1, 2, 3]
y = sorted(x)       # y = [1, 2, 3, 4]
x.sort()            # x = [1, 2, 3, 4]

z = sorted([-4, 1, -2, 3], key=abs, reverse=True)   # z = [-4, 3, -2, 1]

# example
# wc = sorted(word_count.items(), key=lambda x: x[1], reverse=True)