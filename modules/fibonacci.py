# def  Fibonacci_generator():
#     for i in range(10000):
#         yield i+next(i)
#
#
# F = Fibonacci_generator()
#
# for item in Fibonacci_generator():
#     print(item)

def fib(number):
    i = 0
    a = 0
    b = 1
    while i < number:
        yield a
        a, b = b, a+b
        i += 1

for item in fib(25):
    print(item)

list = list(fib(10))
print(list)

# def fib(number):
#     a = 0
#     b = 1
#     for i in range(number):
#         yield a
#         temp = a
#         a = b
#         b = temp + b

def fib2(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

for item in fib1(10000):
    print(item)

# print(fib2(10000))

