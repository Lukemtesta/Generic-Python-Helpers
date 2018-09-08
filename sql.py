'''
sql.py

Python module containing sql helpers

Dependencies:

pip install flask flask-jsonpify flask-sqlalchemy flask-restful 
pip freeze
'''

import os
import sys
import flask

'''
Construct a resource path
'''
def build_resource_path(i_resource):

    if isinstance(i_resource, list):
        i_resource = '/'.join(i_resource)

    return '/' + i_resource

'''
Execute database request on an sql database
'''
def execute_request(i_database, i_request):

    conn = i_database.connect() 
    return conn.execute(i_request).cursor.fetchall()

'''
Select property from a group in an sql database. Reads all by default
'''
def select_property_from_group(i_database, i_group, i_properties = '*'):

    request = build_select_database_string(i_group, i_properties)
    return execute_request(i_database, request)
    
'''
Select property from a group in an sql database. Reads all by default
'''
def match_field_from_group(i_database, i_group, i_properties, i_field, i_value):

    request = build_match_item_database_string(i_group, i_properties, i_field, i_value)
    return execute_request(i_database, request)
        
'''
Construct an sql database command string for selecting group properties
'''
def build_select_database_string(i_group, i_properties):

    ret = None

    if isinstance(i_properties, list):
        i_properties = ', '.join(i_properties)
        
    if not isinstance(i_group, list): 
        ret = 'select ' + i_properties + ' from ' + i_group

    return ret
    
'''
Construct an sql database command string for matching properties from groups
'''
def build_match_item_database_string(i_group, i_properties, i_field, i_value):

    ret = build_select_database_string(i_group, i_properties)

    if ret:
        ret = ret + ' where ' + i_field + ' = ' + i_value

    return ret
    
    
    