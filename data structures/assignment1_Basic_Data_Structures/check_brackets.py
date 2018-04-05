# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            top=Bracket(next,i)
            opening_brackets_stack.append([top.bracket_type,top.position])
        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if len(opening_brackets_stack)==0:
                print(i+1)
                sys.exit()
            top=Bracket(opening_brackets_stack[-1][0],len(opening_brackets_stack)-1)
            if not top.Match(next):
                print(i+1)
                sys.exit()
            if top.Match(next):
                opening_brackets_stack.pop()
    if opening_brackets_stack!=[]:
        print(opening_brackets_stack[0][1]+1)
    else:
        print("Success")




    # Printing answer, write your code here
