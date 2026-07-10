"""Loops in Python"""
"""1) for loop"""
# print("Even numbers from 1 to 100:")
# for i in range(1,101):
#   if(i%2==0):
#     print(i)

# print("Revers numbers from 100 to 1:")
# for i in range(100, 0, -1):
#     print(i)

# print("Sum of numbers from 1 to 10:")
# total = 0
# for i in range(1, 11):
#     total += i
# print(total)


#lets print a table of 5
# n = int(input("Which table you want ? "))

# for i in range(n,(n*10)+1,n):
#     print(i)

# a = "SHERYIANS TEACHES INDUSTRY THINGS"
# print(len(a))

# for i in range(len(a)):
#     print(a[i])


# a = "SHERYIANS IS COOL"

# for i in a:
#     print(i)


# for i in range(1,21):
#     if i == 56:
#         print("break statement is executed")
#         break
#     print(i)

# else:
#     print("Break statement is not executed")


# n = int(input("please tell your number"))

# for i in range(n):
#     print("hello world ")

# n = int(input("please tell your number "))

# for i in range(1,n+1):
#     print(i)

# n = int(input("please tell your number "))

# for i in range(n,0,-1):
#     print(i)


# n = int(input("which table you want : - "))

# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")


# n = int(input("please tell your number:- "))

# sum = 0 

# for i in range(1,n+1):
#     sum = sum + i


# print(f"your sum is {sum}")

# n = int(input("please tell your number:- "))

# fact = 1 

# for i in range(1,n+1):
#     fact = fact * i


# print(f"your factorial is {fact}")


# n = int(input("tell your number :- "))
# even = 0
# odd = 0
# for i in range(1,n+1):
#     if i%2 == 0:
#         even = even + i
#     else:
#         odd = odd + i

# print(f"your even and odd sum are {even} , {odd}")


# n =int(input("which number factors you want :- "))

# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)


# n = int(input("check your number is perfect or not :-"))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum = sum + i

# if sum == n:
#     print("your number is perfect")
# else:
#     print("not a perfect number")




# n = int(input("check your number is prime or not  :-"))

# count = 0

# for i in range(1,n+1):
#     if n%i == 0:
#         count = count + 1

# if count == 2:
#     print("your number is prime")
# else:
#     print("your number is not prime")


# a = "SHERYIANS"

# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]

# print(b)

# a = "NAMAN"

# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]


# if b == a:
#     print("your string is pallindrome")

# else:
#     print("its not a pallindrome")

# a = "sdfsogn12413@#$%^&U"

# char = 0
# dig = 0
# spchr = 0

# for i in a:
#     if i.isdigit():
#         dig +=1 
#     elif i.isalpha():
#         char+=1
#     else:
#         spchr +=1 

# print(f"your digits are {dig}\nyour alphabets are {char}\nyour special characters are {spchr}")

# print(dir(str))


"""2) while loop"""
# i=1
# while(i<=10):
#   print(i)
#   i+=1

# i= 1
# while (i<=10):
#   if(i==5):
#     i+=1
#     continue
#   if(i==8):
#     i+=2
#     pass
#   print(i)
#   i+=1

# a = int(input("tell your number"))

# rev = 0

# while a > 0:
#     rev = rev *10 + a % 10
#     a = a //10

# print(rev)


# a = int(input("tell your number"))

# copy = a
# rev = 0

# while a > 0:
#     rev = rev *10 + a % 10
#     a = a //10

# if copy == rev:
#     print("pallindromic number")
# else:
#     print("not a pallindromic number")



# import random

# num = random.randint(1,10)

# tries = 0

# while True:
#     guess = int(input("please guess your number between 1 and 10 :- "))
#     if num == guess:
#         tries +=1
#         print(f"you are right you guessed the number is {tries} tries")
#         break

#     elif num < guess:
#         print("go a little lower")
#         tries +=1
    
#     elif num > guess:
#         print("go a little higher")
#         tries +=1

#     else:
#         tries +=1 
#         print("sorry you are wrong")

# print(12)
