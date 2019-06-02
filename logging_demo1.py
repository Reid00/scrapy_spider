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
