

# number=7
# user_input=input("Do you want to play yes or no: ").lower()

# if user_input=="yes":
#     user_number=int(input("Guess our number:"))
#     if user_number== number:
#         print("you guessed correctly")
#     else:
#         print("try another number")
# else:
#     print("ok you will play later")

# my_list=[1,2,3,4,5]
# my_men=[8,9,8,555]


# for d in my_list:
#     print(f"{d} all are my nubers")


# grades=[25,66,55,48,55]
# total=sum(grades)
# print(total)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# evens = []
# for number in numbers:
#     if number%2==0:
#         evens.append(number)
# print(evens)

# user_input = input("Enter your choice: ").lower()
# if user_input != "q":
#     print("Add")
# else:
#     print("Quit")



#     user_input = input("Enter your choice: ")
# if user_input == "a":
#     print("Add")
# elif user_input=="q":
#     print("Quit")

###################################3
##this is comphension in python
# numbers=[1,2,35,56,8]
# doubling=[num for num in numbers  if num % 2== 0]
# print(id(numbers),doubling)

#or
# double=[]
# for nu in numbers:
#     double.append(nu*2)
# print(double)



#############
#Dictionaty

# total=sum(friends.values())
# print(total)

# for x , y in friends.items():
# tot=0
# for x  in friends.values():
#     tot+=x
# print(tot)
# my_dictionary = {'a': 1, 'b': 2, 'c': 3}
# items = list(my_dictionary.items())
# print(items)


# friends = [("Rolfe",30) , ("yu",355)]

# for name, _ in friends:
#     print(f"name:{name}, age :{_}")
# def my_function():
#     print('Bob')
 
# result = my_function()


# def double(x):
#     return x*2
# number=[1,2,3,4,9]
# # doubled= [x*2 for x in number]
# # doubled= [double(x) for x in number]
# doubled= list(map(double,number))
# # doubled_list=list(doubled)
# print(doubled)


# def multiple(*args):
#     print(args)
#     total=2
#     for arg in args:
#         total=total*arg
#     return total

# print(multiple(1,2,3))

# def add(x,y):
#     return x+y
# nums={"x":3,"y":5}
# print(add(**nums))

# def both (*args,**kwargs):
#         print(args)
#         print(kwargs)

# both(1,3,5,name="bob", age=25)

#*args for the single arguments
#** kwargs for the key value arguments




# student={"name": ("natnael","daniel"),"grads":(98,95,97)}

# def average(grad):
#     return sum(grad)/len(grad)
# def namees (name):
#     return name
# # print(average(student["grads"]))
# print(student.average())
# # print(average(student["grads"]))

##**Object Oranted programing

# class Student:
#     def __init__(self,name,grads):
#         self.name=name
#         self.grades=grades
#     def average(self):
#         return sum(self.grades)/len(self.grades)
    

# students = []
# names = ["Natnael", "Peter", "Daniel"]
# grades = [(98, 97, 99, 100), (95, 96, 98, 99), (90, 92, 95, 97)]
# one_student= Student()
# print(one_student.average())
        

# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
    
#     def average(self):
#         return sum(self.grades) / len(self.grades)

# # Create a list of students
# # students = Student()
# names = ["Natnael", "Peter", "Daniel"]
# grades = [(98, 97, 99, 100), (95, 96, 98, 99), (90, 92, 95, 97)]
# print(students.name)
# Populate the list of students
# for name, grade in zip(names, grades):
#     students.append(Student(name, grade))

# # Print the average grade for each student
# for student in students:
#     print(f"{student.name}'s average grade is: {student.average()}")

# together=zip(names,grades)
# for x in together:
#     print(x)


     

# class Student:
#     def __init__(self,name,grades):
#         self.name = name
#         self.grades = grades
    
#     def average(self):
#         return sum(self.grades) / len(self.grades)

# # Create a list of students
# # # students = Student()
# # my_name="nati"
# # my_grade=(98, 97, 99, 100)
# # one_student=Student(my_grade,my_grade)
# # print(one_student.name)
# # print(one_student.grades)
# # print(one_student.average())




# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"{self.name},{self.age} years old"

# # Create a list of students
# # students = Student()

# one_student=Student("nati",28)
# print(one_student)



# class Store:
#     def __init__(self,name):
#         self.name=name
#         self.items=[]
       
#     def add_item(self, name, price):
    
#         item ={"name": name, "price":price}
#         self.items.append(item)
    

#     def stock_price(self):
#         # Add together all item prices in self.items and return the total.
#         # return  sum([item['price'] for item in self.items])
#         total=0
#         for item in self.items:
#             total=total+item["price"]
#         return total
        
    


# my_store=Store()

# Store.add_item(my_store)
# print(my_store.add_item())



# class Book:
#     TYPES=("harrrrrd","paper")

#     def __init__(self,name,book_type,weight):
#         self.name= name
#         self.book_type= book_type
#         self.weight=weight
#     def __str__(self) :
#         return f"name of the book is {self.name}: and type {self.book_type} and aslo wight of {self.weight}"
#     @classmethod
#     def hard(cls,name,page_weight):
#         return cls(name,cls.TYPES[0],page_weight)
#     @classmethod
#     def paper(cls,name,page_weight):
#         return cls(name,cls.TYPES[1],page_weight+150)

# books=Book.paper("Code",25)
# print(books)




# class Store:
#     def __init__(self,name):
#         self.name=name
#         self.items=[]
       
#     def add_item(self, name, price):
    
#         item ={"name": name, "price":price}
#         self.items.append(item)
    

#     def stock_price(self):
#         # Add together all item prices in self.items and return the total.
#         return  sum([item['price'] for item in self.items])
#         # total=0
#         # for item in self.items:
#         #     total=total+item["price"]
#         # return total
#     @classmethod
#     def franchise(cls,store):
#         new_store=cls(store.name + " - franchise")
#         return new_store
#     @staticmethod
#     def store_details(store):
#         return '{},total stock price:{}'.format(store.name, int(store.stock_price()))
    
# my_store = Store("Amazon")
# my_store.add_item("Chair", 50)
# my_store.add_item("Table", 150)

# print(Store.store_details(my_store))
# from toimport import divide
# print(divide(10,5))
# print(__name__)
# import sys
# print (sys.modules)
# def divide(divided,divisor):
#     if divisor==0 or (isinstance(divisor, (list, tuple, set)) and len(divisor) == 0):
#         print("Divisor cannot be 0")
#         return
#     return divided/divisor

# grades={78,98,95,96}
# average=divide(sum(grades),len(grades))
# if average is not None:
#     print(f"the average of the grade will be {average}")


# class Book:
#     def __init__(self, name:str, page:int):
#         self.name=name
#         self.page=page
#     def __str__(self):
#         return f"Book name='{self.name}', page={self.page}"
        


# bookStore=Book("big TRhink",250)

# print(bookStore)


from flask import Flask
app =Flask(__name__)
stores=[
    {"name":"my Store","Items":[{"name":"Chair","Price": 15.99}]}
]
@app.get("/store")
def get_Stores():
    return {"stores": stores}

print(stores)