'''
factory.py

Abstract factory that creates objects with static make. No type restrictions

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


'''
Implementation of factory
'''
class Factory:

    def __init__(self):

        self.registry = dict()
        
    '''
    Register an id against a factory type. Overwrites existing ids
    '''
    def register(self, i_id, i_type):
    
        if not hasattr(i_type, 'make'):
            raise NotImplementedError('Class ' + i_type + ' must implement a static make')
    
        self.unregister(i_id)
        self.registry[i_id] = i_type.make
        
    '''
    Unregister an id against a factory type.
    '''
    def unregister(self, i_id):
    
        if i_id in self.registry:
            del self.registry[i_id]
    
    '''
    Clear all registered types
    '''
    def clear(self):
    
        self.registry.clear()
        
    '''
    Make an object based on some parameters. Returns None if id is not registered
    '''
    def make_object(self, i_id, *i_args):
    
        ret = None
    
        if i_id in self.registry:
            ret = self.registry[i_id](*i_args)
            
        return ret