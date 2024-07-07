#!/usr/bin/python3

'''
    创建一个迭代器
'''
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        return x
    
myclass = MyNumbers()
myiter = iter(myclass)

print (next(myiter))
print (next(myiter))
print (next(myiter))
print (next(myiter))
print (next(myiter))


# 生成器
