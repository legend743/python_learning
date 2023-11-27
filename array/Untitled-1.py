# # find  the unique element
# a=[10,2,3,11,10,2,3]
# unique_element=[]
# for element in a:
#     if element  not in unique_element:
#         unique_element.append(element)
# print(unique_element)

#find the element which comes only once in the l
# from collections import Counter
# l=[1,5,3,4,2]
# for i in range(len(l+1)):
#     if l[i]-l[i+1]==2:
#         print("satisfied")

# insertion sort
 
list=[10,22,3,8,1]
b=[]
for i in range(len(list)):
    
    b.append(min(list))
    value=min(list)
    list.remove(value)
print(b)