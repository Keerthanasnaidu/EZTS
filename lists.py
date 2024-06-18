#my_list=[1,2,3,4]
#print(my_list)
#my_list.append(5)
#print(my_list)
#my_list.extend([6,7,8])
#print(my_list)
#my_list.remove(5)
#print(my_list)

user_input=input("enter numbers seperated by space")
number=list(map(int,user_input.split()))
for i in number:
    print(i)
