A = [15, 10 ,19 ,10, 5 ,18 ,7]
N = 7
M =5
i=1
li =[]
while M:
    li.append(max(sum(A[:i]),sum(A[i:])))
    i+=1
    N-=1
print(min(li))   