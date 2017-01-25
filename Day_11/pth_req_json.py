import json
import requests as r
import re

a= r.get('http://122.181.186.42:9200/raaga')
json_str = a.text

json_dict = json.dumps(json_str)

#print json_dict
#uuid\
p=re.compile(r'"uuid(.*),')
f=re.findall(p,json_dict)
print f
