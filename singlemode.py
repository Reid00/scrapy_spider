import os
import time
from multiprocessing import Process


#
# def pro_func(name, age, **kwargs):
#     for i in range(5):
#         print('子进程正在运行中， name {}, age {} pid {]'.format(name, age, os.getpid()))
#         print(kwargs)
#         time.sleep(0.2)
#
#
# if __name__ == '__main__':
#     # 创建process 对象
#     p = Process(target=pro_func, args=('小明', 18), kwargs={'m': 20})
#
#     p.start()
#     time.sleep(1)
#     p.terminate()
#     p.join()
#

# 单例模式

class Singleton():
    _instnace = None

    def __new__(cls, *args, **kwargs):
        if not cls._instnace:
            cls._instnace = super().__new__(cls, *args, **kwargs)
        return cls._instnace


a = Singleton()
b = Singleton()
print(id(a), id(b))

a.age = 19
print(b.age)
