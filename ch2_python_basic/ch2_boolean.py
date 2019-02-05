# and or
x = 1
safe_x = x or 0
print(safe_x)

# all and any
all([True, 1, {3}])     # True
all([True, 1, {}])      # False
any([True, 1, {}])      # True
print(all([]))                 # True, there is no element which is false
print(any([]))                 # False, there is no element which is true