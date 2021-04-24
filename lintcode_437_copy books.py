Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        if not pages:
            return 0
            
        start, end = max(pages), sum(pages)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.get_least_people(pages, mid) <= k:
                end = mid
            else:
                start = mid
                
        if self.get_least_people(pages, start) <= k:
            return start
            
        return end
        
    def get_least_people(self, pages, time_limit):
        count = 0
        time_cost = 0 
        for page in pages:
            if time_cost + page > time_limit:
                count += 1
                time_cost = 0
            time_cost += page
            
        return count + 1
#TC: O(nlog(sum))