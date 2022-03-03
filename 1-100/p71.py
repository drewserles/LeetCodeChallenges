'''
String parsing exercise.

Result should be of the form:
    The path starts with a single slash '/'.
    Any two directories are separated by a single slash '/'.
    The path does not end with a trailing '/'.
    The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')

I'm thinking I should build it up piece by piece? Parse out a chunk in the path and then add it to a

>Could do something nice with regex where we split on the slashes.
'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        def parse(snippet):
            if snippet == '..':
                if len(res) > 0:
                    res.pop()
            elif snippet != '.':
                res.append(snippet)
        res = []
        piece = ''

        for c in path:

            # If you find a '/' then need to do something about it
            if c == '/':
                # repeat slashes after the first
                if len(piece) == 0:
                    continue
                # otherwise this terminates something. 
                else:
                    parse(piece)
                    piece = ''
            else:
                piece += c

        if len(piece) > 0:
            parse(piece)

        return '/' + '/'.join(res)





if __name__ == "__main__":
    sol = Solution()
    path = "/a//b////c/d//././/..////a"
    print(sol.simplifyPath(path))