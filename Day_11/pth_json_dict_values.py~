import json
import requests as r
import re

a= r.get('http://122.181.186.42:9200/raaga')
json_str = a.text

json_dict = json.loads(json_str)


print json_dict.keys()

print json.dumps(json_dict, indent=5)
