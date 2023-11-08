n=int(input("enter the number"))
m=int(input("enter the power"))
def power(n,m):
    if m==1:
        return n
    else:
        return n*power(n,m-1)

p=power(m,n)
print(p)
