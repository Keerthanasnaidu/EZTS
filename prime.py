num=int(input())
flag=True
for i in range(2,num//2):
    if num%i==0:
        flag=False
if flag:
    print("prime")
else:
    print("not prime")