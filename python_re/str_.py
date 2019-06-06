# -*- coding:utf-8 -*-
# /usr/bin/python
'''
@Author:  Yan Errol  @Email:2681506@gmail.com   
@Date:  2019-06-01  01:43
@File：str_.py
@Describe：字符串操作
@Evn:
'''
from io import StringIO
import re

class str_base(object):
    def __init__(self,strs):
        self.strs = strs

    def reverse_str(self,):
        '''
        字符串倒序
        :param strs:
        :return:
        '''
        return self.strs[::-1]


def main():
    strs = 'I love Python'
    newres = str_base(strs)
    print(newres.reverse_str())
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔','*', sentence, flags=re.IGNORECASE)
    print(purified)

if __name__=="__main__":
    main()
