a=[3,1,-2,-5,2,-4]
l=[]
buffer=[]
for value in a:
    if value>0:
        if not buffer and not l:
            l.append(value)
            continue
        if l[-1]<0:
            l.append(value)
            continue
        else:
            buffer.append(value)
            print(buffer,"this is buffer value")
            continue
    if value<0:
        l.append(value)
        if buffer:
            l.append(buffer[0])

            buffer=[]
print(l)
