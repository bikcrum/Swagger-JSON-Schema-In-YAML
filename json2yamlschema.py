import json

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
    
def parser(json_data,indent):
    if type(json_data) is dict:
        write(indent + 'type: object')
        if len(json_data) > 0:
            write(indent + 'properties:')
        for key in json_data:
            write(indent + '  %s:' % key)
            parser(json_data[key], indent+'    ')
    elif type(json_data) is list:
        write(indent + 'type: array')
        write(indent + 'items:')
        if len(json_data) != 0:
            parser(json_data[0], indent+'  ')
        else:
            write(indent + '  type: object')
    else:
        write(indent + 'type: %s' % gettype(type(json_data).__name__))

parser(json_data,'')
