#I'st Approch simple and direct 
def longest_palindrome_subseq(s):
    l = len(s)
    r = s[-1::-1]
    for i in range(l+1):
        a = [0]*(l+1)
        dp.append(a)
    count = 0
    for i in range(1,l+1):
        for j in range(1,l+1):
            if s[i-1] == r[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
                count+=1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(count)
    return dp[l][l]
"""

#II'nd approch Tricky but less time consuming
def longest_palindrome_subseq(s):
    l = len(s)
    for i in range(l):
        a = [0]*(l)
        dp.append(a)
        dp[i][i] = 1
    count = 0
    for gap in range(1,l):
        start = 0
        while start < l-gap:
            if s[start] == s[start+gap]:
                dp[start][start+gap] = 2+dp[start+1][start+gap-1]
                count+=1
                print('++++')
            else:
                
                dp[start][start+gap] = max(dp[start][start+gap-1], dp[start+1][start+gap])
            start+=1
    print(count)
    return dp[0][l-1]


"""

    
    
s = input()
dp = []
print(longest_palindrome_subseq(s))


