Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class RandomizedSet:

    def __init__(self):
        self.nums_list = []
        self.nums_map = dict()
        

    def insert(self, val: int) -> bool:
        if val in self.nums_map:
            return False
            
        self.nums_map[val] = len(self.nums_list)
        self.nums_list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.nums_map:
            return False
        
        index = self.nums_map[val]
        last = len(self.nums_list)-1
        
        self.nums_map[self.nums_list[last]] = index
        self.nums_list[index], self.nums_list[last] = self.nums_list[last], self.nums_list[index]
        
        self.nums_list.pop()
        del self.nums_map[val]
        return True
        

    def getRandom(self) -> int:
        import random
        return random.choice(self.nums_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


#思路：insert:可以直接在数组后面添加一个新元素，并在哈希表中记录下该元素对应的数组下标。
#remove:先将待删除的元素与数组中最后一个元素调换，由于两个元素的顺序调换了，它们在哈希表中记录的下标也应该调换。
#调换完成后，待删除元素变成了数组中最后一个元素，故直接将数组长度减一并将该元素从哈希表中移除即可。