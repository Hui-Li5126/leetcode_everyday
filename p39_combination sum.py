Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(list(set(candidates)))
        results = []
        self.dfs(candidates, target, 0, [], results)
        return results

    def dfs(self, candidates, target, start, combination, results):
        if target < 0:
            return
        if target == 0:
            return results.append(list(combination))

        for i in range(start, len(candidates)):
            combination.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, combination, results)
            combination.pop()