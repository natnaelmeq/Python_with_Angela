fruits = eval(input())

def make_pie(index):
    try:
        fruit = fruits[index]

    except IndexError:
        print ("no nati it has key error")
    else:
        print(fruit + "pie")

make_pie(4)