import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = []
        heapq.heappush(heap, 1)

        seen = set()
        seen.add(1)

        factors = [2, 3, 5]

        curr_ugly = 1
        
        for _ in range(n):
            # 每次弹出当前最小丑数
            curr_ugly = heapq.heappop(heap)
            # 生成新的丑数
            for f in factors:
                new_ugly = curr_ugly * f
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        return curr_ugly


import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglys = []
        uglys.append(1)

        p2, p3, p5 = 0, 0, 0

        for i in range(1, n):
            last_number = uglys[i - 1]
            while uglys[p2] * 2 <= last_number:
                p2 += 1
            while uglys[p3] * 3 <= last_number:
                p3 += 1
            while uglys[p5] * 5 <= last_number:
                p5 += 1

            uglys.append(min(uglys[p2] * 2, uglys[p3] * 3, uglys[p5] * 5))

        return uglys[n - 1]
    
      #time complexity: O(n), but thought process isn't easy, so don't recommend this method