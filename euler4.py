def ispalindrome(n):
    num = str(n)
    num_reversed = num[::-1]
    if num == num_reversed:
        return True
    else:
        return False 
    





maior = 0 
for i in range(100,1000):
    for j in range(100,1000):
        
        if maior < i * j:
            if ispalindrome(i*j):
                maior = i * j 
print("cheguei", maior)
