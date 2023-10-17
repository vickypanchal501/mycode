import re

filename = open("text.txt",'r')
l = filename.readlines()
g= l[2].split()
dict1= {}
dict1[g[0]] = g[1]
print(dict1)

# g = re.findall("\ASolution",l[12])
# print(l[12])
# print(g)
# if g:
#   print("Yes, there is a match!")
# else:
#   print("No match")


# Dict = [{'Dict1': {'name': 'Ali', 'age': 19},
#         'Dict2': {'name': 'Bob', 'age': 21}}]


# if Dict[-1]["Dict1"] not in ["vikas"]:
#         Dict[-1]["Dict1"]["vikas"] = "hell"

# if Dict[-1]["Dict1"] in ["name"] :       
#         Dict[-1]["Dict1"]['nam'] = "helo"  
# print(Dict)
# # read1 = open.read()

# # from collections import Counter
# line_count = 0
# line_number =[]

# for line in filename :
#     line_count += 1
#     if re.findall("\A#---",line):
#         line_number.append(line_count)
# print(line_number)

# filename.close()
# filename = open("text.txt",'r')

# def find_line_number(filename, line_number):
#     # with open(filename,'r') as file:
#     max_number= max(line_number)
#     i = 0
#     while max_number < i:
#         for i in range(line_number[i],line_number[i+1]):
#             if re.findall("\A#---",line):
#                 continue
#     #             print("first")
#             if re.findall("\ASolution:",line):   
            






















# 
#     li= []

#     count = 0
#     for line_num ,line in enumerate(filename) :
#         count += 1
#         while True:
#             if re.findall("\A#---",line):
#                 print("first")
                
#             if re.findall("\AQuestion ",line):
#                 li.append({"Question {}".format(count):[]})
                
#             break    
#     print(li)          

# find_line_number(filename,line_number)

#         count += 1
#         while True:
#             if re.findall("\AQuestion",line) :
#                 # dict1.append(dict("Question",count))
#                 print("Question")
#                 break

            # for i in Question_num:
            #     if i in line:
            #         line_number.append(line_count)
    # return line_number
# op1 = find_line_number(filename,Question_num)

# find_question = [line for line in open("text.txt") if "Q"]
# readfile = open("text.txt")
# print(str(filename[1:20]))
# dict = {}
# for i in p:
#     i.split()
#     i[0] = i[1]



# print(Question_num)


# print(find_line_number(filename,Question_num))
# print(Question_num[0].split())
# print(dict(Counter(Question_num)))
# print(p[0][9])





# dict1 = [{"vikas":{"1":2,"2":3}}]
# # l = dict1[-1].values()

# if dict1[-1]["vikas"].keys() not in ['w']:
#         dict1[-1]["vikas"]["w"] = "3"
# print(dict1)        
# if dict1[-1]["vikas"] in 'w':     
#         print("true")
# # print(dict1[-1]["vikas"]["sd"] = 3)
# print(dict1)







# dict1 =  []
# count = 0
# for line in filename :
#     if re.findall("\A#---",line)in line:
#         print("first")
#         count += 1
#         while True:
#             if re.findall("\AQuestion",line) :
#                 # dict1.append(dict("Question",count))
#                 print("Question")
#                 break

# print(dict1)            