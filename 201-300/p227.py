'''
I came up with a solution that involved storing the operations in an array then evaluating them later.

There's a stack solution that's fairly similar (involves adding up the stack at the end)
And a nice solution keeping track of previous numbers. I implemented this one
'''


class Solution:
    def calculate_v0(self, s):
        def calcMultDiv(s):
            vals, ops= [], []
            mem = ''
            for i in range(len(s)):
                if s[i] in  ('*', '/'):
                    vals.append(int(mem))
                    ops.append(s[i])
                    mem = ''
                else:
                    mem += s[i]
            vals.append(int(mem))
            
            tot = vals[0]
            v,o = 1,0
            while v < len(vals) and o < len(ops):
                if ops[o] == '*':
                    tot *= vals[v]
                elif ops[o] == '/':
                    tot //= vals[v]
                v += 1
                o += 1
            return tot
        
        vals, ops = [], []
        mem = ''
        for i in range(len(s)):
            if s[i] in  ('+', '-'):
                vals.append(calcMultDiv(mem))
                ops.append(s[i])
                mem = ''
            else:
                mem += s[i]
        vals.append(calcMultDiv(mem))
        
        tot = vals[0]
        v,o = 1,0
        while v < len(vals) and o < len(ops):
            if ops[o] == '+':
                tot += vals[v]
            elif ops[o] == '-':
                tot -= vals[v]
            v += 1
            o += 1
        return tot

    '''
        Second attempt: keep track of three numbers: a total (overall),  a subtotal (running block that is separated by +/-), and current number (memory)
    '''
    def calculate_v1(self, s):
        # Keep a "current value (int)", a current operation - the last op we saw and we're figuring out what to op it with, and a running memory.

        tot = 0
        subtot = None
        pmd = '' # previous mult or div
        ppm = None # previous plus minus
        mem = ''

        def gen_sub(subtot, mem, pmd):
            if subtot is None:
                return int(mem)
            else:
                if pmd == '*':
                    return subtot * int(mem)
                elif pmd == '/':
                    return subtot // int(mem)

        def gen_tot(ppm, tot, subtot):
            if ppm is None:
                return subtot
            else:
                if ppm == '+':
                    return tot + subtot
                elif ppm == '-':
                    return tot - subtot

        for c in s:
            if c in ('*', '/', '+', '-'):
                subtot = gen_sub(subtot, mem, pmd)

                # If it's a mult or div then can evaluate what we have so far
                if c in ('*', '/'):
                    pmd = c
                    mem = ''
                # If it's an addition or subtraction then it's a little bit more complicated
                # It means we can evaluate what's trailing by adding it on to the total
                elif c in ('+', '-'):
                    tot = gen_tot(ppm, tot, subtot)
                    ppm = c
                    mem = ''
                    subtot = None # zero out the subtotal

            else:
                mem += c
        subtot = gen_sub(subtot, mem, pmd)
        tot = gen_tot(ppm, tot, subtot)
        return tot

    '''
    Clean up attempt of the above.
    Main thing to get my head around: We back track the previous operation seen with current_op.
        When we see a +,- we update the total with the previous number and replce prev with current. We encode the sign (current op) in the sign of the prev num value
        When we see *,/ the active (prev) number should continue so we update with the value
    '''
    def calculate(self, s):
        total, prev_num, cur_num = 0,0,''
        current_op = '+'

        for i in range(len(s)):
            if s[i].isdigit():
                cur_num += s[i]
            # Evalaute char or the last character of the string
            if s[i] in ('+', '-', '*', '/') or i == (len(s)-1):
                if current_op == '+':
                    total += prev_num
                    prev_num = int(cur_num)
                elif current_op == '-':
                    total += prev_num
                    prev_num = -int(cur_num)
                elif current_op == '*':
                    prev_num *= int(cur_num)
                elif current_op == '/':
                    prev_num //= int(cur_num)
                
                cur_num = ''
                current_op = s[i]
        return total + prev_num


if __name__ == "__main__":
    sol = Solution()
    s = "0*1+7"
    print(sol.calculate(s))