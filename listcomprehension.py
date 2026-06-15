# list comphrension


lst1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
new_lst1 = []

for i in lst1:
    new_lst1.append(i+1)

print(new_lst1)



lst2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
new_lst2 = [i+1 for i in lst2]
print(new_lst2)

# new_lst1 = []

# for i in range(20):
#     new_lst1.append(i+1)


# print(new_lst1)


new_lst3 = [i+1 for i in range(20)]
print(new_lst3)













# condition kasari lagaunay


# lst1 = []
# for i in range(20):
#     if (i%2 == 0 ):
#         lst1.append(i)
# print(lst1)



# with list comphrension condtion

# lst2 = [i for i in range(20) if i%2==0]
# print("newlist : ", lst2)















temperature = [25,32,28,35,30,31]
new_temp = ["hot" for i in temperature if i>30]
print(new_temp)



















marks = [40,75,55,90,65]
new_mark = ["high" for  i in marks if i>70]
print(new_mark)









ages = [12,18,25,45,15,30]
eligible_age = ["eligible" for  i in ages if i>18]
print(eligible_age)











prices_eur = [100,200,50,75]
price= [i*1.1 for i in prices_eur ]
print(price)



















temps = [20,28,30,15,22]
temps_labels = ["hot" if i>25 else "cool" for t in temps for i in temps]
print(temps_labels)













nums = [25,8,12,7,20]
num = [i*2 if (i%2== 0 and i>10) else i  for i in nums ]
print(num)






