import json
my_dict = {'name':'hari', 'org':'zasm', 'pack':['python','ajs','html']}
print json.dumps(my_dict,indent=10,sorted_key=True)
