# Q10.Shift Array element by 1.

# 	i/p `[10 20 30 40 50 60]`
# 	o/p [60 10 20 30 40 50]
a=[10,20,30,40,50,60]
b=[]

for i in range(-1,len(a)-1):
    b.append(a[i])

print(b)
