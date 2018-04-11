'''
observers.py

Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
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
        
    