class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        Solution.combo = []
        self.helper(candidates, target, [])
        return Solution.combo
        
    def helper(self, candidates, target, output):
        if target == 0 and output not in Solution.combo:
            Solution.combo.append(output)
            return
        
        for i, val in enumerate(candidates):
            if val<=target:
                self.helper(candidates[i+1:], target-val, output+[val])
            else:
                return
            
