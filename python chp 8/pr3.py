def hello(n):
    if(n==1):
        return 1
    return hello(n-1)+n
a=hello(9)
print(a)    