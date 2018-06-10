'''
dispatcher.py

General command dispatcher

-Licensed to the Apache Software Foundation (ASF) under one
-or more contributor license agreements.  See the NOTICE file
-distributed with this work for additional information
-regarding copyright ownership.  The ASF licenses this file
-to you under the Apache License, Version 2.0 (the
-"License"); you may not use this file except in compliance
-with the License.  You may obtain a copy of the License at
+License: https://www.binpress.com/license/view/l/89b074d75c23539f3ad7fd68da6fc07e
 
-  http://www.apache.org/licenses/LICENSE-2.0
-
-Unless required by applicable law or agreed to in writing,
-software distributed under the License is distributed on an
-"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
-KIND, either express or implied.  See the License for the
-specific language governing permissions and limitations
-under the License.
'''

from collections import namedtuple

from common.logger import Logger


'''
Global definitions
'''
global_logger = Logger(__file__)


'''
Data container command dispatching with variadic parameters
'''
Command = namedtuple("Command", "command parameters")

'''
Class for registering and dispatching comands
'''
class Dispatcher:

    def __init__(self):

        self.commands = dict()
        
    '''
    Bind a function against a key for dispatching
    '''
    def register(self, i_key, i_fnc, *i_args):
    
        ret = self.exists(i_key)
    
        if ret:
            global_logger.log(
            'Command key',
            i_key, 
            'is occupied with',
            self.commands[i_key],
            '. Not inserting',
            i_fnc.__name__, 
            i_args, 
            ', skipping register')
        else:
            self.replace(i_key, i_fnc, *i_args)
            ret = True
            
        return ret
        
    '''
    Remove key and command from registry
    '''
    def unregister(self, i_key):
    
        if self.exists(i_key):
        
            global_logger.log('Removed command[', i_key, ']:', self.commands[i_key])
            del self.commands[i_key]
        
    '''
    Replace key and command from registry
    '''
    def replace(self, i_key, i_fnc, *i_args):
    
        self.commands[i_key] = [ Command(i_fnc, i_args) ]
        global_logger.log('Replacing with command[', i_key, ']:', self.commands[i_key])
        
    '''
    Append key with new input command
    '''
    def append(self, i_key, i_fnc, *i_args):
    
        command = Command(i_fnc, i_args) 
    
        if not self.exists(i_key):
            self.commands[i_key] = [ command ]
        else:
            self.commands[i_key].append( command )
        
        global_logger.log('Appending with command[', i_key, ']:', self.commands[i_key])
        
    '''
    Invoke binded function
    '''
    def execute(self, i_key):
    
        ret = None
    
        if self.exists(i_key):

            for dispatch in self.commands[i_key]:
            
                global_logger.log(
                'Executing command[', 
                i_key,
                ']:',
                dispatch)
            
                ret = ret and dispatch.command( *dispatch.parameters )
        else:
            global_logger.log('Command[', i_key, '] not recognised. Register before executing. ')
            
        return ret
        
    '''
    Invoke all binded functions
    '''
    def execute_commands(self, i_cmd_key_queue):

        return [ self.execute(cmd_key) for cmd_key in i_cmd_key_queue ]
            
    '''
    Check whether a key has a registered function in the command registry
    '''    
    def exists(self, i_key):
    
        return i_key in self.commands
    
        

    

