# import fibo

# fibo.foo()
# fibo.bar()
# print(fibo.__name__)
# print(dir(fibo))

# from fibo import foo

# foo()
# bar()

# def foo():
#     print('my foo')

# from fibo import *

# foo()
# bar()
# print(fibo)

# import fibo as fibo2
# fibo2.foo()
# fibo2.bar()

# def foo():
#     print('my foo')

# from fibo import foo as foo2
# foo2()
# foo()

# import fibo
# print(dir(fibo))

from fibo import *
# print(fibo.__dict__)

from fibo import bar
print(dir())