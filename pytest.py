# coding=utf-8

import time


def test():
    i = 0
    while i < 10:
        print 'i:', i
        time.sleep(1)
    print '--end--'


if __name__ == '__main__':
    test()
