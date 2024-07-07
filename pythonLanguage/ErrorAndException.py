'''
    以下例子中，让用户输入一个合法的整数，但是允许用户中断这个程序（使用 Control-C 或者操作系统提供的方法）。用户中断的信息会引发一个 KeyboardInterrupt 异常。
'''
while True:
    try:
        x = int(input("请输入一个整数: "))
        break
    except ValueError:
        print("无效的输入，请输入一个整数。")


'''
    最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出。
'''
import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


'''
    以下实例如果 x 大于 5 就触发异常:
'''
x = 10
if x > 5:
    raise Exception('x 不能大于 5。当 x = 10 时，抛出异常.')

'''
    以下实例中 finally 语句无论异常是否发生都会执行：
'''
try:
    runoob()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('这句话，无论异常是否发生都会执行。')


