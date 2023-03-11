from typing import Type


def func():
    print("hello my name is dhruvi")

func()

def greet(name="stranger"):
    return "hello "+name

a=greet()
print(a)
b=greet("dhruvi")    
print(b)
print(type(a))