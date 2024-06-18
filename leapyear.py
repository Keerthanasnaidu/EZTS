count=0
for year in range(1850,2025):
    if((year%4==0 and year%100!=0) or (year%400==0)):
        count=count+1
print(count)