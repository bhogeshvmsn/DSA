class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        fm=defaultdict(int)

        for i in text:
            if i in 'balloon':
                fm[i]+=1
        return min(fm['b'],fm['a'],fm['l']//2,fm['o']//2,fm['n'])

        