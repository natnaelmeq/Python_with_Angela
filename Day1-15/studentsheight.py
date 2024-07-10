# student_height=input().split()
# for n in range(0, len(student_height)):
#     student_height[n]=int(student_height[n])

# total_height=0
# for height in student_height:
#     total_height +=height
# print(f"total height= {total_height}")

# no_stu=0
# for stud in student_height:
#     no_stu+=1
# print(no_stu)


# total=0
# for number in range(1,10):
#     total +=number
#     print(number)
# print(total)


# given_number=int(input())
# even_number=0
# for x in range(0,given_number+1):
#     if x % 2==0:
#         even_number+=x
# print(even_number)

given_number= range(1,16)
for x in given_number:
    if x%3==0 and x%5==0:
        x="FizzeBuzz"
    elif x%3==0:
        x="Fize"
    elif x%5==0:
        x="Buzz"
    
    print(x)
        

