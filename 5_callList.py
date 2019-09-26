class CallDetail:
    def __init__(self,callingNo,calledNo,dur,ctype):
        self.diallingNo = callingNo
        self.dialledNo = calledNo
        self.duration = dur
        self.callType = ctype

    def print_call_details(self):
        print("Dialling No: "+self.diallingNo+"\n Dialled No: "+self.dialledNo+"\n Call Duration: "+self.duration+"\n Call type: "+self.callType+"\n")

class Util:
    def __init__(self):
        self.list_of_call_objects = list()

    def parse_customer(self,list_of_call_string):
        for call in list_of_call_string:
            callList = call.split(',')
            self.list_of_call_objects.append(CallDetail(callList[0],callList[1],callList[2],callList[3]))

    def print_list(self):
        i=1
        for obj in self.list_of_call_objects:
            print("Call Details "+str(i)+"\n")
            obj.print_call_details()
            i+=1
    
call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'
list_of_call_string=[call,call2,call3]
u = Util()
u.parse_customer(list_of_call_string)
u.print_list()
