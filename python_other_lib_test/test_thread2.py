import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)

# 创建线程
thread = threading.Thread(target=print_numbers)

# 启动线程
thread.start()

# 等待线程结束
thread.join()
