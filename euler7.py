def gerador():
    i = 2
    while True:
        yield i
        i = i + 1

def erastoteles_sieve(g):
    def isnot_multiplos(n):
        def ret(k):
            return k % n != 0
        return ret
    while True:
        next_prime = next(g)
        
        yield next_prime
        g = filter(isnot_multiplos(next_prime), g)
g = erastoteles_sieve(gerador())
cont = 1
for i in g:
    if cont == 10001:
        print(i)
        break
    cont +=1 

    
