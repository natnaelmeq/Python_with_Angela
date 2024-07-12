

                #List comprehension
# numbers = [1,1,2,3,5,8,13,21,34,55]
# squared_number = [num*num for num in numbers]
# print(squared_number)

# lis_of_strings =  input("please put the number here: ").split(',')
# filter_even = [int(even) for even in lis_of_strings if int(even) % 2 == 0]
#
#
# print(filter_even)

# with open("file1.txt") as file1:
#     list1 =  file1.readlines()
# with open("file2.txt") as file2:
#     list2 = file2.readlines()
#
# common_number = [int(num)  for num in list1 if num in list2]
# print(common_number)

        #Dictionary Comprehension
# import random
# names = ["nati","anem","kidus","yafet"]
# score = {na:random.randint(90,100) for na in names}
# 5}
# print(score)

        #Example 1
import random



                # sentence = input("Please put you sentence:")
# new_list_words = {words:len(words) for words in sentence.split()}
# print(new_list_words)
        #Example 2

# weather_c = eval(input("Put number in celices:"))
# weather_f = {day:temp *9/5 +32 for (day,temp) in weather_c.items()}
# print(weather_f)


import pandas
from pandas import Index

neto_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(neto_alphabet.to_dict())

phonetic_dict = {row.letter: row.code for (index,row) in neto_alphabet.iterrows()}
print(phonetic_dict)

new_name = input("Enter a Word: ").upper()
out_put = [phonetic_dict[letter] for letter in new_name]
print(out_put)