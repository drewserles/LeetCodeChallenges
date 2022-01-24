'''
Using cartesian coordinates instead of matrix. North 1 from centre is [0,1]

I did a whole bunch of work here but there's a trick. The only time the robot doesn't make it back home is if
it's still facing north after the first sequence and isn't already home. Otherwise we get home in 2 (if facing south)
or 4 (facing left or right) iterations because the movement vector rotates.
'''

class Solution:
    def isRobotBounded_0(self, instructions: str) -> bool:
        # Start off at centre facing noth
        coords = [0,0]
        facing = [0,1]


        for i in instructions:
            if i == 'G':
                coords[0] += facing[0]
                coords[1] += facing[1]
            elif i == 'L':
                facing = [-facing[1], facing[0]]
            elif i == 'R':
                facing = [facing[1], -facing[0]]

    # Consider coords to be a position vector from [0,0] and facing to be a direction

        # If we're back at the start we're done
        if coords == [0,0]:
            return True

        # otherwise have moved off centre
        # If facing same direction then this won't end
        elif facing == [0,1]:
            return False

        # If it's facing the opposite direction then the position vector gets inverted for the next step and it will return home
        elif facing == [0,-1]:
            return True

        # If it's turned 90 degrees L then want to move 3 more times and see if it comes back
        elif facing == [-1, 0]:
            print('90L turn')
            vect = coords
            for _ in range(3):
                vect = [-vect[1], vect[0]]
                coords[0] += vect[0]
                coords[1] += vect[1]
                print(f'Vector: {vect}, position: {coords}')
            if coords == [0,0]:
                return True
            else:
                return False

        elif facing == [1, 0]:
            print('90R turn')
            vect = coords
            for _ in range(3):
                vect = [vect[1], -vect[0]]
                coords[0] += vect[0]
                coords[1] += vect[1]
                print(f'Vector: {vect}, position: {coords}')
            if coords == [0,0]:
                return True
            else:
                return False

    def isRobotBounded(self, instructions: str) -> bool:
        coords = [0,0]
        facing = [0,1]


        for i in instructions:
            if i == 'G':
                coords[0] += facing[0]
                coords[1] += facing[1]
            elif i == 'L':
                facing = [-facing[1], facing[0]]
            elif i == 'R':
                facing = [facing[1], -facing[0]]

    # Consider coords to be a position vector from [0,0] and facing to be a direction

        # If we're back at the start we're done
        if coords == [0,0] or facing != [0,1]:
            return True
        else:
            return False

if __name__ == "__main__":
    sol = Solution()
    instructions = "GG"
    print(sol.isRobotBounded_0(instructions))