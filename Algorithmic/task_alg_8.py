# Check the parentheses. You have 3 types of parentheses () [] {},
# for example! ({{}} {] []}})! Check that each open
# parenthesis has a closing parenthesis.


def is_valid(prnthses: str):
    stack = []
    opening = set('([{')
    closing = set(')]}')
    pair = {')': '(', ']': '[', '}': '{'}
    for i in prnthses:
        if i in opening:
            stack.append(i)
        if i in closing:
            if not stack:
                return "is Not Valid"
            elif stack.pop() != pair[i]:
                return "is Not Valid"
            else:
                continue
    if not stack:
        return "is Valid"
    else:
        return "is Not Valid"


prnthses = '{[()]}'
print(f'The {prnthses} {is_valid(prnthses)}')

prnthses1 = '{[()]}{]{}}'
print(f'The {prnthses1} {is_valid(prnthses1)}')

prnthses2 = '({{}} {{ []})'
print(f'The {prnthses2} {is_valid(prnthses2)}')
