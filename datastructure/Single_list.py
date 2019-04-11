# coding=utf-8
# /usr/bin/python
'''
Author:Yan Errol
Email:2681506@gmail.com
Wechat:qq260187357
Date:2019-04-11--00:25
Describe: 单向链表是最简单的一种形式，它每个结点包含两个域，一个信息域，一个事链接域，链接指向表中的下一个一个节点，而最后一个节点的链接域指向一个空值。
'''


import time

class SingleNode(object):
    """单链表的结点"""
    def __init__(self,item):
        # _item存放数据元素
        self.item = item
        # _next 是指向下一个节点的标识
        self.next = None


'''
单链表的操作：
is_empty() 链表是否为空
length() 链表长度
travel() 遍历整个链表
add(item) 链表头部添加元素
append(item) 链表尾部添加元素
insert(pos, item) 指定位置添加元素
remove(item) 删除节点
search(item) 查找节点是否存在
'''

class Single_link_list(object):
    """ 单向链表 """
    def __init__(self):
        self._head = None

    def is_empty(self):
        """ 判断是否是空链表"""
        return self._head == None

    def length(self):
        """ 链表的长度"""
        # cur 初始指向头节点
        cur = self._head
        Node_number = 0
        while cur != None:
            Node_number +=1
            # 节点后移
            cur = cur.next
        return Node_number

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur != None:
            print(cur.item,cur = cur.next)
            
        print("")


if __name__ == "__main__":
    main()