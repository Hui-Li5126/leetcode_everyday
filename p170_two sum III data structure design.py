Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:

TwoSum() Initializes the TwoSum object, with an empty array initially.
void add(int number) Adds number to the data structure.
boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.




class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = {}
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.count[number] = self.count.get(number, 0) + 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.count:
            if value - num in self.count and (value - num != num or self.count[num] > 1):
                return True
        return False