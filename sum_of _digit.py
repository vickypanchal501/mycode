
    
# def myfunc(n):
#     li = [1,10,100,1000,10000,100000]
#     num = 0
#     while num != 20:
#         count = 0
#         for i in str(n):
#             count += pow(int(i),2)
#         if count in li:
#             return True
#         num+=1
#         n = count

#     return False



    
# def myfunc(n):
#     count = 0
#     for i in str(n):
#         count += pow(int(i),2)
#     if len(str(count)) == 1:
#         if count == 1 or count == 7:
#             return True
#         else:
#             return False
    
#     return myfunc(count)
# m = int(input())
# print(myfunc(m))


li = [1,2,3,4,5]
p = [li[-1]]
p.append(li[i] for i in range(1,len(li)-1))
print(li[1:-1])
print(p)