class CheckValidity:
    def __init__(self,string):
        self.sequenceStr = string
    def check_validity(self):
        strlist = list(self.sequenceStr)
        stack1 = []
        stack2 = []
        stack3 = []
        for char in strlist:
            if char=='(':
                stack1.append(char)
            if char==')':
                if not stack1:
                    return 0
                else:
                    stack1.pop()
            if char=='{':
                stack2.append(char)
            if char=='}':
                if not stack2:
                    return 0
                else:
                    stack2.pop()
            if char=='[':
                stack3.append(char)
            if char==']':
                if not stack3:
                    return 0
                else:
                    stack3.pop()
        if stack1 or stack2 or stack3:
            return 0
        else:
            return 1

seqStr = input("Enter string: ")
obj = CheckValidity(seqStr)
if obj.check_validity()==0:
    print("Invalid String")
else:
    print("Valid String")
