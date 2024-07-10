# def is_leap(year):
#     if year % 4==0:
#      if year % 100==0:
#         if year %400==0:
#            print("Leap year")
#         else:
#            print("Not leap Year")
#      else:
#        print("Leap Year")
#     else:
#        print("Not Leap Year")

# print(is_leap(1900))


def my_function(a):
    if a < 40:
        return "Terrible"
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))