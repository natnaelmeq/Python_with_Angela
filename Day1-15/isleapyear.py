year=int(input("just put the year"))
if year % 4==0:
    if year % 100==0:
        if year %400==0:
            print("wow it leap year")
        else:
            print("sorry Not leap year")
    else:
        print("leap year")
else:
    print("not leap year   ")