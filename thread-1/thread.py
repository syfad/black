#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018
# @Author  : SunYunfeng
# @Disc    : ssh-copy-id
# @Disc    : support python 2.x and 3.x


import threading
import time

#演示创建线程
def test1():
    for i in range(5):
        print("---test1---%d" %i)
    #若果创建Thread时执行的函数，运行结束那么意味着子线程结束了

def test2():
    for i in range(5):
        print("---test2---%d" %i)

def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()
    t2.start()

    print(threading.enumerate()) #打印出线程

#if __name__ == "__main__":
#    main()


#=========================

#通过继承Thread类完成创建线程
class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'am" + self.name + "@" +str(i)  #name属性中保存的是当前线程的名字
            print(msg)

        self.login()  #如果类里有多个方法，要通过这种方式来调用方法，因为继承thread类只会执行run方法里的代码。。。#
        self.register()


    def login(self):
        print("这是登陆")
    def register(self):
        print("这是注册")

# if __name__ == '__main__':
#     t = MyThread()
#     t.start()
#=========================

#多线程之间共享全局变量
#多线程之间共享全局变量--args参数

#定义一个全局变量
#g_num = 100

def test3(temp):
    temp.append(33)
    print("---in test3 temp=%s" % str(temp))

def test4(temp):
    print("--in test4 temp=%s" % str(temp))

#args参数
g_nums = [11, 22]


def main():
    # target 执行将来 这个线程去哪个函数执行代码
    # args执定将来调用 函数的时候 传递什么数据过去
    t3 = threading.Thread(target=test3, args=(g_nums,))
    t4 = threading.Thread(target=test4, args=(g_nums,))

    t3.start()
    time.sleep(1)

    t4.start()
    time.sleep(1)

    print("--in main Thread g_nums = %s" % g_nums)

# if __name__ == "__main__":
#     main()

#======================

# 共享全局变量-资源竞争的问题
#实验代码体现，多线程是当g_nums数字变大时，线程1和线程2出现资源竞争问题。


#使用互斥锁解决源竞争的问题

g_num = 0
def test5(num):
    global g_num

    # 上锁，如果之前没有被上锁，那么此时上锁成功
    # 如果上锁之前 已经被上锁了，那么此时会堵塞在这里，直到锁解开为止
    mutex.acquire()
    for i in range(num):
        g_num += 1
    #解锁
    mutex.release()

    print("===in test5 g_num=%d===" % g_num)


def test6(num):
    global g_num

    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()

    print("== in test6 g_num=%d==" % g_num)


# 创建一个互斥锁，默认是没有上锁的
mutex = threading.Lock()

def main():
    t5 = threading.Thread(target=test5, args=(1000000,))
    t6 = threading.Thread(target=test6, args=(1000000,))

    t5.start()
    t6.start()

    time.sleep(2)
    print("in main Thread g_num = %d==" % g_num)

if __name__ == "__main__":
    main()

#============================================

#资源竞争会导致死锁
#如何避免死锁
    #程序设计避免（银行家算法）
    #添加超时时间







