Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class TwoSum(object):

    def __init__(self):
        # initialize your data structure here
        self.count = {}
        
    # Add the number to an internal data structure.
    # @param number {int}
    # @return nothing
    def add(self, number):
        self.count[number] = self.count.get(number, 0) + 1


    # Find if there exists any pair of numbers which sum is equal to the value.
    # @param value {int}
    # @return true if can be found or false
    def find(self, value):
        for num in self.count:
            if value - num in self.count and (value - num != num or self.count[num] > 1):
                return True
        return False