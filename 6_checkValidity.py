class CheckValidity:
    def __init__(self,string):
        self.sequenceStr = string
    def check_validity(self):
        strlist = list(self.sequenceStr)
        stack = []
        for char in strlist:
            if char=='(' or char=='{' or char=='[':
                stack.append(char)
            if char==')':
                if not stack:
                    return 0
                elif stack[-1]=='(':
                    stack.pop()
                else:
                    return 0
            if char=='}':
                if not stack:
                    return 0
                elif stack[-1]=='{':
                    stack.pop()
                else:
                    return 0
            if char==']':
                if not stack:
                    return 0
                elif stack[-1]=='[':
                    stack.pop()
                else:
                    return 0
        if stack:
            return 0
        else:
            return 1

seqStr = input("Enter string: ")
obj = CheckValidity(seqStr)
if obj.check_validity()==0:
    print("Invalid String")
else:
    print("Valid String")
