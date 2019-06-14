import time


# 判断是不是质数
def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
            else:
                return True


def display_time(func):
    def wrapper(*args):  # 此处本质调用传入的func
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        print('total time {:.4}s'.format(end_time - start_time))
        return result  # 如果被修饰的函数有返回值，需要再wrapper（） 里面 设置返回值
    return wrapper  # 此处本质是把func 整体返回


@display_time
def prime_nums(maxnum):
    count = 0
    for i in range(2, maxnum):
        if is_prime(i):
            count = count + 1
    return count


if __name__ == '__main__':
    count = prime_nums(10000)
    print(count)
