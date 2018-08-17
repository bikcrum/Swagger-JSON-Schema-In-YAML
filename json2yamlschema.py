
import json
from pprint import pprint

# input file containing json file
with open('data.json') as f:
    json_data = json.load(f)
    
# json schema in yaml format
out = open('out.yaml','w')

def gettype(type):
    for i in ['string','boolean','integer']:
        if type in i:
            return i
    return type

def write(string):
    print(string)
    out.write(string+'\n')
    out.flush()
    
    
def parser(json_data,intend):
    if type(json_data) is dict:
        write(intend + 'type: object')
        write(intend + 'properties:')
        for key in json_data:
            write(intend + '  %s:' % key)
            parser(json_data[key], intend+'    ')
    elif type(json_data) is list:
        write(intend + 'type: array')
        write(intend + 'items:')
        if len(json_data) != 0:
            parser(json_data[0], intend+'  ')
        else:
            write(intend + '  type: object')
    else:
        write(intend + 'type: %s' % gettype(type(json_data).__name__))
    

parser(json_data,'')
