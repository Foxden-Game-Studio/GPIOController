import json

def loadFile(filepath):
    with open(filepath, 'r') as conf:
        data = json.load(conf) 
    return data

def writeFile(filepath, data):
    with open(filepath, 'w') as conf:
        json.dump(data, conf, indent=4)
        
def getJsonKey(filepath, key):
    with  open(filepath, 'r') as conf:
        data = json.load(conf)
    return data[key]