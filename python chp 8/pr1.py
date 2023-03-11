def max(a,b,c):
    m=0
    if(a>b and a>c):
        m=a
        return m 
    elif(b>a and b>c):
        m=b 

        return m
    else:
        m=c
        return c    

d=max(60,78,56)
print(d)            
        