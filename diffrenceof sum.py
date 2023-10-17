
def func(li):
    if len(li) < 2:
        return 0
    li.sort()
    new_list = []
       
    for i in range(0,len(li)-1):
        new_list.append(li[i+1]-li[i])
    return max(new_list)      
li = [3]  
print(func(li))  