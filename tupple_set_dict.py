"""Tupple, Set and Dictionary in Python"""
"""Tupple"""

# t = (1,2,3,4,5,6,7,8,9)
# print(t)
# print(t[0:5])
# print(t[0:5:2])
# print(t[0])
# print(type(t))

"""Set"""
# s= {1,2,3,4,5,6,7,8,9}
# print(s)
# print(type(s))

# s1= {9,2,3,7,4,5,6,7,8,9,1,2,4,6,8}
# print(s1)
# s1.add(10)
# print(s1)
# s1.remove(10)
# print(s1)

# s1.intersection({1,2,3,40,50})
# print(s1)
# s1.union({1,2,3,40,50})
# print(s1)


"""Dictionary"""
# d={10:100,20:200,30:300,40:400}
# print(d)
# d[10] = 1000 #updating
# print(d)
# d[50] = 5000 # creating
# print(d)
# del d[30] # deleting
# print(d)


# a = (1,2,3,4,5,5,5.5,print(),"hello")


# count = a.count(5)

# print(count)


# a = (1,)

# print(type(a))



# a = {1,8,9,"hello",2,3,4,5}

# for i in a:
#     print(i)

# a = {8,1,2,3,4}

# a.clear()

# print(a)


# a = {1,2,3,4,5}
# b = {4,5,6,7,8}

# b -= a

# print(b)

# d = {10:100,20:200,30:300,40:400}

# d[10] = 100 #updating
# d[50] = 500 # creating
# del d[30] # deleting 

# print(d)




# d = {10:100,20:200,30:300,40:400}

# print(d.items())

# d1 = {10:100,20:200,40:300}
# d2 = {40:400,50:500,60:600}


# for i in d2:
#     d1[i] = d2[i]

# print(d1)

# d1 = {10:100,20:200,40:300}
# sum = 0

# for i in d1:
#     sum = sum + d1[i]

# print(sum)


# a = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,7,8]

# d = {}
# for i in a:
#     if i in d.keys():
#         d[i] +=1 
#     else:
#         d[i] = 1

# print(d)


# d1 = {10:100,20:200,40:300}
# d2 = {40:400,50:500,60:600}

# for i in d2:
#     if i in d1.keys():
#         d1[i] += d2[i]
#     else:
#         d1[i] = d2[i]

