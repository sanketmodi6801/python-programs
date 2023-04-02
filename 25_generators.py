# This file is about generators , iterables, iterator, iteration
# def gen(x):
#     for i in range(x):
#         yield i
#
#
# sam = gen(5)
# # for j in sam:
# #     print(j)
#
# print(sam.__next__())
# print(sam.__next__())
# print(sam.__next__())
# print(sam.__next__())
# print(sam.__next__())
# print(sam.__next__())

""" Advantages of using Generators:
Producing iterables is extremely difficult and lengthy without Generators in Python.
Generators automatically implement __iter__(), __next__() and StopIteration which otherwise, need to be explicitly
specified.The most significant advantage of generators is that the memory is saved as the items are produced when required.
Generators are also used to pipeline a series of operations, for example, Generate Fibonacci Series"""


# Factorial program


# def Fac(x):
#     fac = 1
#     for i in range(x):
#         fac = fac * (i + 1)
#         yield fac
#
#
# s = Fac(6)
# for i in s:
#     print(i)
# print(Fac(5))

# def fac(x):
#     f = 1
#     for i in range(x):
#         f = f * (i + 1)
#         yield f
#
#
# s = fac(5)
# for i in s:
#     print(i)
#
#
# # fibbonaci series
#
# def fib(x):
#     n = 1
#     i = 0
#     for _ in range(x):
#         yield n
#         i, n = n, (i+n)
#
#
# s = fib(7)
# for i in s:
#     print(i)
n = 2
print(n ** 3)
