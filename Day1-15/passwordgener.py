import random
import string


alphabets = [char for char in string.ascii_lowercase]
numbers = [str(num) for num in range(10)]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', "'", '"', ',', '.', '/', '?', '<', '>']


# print(alphabets)
# print(numbers)
# print(symbols)

# generate= random.randint()
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_numbers= int(input("How many number would you like?\n"))
nr_symboles= int(input("How many symboles would you like?\n"))

passwrod= []
for char in range(1,nr_letters+1):
    passwrod +=random.choice(alphabets)
for char in range(1,nr_numbers+1):
    passwrod +=random.choice(numbers)
for char in range(1,nr_symboles+1):
    passwrod +=random.choice(symbols)
    
print(passwrod)
random.shuffle(passwrod)
print(passwrod)

generated=""
for y in passwrod:
    generated +=y
print(generated)    
