for a in range(1,1001):
    for b in range(1,a):
        for c in range(1,b):
            if b**2 + c**2 == a**2 and a + b + c == 1000:
                print(a*b*c)
                
   
            

