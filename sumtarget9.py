# # l=[10,2,3,4,5,6]
# # for i in range(len(l)-1):
# #     print(l[i])
 
# #     for j in range (1,len(l)-1):
# #         print("this is my l wali string",l[j])
# #         if(l[i]+l[j]==9):
# #             print("we got the string")
# #         else:
# #             print("continue")
# nums = [2,7,11,15]
# for i in range(len(l)-1):
#     for j in range(1,len(l)-1):
#         if(l[i]+l[j]==9):
#             return 1
#         else:
#             return 0
def square(x):
    return x**2
def operates_on_number(func,num):
    result=func(num)
    return result
number=10
result=operates_on_number(square,number)
print(f"the square of:{number} is:{result} ")