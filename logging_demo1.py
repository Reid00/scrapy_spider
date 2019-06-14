import logging

# 设置log 的输出方式
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    # filename='myapp.log', #文件位置
    filemode='w'
)
logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logger.info('this is a info info')
    logger.debug('this is a degug info2')

## @property 的用法，把方法属性化
class Washer:
    def __init__(self, water=10, scour=2):
        self._water = water
        self.scour = scour

    @property  # 把方法转化成属性去调用 （属性包装，把类的内部属性在外部展现出来，通过方法）
    def water(self):        # 属性读取
        return self._water

    @water.setter       # 属性更改
    def water(self, water):
        if 0 < water < 500:
            self._water = water
        else:
            print('set failure!')

    # @water.deleter


if __name__ == '__main__':
    w = Washer()
    print(w.water)
    w.water=100
    print(w.water)


