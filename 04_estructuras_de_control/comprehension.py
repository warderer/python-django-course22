# >> List comprehension
# Crear una nueva lista a traves de una iteración

# word = 'comprehension'
# # list_letters = []


# # for letter in word:
# # 	list_letters.append(letter)



# #  List comprehension
# list_letters = [letter for letter in word]

# print(list_letters)


fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']

# for x in fruits:
# 	if 'a' in x:
# 		newlist.append(x)

newlist = [x for x in fruits if 'a' in x]

print(newlist)