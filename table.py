
# name = ["First_Name"]
# surname = ["Last_Name"]
# age =["age"]
# s_no = ['S.No.']

# num = 0
# i = " "
# while True:
#     name.append(input("Enter Your First Name :-"))
#     surname.append(input("Enter Your Last Name :-"))
#     age.append(int(input("Enter Your Age :-")))
#     chack = input("Add More Date Type Yes Either no :-")

#     # if chack == "yes" :
#     if chack == "yes" or chack=='YES':
#         num+=1
#         s_no.append(num)
#         i = True
#         #continue
        
#     elif chack == "no":
#         num+=1
#         s_no.append(num)
#         i = True
#         break
        
#     else:
#         print("Your Command is Wrong")
#         i = False
#         break
# namel = max([len(i)for i in name])
# surnamel = max([len(k) for k in surname])
# agel = max([len(str(k)) for k in age])       
# s_nol = max([len(str(k)) for k in age])  

# if i == True:
# #     print('''|------|--------------|----------------|--------|
# # | S.No | First_Name   | Last_Name      | age    |
# # |------|--------------|----------------|--------|''')
#         for j in range(len(name)):
#             print('''|{4}|{5}|{6}|{7}|
#     |{0}|{1}|{2}|{3}|'''.format(str(s_no[j]).center(s_nol +2) ,str(name[j]).center(namel+2),str(surname[j]).center(surnamel+2),str(age[j]).center(agel+2),'-'*int(s_nol+2),'-'* int(namel+2),'-'*int(surnamel+2,),'-'*int(agel+2)))
#         # print({}{}.format)
    

aa = '''#----------------------------------------#
Question 1
Level 1

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(begin,end) method

Solution:
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print ','.join(l)
#----------------------------------------#'''

bb = aa.split('#----------------------------------------#')

print(bb[2].split('Solutions'))