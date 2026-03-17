def generator_function(num):
    for i in range(num):
        yield i**2

g = generator_function(100)
next(g)
next(g)
print(next(g))

for item in generator_function(100):
    print(item)

# def  Fibonacci_generator():
#     for i in range(10000):
#         yield i+i
#
#
# F = Fibonacci_generator()
#
# for item in Fibonacci_generator():
#     print(item)
