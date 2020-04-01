def checkdict(var):
    return str(type(var)) == "<class 'dict'>"
    
def flattendict(d,newdict,key):
    if not checkdict(d):
       newdict[key] = d
       return
       
   for i in d:
       newkey = '{}.{}'.format(key,i) if key else i
       flattendict(d[i],newdict,newkey)
       
def ans(d):
    newdict = dict()
    flattendict(d,newdict,' ')
    return newdict
    
d = {'key': 3,'foo': {'a': 5,'bar': {'baz': 8}}}
print(ans(d))
