'''
    如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。
'''
try:
    raise NameError('HiThere')   # 模拟一个异常。
except NameError:
    print('An exception flew by!')
    raise