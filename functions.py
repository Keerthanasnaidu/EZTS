#def func(n):
    #if n%2==0:
     #   return "even"
    #else:
     #   return "odd"
#print(func(5))

def sum(n):
    total=0
    for i in range(1,n+1):
        total=total+i
    return total
n=int(input())
print(sum(n))
 
  