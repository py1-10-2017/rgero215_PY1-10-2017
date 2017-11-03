from datetime import datetime

class Call(object):
    """docstring for Call."""
    num_calls = 0
    def __init__(self, name, number, time, reason):
        self.uid = Call.num_calls
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason

        Call.num_calls += 1

    def display(self):
        print '''Caller UID: {}
Caller Name: {}
Caller Phone Number:{}
Time of Call: {}
Reason for Calling: {}
==========================================='''.format(self.uid, self.name, self.number, self.time, self.reason)
        return self

class CallCenter(object):
    """docstring for CallCenter."""
    def __init__(self):
        self.calls = []
        self.queue = 0

    def add(self, call):
        self.calls.append(call)
        self.queue = len(self.calls)
        print '''Calls in Queue: {}
====================================='''.format(self.queue)
        return self

    def remove(self):
        temp = self.calls[0].uid
        self.calls.remove(self.calls[0])
        self.queue = len(self.calls)
        print '''Call with UID {} has been successfully removed
Remaining Calls: {}
========================================'''.format(temp, self.queue)
        return self

    def find(self, phone):
        for call in self.calls:
            if call.number == phone:
                self.calls.remove(call)
                self.queue = len(self.calls)
        print '''{} has been successfully removed.
========================================'''.format(phone)
        return self

    def sort(self):
        temp_list = []
        for call in self.calls:
            temp_list = sorted(self.calls, key=lambda x: x.uid)
            self.calls = temp_list
        for i in self.calls:
            print '''Calls has been sorted by ascending order {}
======================================'''.format(i.uid)
        return self

    def info(self):
        for call in self.calls:
            print '''Caller Name: {}
Caller Phone: {}
Calls in Queue: {}
======================================'''.format(call.name, call.number, self.queue)
        return self

'''
Uncomment to test it add calls
'''
# caller1 = Call('Ramon Geronimo', '000-000-0000', datetime.now().strftime('%H:%M:%S'), 'I want to cancel my service' ).display()
# caller2 = Call('Juan Geronimo', '111-111-1111', datetime.now().strftime('%H:%M:%S'), 'I want to update my service' ).display()
# caller3 = Call('Eduardo Geronimo', '222-222-2222', datetime.now().strftime('%H:%M:%S'), 'I want to subscribe' ).display()
# caller4 = Call('Frank Geronimo', '333-333-3333', datetime.now().strftime('%H:%M:%S'), 'I nedd help to make a payment' ).display()
#
#
# call_center = CallCenter()
# call_center.add(caller1)
# call_center.add(caller2)
# call_center.add(caller3)
# call_center.add(caller4)
#
# call_center.remove()
#
# call_center.find('222-222-2222')
#
# call_center.sort()
#
# call_center.info()

'''
You can run this file to interactively add calls
'''

def handle_call():
    print "Would You like to make a call?"
    print "type [1] for yes and [0] for no"
    ans = raw_input()
    return int(ans)

def take_call():
    print "What is your name?"
    name = raw_input()
    print "What is your reason for calling?"
    reason = raw_input()
    print "Please confirm your phone number"
    number = raw_input()
    print "Please stay on the line while we proccess your call"
    return Call(name, number, datetime.now().strftime('%H:%M:%S'), reason)

game_on = True
center = CallCenter()
while game_on:
    ring = handle_call()
    if ring == 1:
        center.calls.append(take_call())
        print "All calls today:"
        center.info()
    else:
        game_on = False
