'''
base_abstract_factory.py

Base builder implementing factory

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

from factory import Factory

'''
Concrete implementation of an abstract factory
'''
class BaseAbstractFactory:

    def __init__(self, i_key = None, *i_params):
    
        self.factory = Factory()
                
        self.key = i_key
        self.params = i_params
        
        self.reset_accepted_types()
        
    '''
    Register valid parameter to constrain class
    '''
    def set_type_constraint(self, i_types):
    
        self.reset_accepted_types()
        
        self.accepted_types.append(i_types)
        
    '''
    Clear accepted types
    '''
    def reset_accepted_types(self):
    
        self.accepted_types = []
        
    '''
    Test whether parameters are accepted
    '''
    def are_parameter_types_accepted(self, i_params):
    
        ret = True
        
        # Ugly to support python 2 (type evaluates tuples as 'instance'). Python 3 use [ for ... ] and all(ret)
        if self.accepted_types:
            for param in i_params:
                print('type', type(param))
                ret = ret and max([isinstance(param, accepted_type) for accepted_type in self.accepted_types])
                
        return ret
        
    '''
    Keep the parameters up-to-date manually to use override make_object calls
    '''
    def update_parameters(self, *i_args):
    
        assert self.are_parameter_types_accepted(i_args)
    
        self.params = i_args
                
    '''
    Create an object using the factory and defined descriptor
    '''
    def make_object(self, i_key, *i_args):

        assert self.are_parameter_types_accepted(i_args)
    
        self.key = i_key
        self.params = i_args

        return self.factory.make_object(i_key, *i_args)
        