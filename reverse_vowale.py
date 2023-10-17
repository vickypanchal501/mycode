# vowale = ["a","e","i","o","u","A","E","I","O","U"]
# input1 =  "gedfajfaihahgodwiifdfsobdofsdojd"
# inputlist = [i for i in input1]
# vowalestr = ''
# print(inputlist)
# for i in inputlist:
#     if i in vowale:
#         vowalestr += i
# revstr = vowalestr[::-1]
# g= 0
# print(revstr)
# newstr = ''
# for i in inputlist:
#     if i in vowale:
#         newstr += revstr[g]
#         g+=1
#     else:
#         newstr+=i    
# print(newstr)        



# perfect sum -----------------------------------------

arr = [2, 3, 5, 6, 8, 10]
sum = 10
arr = list(filter(lambda x : x <= sum, arr))
MOD = 1000000007
n = len(arr)
dp = [[0 for _ in range(sum + 2)] for __ in range(n + 1)]
dp[0][0] = 1
print(dp)
for i in range(n):
    for j in range(sum + 1):
        if j >= arr[i]:
            dp[i + 1][j] = (dp[i][j] + dp[i][j - arr[i]]) % MOD
        else:
            dp[i + 1][j] = dp[i][j]
print(dp[n][sum])
