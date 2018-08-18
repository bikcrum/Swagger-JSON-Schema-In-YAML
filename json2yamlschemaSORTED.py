# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 20:53:54 2018

@author: Bikram Pandit
"""

import json
import yaml

# input file containing json file
with open('data.json') as f:
    json_data = json.load(f)
    
# json schema in yaml format
    
def gettype(type):
    for i in ['string','boolean','integer']:
        if type in i:
            return i
    return type   

def parser(json_data):
    d = {}
    if type(json_data) is dict:
        d['type'] = 'object'
        for key in json_data:
            d[key] = parser(json_data[key])
        return d
    elif type(json_data) is list:
        d['type'] = 'array'
        if len(json_data) != 0:
            d['items'] = parser(json_data[0])
        else:
            d['items'] = 'object'
        return d
    else:
        d['type'] = gettype(type(json_data).__name__)
        return d

p = parser(json_data)
with open('out.yaml','w') as outfile:
    yaml.dump(p,outfile, default_flow_style=False)
