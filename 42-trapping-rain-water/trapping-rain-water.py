class Solution:
    def trap(self, height: list[int]) -> int:
        left=0
        right=len(height)-1
        lm,rm=height[left],height[right]
        water_total=0

        while (left<right):
            if lm<rm:
                left+=1
                lm=max(lm,height[left])
                water_total+=lm-height[left]
            else:
                rm=max(rm,height[right])
                water_total+=rm-height[right]
                right-=1
        return water_total