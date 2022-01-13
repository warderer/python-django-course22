
# lista = [1, 2]

# print(help(lista))


# >> index(value, start, end)

#            0      1       2         3        4
animals = ['cat', 'dog', 'horse', 'bird', 'rabbit', 'dog']

# index = animals.index('horse')
# print(index)

# >> count(value)

# count = animals.count('dog')
# print(count)

# >> sort(key=None, reverse=False) default ordena de forma ascendente

prime_numbers = [11, 3, 7, 5, 2]
# prime_numbers.sort()
# print(prime_numbers)

# >> sorted(<iterable>, key=None, reverse=False)
# reverse_list = sorted(prime_numbers, reverse=True)
# print(prime_numbers)
# print(reverse_list)

# >> reverse()
# prime_numbers.reverse()
# print(prime_numbers)


# revese_list = prime_numbers[::-1]
# print(revese_list)

# >> copy()

my_list = [2, 3, 5]
# my_list_2 = my_list
# new_list = my_list.copy()

# new_list.append(7)

# print(my_list)
# print(new_list)



# min() y max()

numbers = [6, 80, 1, 25, 55, 132, 500, 3, 4]
#numbers.sort()

# print(min(numbers))
# print(max(numbers))

# in
print(500 in numbers)