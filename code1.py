def fib(n):
    result=0
    for i in range(n+1):
        result+=i
    return result

res=fib(5)
print(res)

def printhello(name):
    print(f"Hello{name})
printhello("pooji")
