This lintcode is different from leetcode 146:
Description
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the 
least recently used item before inserting a new item. Finally, you need to return the data from each get.

Example
Example1
Input:
LRUCache(2)
set(2, 1)
set(1, 1)
get(2)
set(4, 1)
get(1)
get(2)
Output: [1,-1,1]
Explanation：
cache cap is 2，set(2,1)，set(1, 1)，get(2) and return 1，set(4,1) and delete (1,1)，because （1,1）is the least use，get(1) and return -1，get(2) 
and return 1.

Example2
Input：
LRUCache(1)
set(2, 1)
get(2)
set(3, 2)
get(2)
get(3)
Output：[1,-1,2]
Explanation：
cache cap is 1，set(2,1)，get(2) and return 1，set(3,2) and delete (2,1)，get(2) and return -1，get(3) and return 2.


class LinkedNode:
    
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.key_to_prev = {}
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.capacity = capacity
    
    def push_back(self, node):
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node
    
    def pop_front(self):
        # 删除头部
        head = self.dummy.next
        del self.key_to_prev[head.key]
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy
        
    # change "prev->node->next...->tail"
    # to "prev->next->...->tail->node"
    def kick(self, prev):	#将数据移动至尾部
        node = prev.next
        if node == self.tail:
            return
        
        # remove the current node from linked list
        prev.next = node.next
        # update the previous node in hash map
        self.key_to_prev[node.next.key] = prev
        node.next = None

        self.push_back(node)

    # @return an integer
    def get(self, key):
        if key not in self.key_to_prev:
            return -1
        
        prev = self.key_to_prev[key]
        current = prev.next
        
        self.kick(prev)
        return current.value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.key_to_prev:	   
            self.kick(self.key_to_prev[key])
            self.key_to_prev[key].next.value = value
            return
        
        self.push_back(LinkedNode(key, value))  #如果key不存在，则存入新节点
        if len(self.key_to_prev) > self.capacity:		#如果缓存超出上限
            self.pop_front()					#删除头部
