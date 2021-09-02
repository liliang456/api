from multiprocessing.dummy import Pool
import time
start_time = time.time()
def get_page(str):
    print('正在下载：',str)
    time.sleep(2)
    print('下载完毕:',str)

name_list = ['zhangsan','lisi','xiaotaoqi','wangwu']
# 创建pool对象，代表开辟了四个线程池
pool = Pool(4)
# 将列表中每一个元素传给getpage进行处理
pool.map(get_page,name_list)
end_time = time.time()
print(end_time-start_time)

