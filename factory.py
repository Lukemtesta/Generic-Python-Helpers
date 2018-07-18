'''
factory.py

License: https://www.binpress.com/license/view/l/89b074d75c23539f3ad7fd68da6fc07e

Abstract factory that creates objects with static make. No type restrictions
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