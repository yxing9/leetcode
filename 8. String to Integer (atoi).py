# 8. String to Integer (atoi)
# Medium
# String



'''

This question has so many edge cases to pass

""
"42"
"   -42"
"4193 with words"
"abc 123 with words"
"-91283472332"
"3.14159"
"-+12"
"+-12"
"21474836460"
"00000-42a1234"


N.B.:
if s.startswith("-"):
    xxx
if s.startswith("+"): # bug
    xxx

using if instead of elif is a huge bug, 
as it is no longer a choice 1 out of 2 

it will return wrong answer for -+12, 
because in the buggy code, 
- is first eliminated, 
then + is eliminated again, 
but we only need to do this once. 

'''



# Larry's 
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = 1
        
        if s.startswith("-"):
            sign = -1
            s = s[1:]
        elif s.startswith("+"):
            s = s[1:]

        current = 0
        for i in s:
            if not i.isdigit():
                break
            current = current * 10 + int(i)
            
        current *= sign
        
        current = min(current, 2 ** 31 - 1)
        current = max(current, -(2 ** 31))
        
        return current
# time O(N) N is s.length
# space O(N)

#----------


# my passed solution after 9 failure
class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        processed_s = s.lstrip()
        if len(processed_s) == 0:
            return 0
        
        if not processed_s[0].isdigit() and processed_s[0] != "-" and processed_s[0] != "+":
            return 0
        
        sign = 1
        if processed_s[0] == "-":
            sign = -1
            processed_s = processed_s[1:]
        elif processed_s[0] == "+":
            processed_s = processed_s[1:]
        
        if len(processed_s) == 0:
            return 0
        
        if processed_s[0] == "+" or processed_s[0] == "-":
            return 0
        
        temp = []
        for i in processed_s:
            if not i.isdigit() or i == 0:
                break
            else:
                temp.append(i)
        
        ans = ''.join(temp)
        if len(ans) == 0:
            return 0
        
        final_ans = int(ans) * sign
        
        if final_ans < (-2) ** 31:
            return (-2) ** 31
        elif final_ans > (2) ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return final_ans

# ---

# my initial solution with changes learned from Larry, still failed at "-+12"
class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        processed_s = s.lstrip()
        if not processed_s[0].isdigit() and processed_s[0] != "-" and processed_s[0] != "+":
            return 0
        
        sign = 1
        if processed_s[0] == "-":
            sign = -1
            processed_s = processed_s[1:]
        elif processed_s[0] == "+":
            processed_s = processed_s[1:]
            
        if processed_s[0] == "+" or processed_s[0] == "-":
            return 0
        
        temp = []
        for i in processed_s:
            if i.isdigit():
                temp.append(i)
            elif i == ".":
                break
        
        ans = ''.join(temp)
        final_ans = int(ans) * sign
        
        if final_ans < (-2) ** 31:
            return (-2) ** 31
        elif final_ans > (2) ** 31:
            return (-2) ** 31
        else:
            return final_ans
# learn variable naming from Larry



# --- End --- #