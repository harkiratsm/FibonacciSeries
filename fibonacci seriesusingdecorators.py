from functools import lru_cache  #this is decorators and this will increase speed
@lru_cache(maxsize=1000)
def fib(n):
    if n==0:              #memorize
        return 0
    elif n==1:          #memorize
        return 1
    else:
        return fib(n-1)+fib(n-2)     #recursion
n=int(input()) 
for i in range(n):
    print(fib(i),end=" ")
    
    
   



