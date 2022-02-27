# 224. Basic Calculator
# Hard


'''


New knowledge: 
Learn this one-liner:

*** sign = [-1, 1][ss=="+"] ***

-> 
sign = 1 if ss == "+" else -1
-> 
if ss == "+":
    sign = 1
else:
    sign = -1



# int(True) = 1, int(False) = 0. Hence,
if ss == "+":
    sign = 1
else:
    sign = -1


----------

Logic:
3 conditions
1. When it's "+" or "-", add operand to result
2. When it's "(", push to stack
3. When it's ")", settle


'''

# my initial code - failed
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        ans = 0
        
        for i in s:
            if stack and (i == "+" or i == "(" or i == ")" or i == "'"):
                ans += int(''.join(stack))
                stack = []
            elif stack and i == "-":
                ans += int(''.join(stack))
                stack = [i]
            elif i.isdigit():
                stack.append(i)
            elif not stack and i == "-":
                stack = [i] # or stack.append(i)
            elif stack[0] == "-" and i == "(":
                temp = []
                # falls into another new cycle
                
        
        if stack:
            ans += int(''.join(stack))
        
        return ans
# it can't solve this case "1-(-1)"


# ----------

# OldCodingFarmer's solution
class Solution:
    def calculate(self, s: str) -> int:
        '''
        https://leetcode.com/problems/basic-calculator/discuss/62424/Python-concise-solution-with-stack.
        '''
        res, temp, sign, stack = 0, 0, 1, []
        for i in s:
            if i.isdigit():
                temp = temp * 10 + int(i) # = not +=
            elif i == "+" or i == "-":
                res += temp * sign
                temp = 0
                sign = [-1, 1][i == "+"]
            elif i == "(":
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif i == ")":
                res += temp * sign
                res *= stack.pop() # sign
                res += stack.pop() # previous res
                temp = 0
        return res + temp * sign # account for cases that doesn't end with ), like ... + 123 but not ... + 123)
# Runtime: 76 ms, faster than 75.62%



# -----------

# lc solution
# Approach 2: Stack and No String Reversal
class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        operand = 0
        res = 0 # For the on-going result
        sign = 1 # 1 means positive, -1 means negative  

        for ch in s:
            if ch.isdigit():

                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)

            elif ch == '+':

                # Evaluate the expression to the left,
                # with result, sign, operand
                res += sign * operand

                # Save the recently encountered '+' sign
                sign = 1

                # Reset operand
                operand = 0

            elif ch == '-':

                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':

                # Push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(res)
                stack.append(sign)

                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                res = 0

            elif ch == ')':

                # Evaluate the expression to the left
                # with result, sign and operand
                res += sign * operand

                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                res *= stack.pop() # stack pop 1, sign

                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                # (operand on stack) + (sign on stack * (result from parenthesis))
                res += stack.pop() # stack pop 2, operand

                # Reset the operand
                operand = 0

        return res + sign * operand


# -----------


s = Solution()
print(s.calculate("1 + 1")) # 2
print(s.calculate(" 2-1 + 2 ")) # 3
print(s.calculate("(1+(4+5+2)-3)+(6+8)")) # 23
print(s.calculate("-1")) # -1
print(s.calculate("1+(-1)")) # 0
print(s.calculate("1-(-1)")) # 2