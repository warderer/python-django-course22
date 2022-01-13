# unpack o desempaquetado

numbers = (1, 2, 3, 4, 5, 6)

# one = numbers[0]
# two = numbers[1]
# three = numbers[2]
# four = numbers[3]

# one, two, three, four, *extras = numbers
one, two, *_, five, six = numbers

# print(one, two, three, four, extras)
print(one, two, five, six)