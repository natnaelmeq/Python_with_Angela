print("Welcome to the rollercoaster!")
height =int(input("What is your height in cm?"))

if height >= 120:
    print("you can ride the rollercoaster!")
    age =int(input("How old are you?"))
    if age >18:
        print ("Cost you $10")
    else:
        print("cost you $5")
else:
    print("Sorry, you have to grow taller before you can ride")