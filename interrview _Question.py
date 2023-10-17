# Q.1---------------------------
# number = int(input())
# newnum  = str(number)
# print(newnum[::-1])

# Q.2-------------------------
# number = int(input())
# count = 0
# for i in str(number):
#     count += pow(int(i),3)
# if count == number:
#     print("True ")   
# else:
#     print("False")    

# Q.3--------------------------------------

# num = int(input())

# if num > 1:
   
#     for i in range(2, int(num/2)+1):
       
#         if (num % i) == 0:
#             print("is not a prime number")
#             break
#     else:
#         print("is a prime number")
# else:
#     print("is not a prime number")

# Q .4 ----------------------------------------------------------------
# list1 = [(2,5),(1,2),(2,3),(4,4),(2,1)]
# output =[]
# for i in list1:
#     output.append(i[::-1])
# output.sort()
# li =[]
# for j in output:
#     li.append(j[::-1])
# print(li)

# Q .5 ------------------------------------------------------------
# first Approch-----------------------
# from collections import Counter
# string = input()
# print(dict(Counter(string)))


# second Approch -------------------------------

# dict1 = {}
# for i in string:
#     if i not in dict1:
#         dict1[i] = 1
#     else:
#         dict1[i] += 1
# print(dict1)        




# Q.6 -----------------------------------------------------
# list1= ["gfg",3,"is",8,"df",23]
# list2 = ["name","id"]
# i = 0
# li = []
# while i != len(list1):
#     dict1= {}
#     for j in range(len(list2)):
#         if i%len(list2) == 0 or j == 0:
#             dict1[list2[j]] = list1[i]
#             i+=1
#         else:
#             dict1[list2[j]] = list1[i]
#             i+=1
       
#     li.append(dict1)
        
# print(li)

# Q.7 ------------------
# from functools import reduce
# num =[8,2,3,-1,7]
# new1 = reduce((lambda x,y : x*y),num)
# print(new1)

# Q.8 -------------------------------

# li = list(input().split())  
# print(" ".join(li[::-1]))


# Q.9 ---------------------
# string ="abaaba"
# if string[:int(len(string)/2)] == string[int(len(string)/2):]:
#     print("True")
# else:
#     print("False")    


# Q.10---------------------------------------
# dict1 = {0 : "zero" ,1 : "One",2 : "two", 3 : "three" ,4 : "four", 5 :" five" ,6 : "six", 7 : "seven" ,8 : "eight", 9 : "nine"}	
# li = ''
# string= list(input().split())
# for key, val in dict1.items():
#     for i in string :
#         if i == val:
#             li += str(key)
# # print(string)        
# print(li)


# Q.11 -----------------------------

# string ="A Man Is Wolking Down the Road."
# aa = string.split(' ')[::-1]
# res = ' '.join(aa).lower().capitalize()
# print(res)
# print(string.upper())
# string = string.rstrip(string[-1])
# li = list(string.split())
# print(' '.join(li[::-1]))
# f =[]
# for i in li:
#     g= i[0].swapcase() + i[1:] 
#     f.append(g)

# print(' '.join(f[::-1])+'.')  





l = [1,2,3,4,5]


def fun(num):
    num =1
    return fun(num+1)

print(fun(1))