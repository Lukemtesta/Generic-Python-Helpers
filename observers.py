'''
observers.py

License: https://www.binpress.com/license/view/l/89b074d75c23539f3ad7fd68da6fc07e
'''

import math

'''
Observable base class capable of notifying a registered observer
'''
class Observable:
    
    def __init__(self):
        self.observers = []
        
    def register(self, observer):
        ret = isinstance(observer, Observer)
        if(ret):
            self.observers.append(observer)
        return ret
        
    def unregister(self, observer):
        ret = isinstance(observer, Observer)
        if(ret):
            items = filter(lambda x: x is observer, self.observers)
            self.observers.remove(items)
        return ret
        
    def unregister_all(self):
        del self.observers[:]
        
    def notify_all(self, *kwargs):
        ret = [observer.notify(self, kwargs) for observer in self.observers]
        return math.floor(sum(ret) / len(ret))
        
    def run(self):
        print('Base observable run')
        self.notify_all()
     
     
'''
Observer base class capable of being notified by a registered observable
'''  
class Observer:

    def __init__(self, observable = None):
        if(isinstance(observable, Observable)):
            observable.register(self)
    
    def notify(self, *kwargs):
        print('Base observer notified')
        
    