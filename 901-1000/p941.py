class Solution:
    def validMountainArray_v1(self, arr):
        if len(arr) < 3: return False
        climb, desc = False, False
        for i in range(1, len(arr)):
            # climbing
            if arr[i] > arr[i-1]:
                if desc: return False
                climb = True
            # falling
            elif arr[i] < arr[i-1]:
                if not climb: return False
                desc = True
            # flat
            else:
                return False
        return climb and desc

    def validMountainArray(self, arr):
        if len(arr) < 3: return False
        s = 0
        for i in range(1, len(arr)):
            d = arr[i] - arr[i-1]
            if d == 0: return False
            if s == 0:
                if d > 0:
                    s = 1
                else:
                    return False
            
            elif s == 1:
                if d < 0:
                    s = 2

            elif s == 2:
                if d > 0:
                    return False
        return s == 2



if __name__ == "__main__":
    sol = Solution()
    arr = [2,3,1]
    print(sol.validMountainArray(arr))