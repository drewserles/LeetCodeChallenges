'''
Trick here is fairly interesting. Realise that the water volume is limited by the smallest edge.
Start at the outside (widest) and move in -> aiming to find a container that holds more because of large walls.
If we move the taller wall and find an even taller one that doesn't help us - the volume can't increase because of the lower opposite wall.
    Nothing to be gained by moving the higher wall - either unusable height is gained or width is lost.
So move the smaller wall in looking for a taller one. The hope is that a height increase is found that outweighs the loss in width.
'''

class Solution:
    def calcArea(self, l_idx, r_idx, l_height, r_height):
        return min(l_height, r_height)*(r_idx - l_idx)
    def maxArea(self, height):
        max_area = 0
        l,r = 0, len(height)-1
        
        while l < r:
            l_height, r_height = height[l], height[r]
            area = self.calcArea(l, r, l_height, r_height)
            if area > max_area:
                max_area = area
            if l_height <= r_height:
                l += 1
            else:
                r -= 1
        return max_area


if __name__ == "__main__":
    height = [1,1]
    sol = Solution()
    print(sol.maxArea(height))