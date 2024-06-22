import os, sys
# 假定 foo.txt 文件存在，并有读写权限
ret = os.access('foo.txt', os.F_OK)
print("F_OK - 返回值 %s"% ret)

ret = os.access('foo.txt', os.R_OK)
print("R_OK - 返回值 %s"% ret)

ret = os.access('foo.txt', os.W_OK)
print("W_OK - 返回值 %s"% ret)

ret = os.access('foo.txt', os.X_OK)
print("X_OK - 返回值 %s"% ret)


path = "/tmp"
# 查看当前工作目录
retval = os.getcwd()
print ("当前工作目录为 %s" % retval)

# 修改当前工作目录
os.chdir( path )

# 查看修改后的工作目录
retval = os.getcwd()

print ("目录修改成功 %s" % retval)
