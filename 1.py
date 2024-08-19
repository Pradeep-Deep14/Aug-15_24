#Reverse a list in Python
#Solution 1
my_list=[1,2,3,4,5]
my_list.reverse()
print(my_list)

#Solution 2

my_list=[1,2,3,4,5]
reversed_list=my_list[::-1]
print(reversed_list)

#Solution3
#using Reversed function

my_list=[1,2,3,4,5]
reversed_list=list(reversed(my_list))
print(reversed_list)

#Solution4
my_l=[1,2,3,4,5]
r_list=[]
for i in my_l:
    r_list.insert(0,i)
print(r_list)

#Solution 5
my_list=[1,2,3,4,5]
reversed_list=[]
for i in range(len(my_list)-1,-1,-1):
        reversed_list.append(my_list[i])
print(reversed_list)
