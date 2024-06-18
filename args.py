#keyword arguments
def sum(a,b):
    return a+b
print(sum(a=12,b=13))
#variable length arguments;
def sum_numbers(*args):
    return sum_numbers(*args)
ans=sum_numbers(1,2,3,4,5)
print(ans)