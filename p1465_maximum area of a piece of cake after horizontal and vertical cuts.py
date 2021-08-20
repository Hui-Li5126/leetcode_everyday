Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        maxH = self.getMaxPieceLength(h, horizontalCuts)
        maxW = self.getMaxPieceLength(w, verticalCuts)
        return (maxH * maxW) % (10 ** 9 + 7)
		
    def getMaxPieceLength(self, cakeLength: int, cuts: List[int])-> int:
        maxPieceLength = prevCut = 0
        for cut in sorted(cuts):
            if cut - prevCut > maxPieceLength:
                maxPieceLength = cut - prevCut
            prevCut = cut
        if cakeLength - prevCut > maxPieceLength:
                maxPieceLength = cakeLength - prevCut
        return maxPieceLength