import json
my_list = [1,2,3,4,5]
#my_dict={'name':'hari'}
#my_str=' asm_tech'
f = open('a.txt','w')
json.dump(my_list,f)
#json.dump(my_dict,f)
#json.dump(my_str,f)
#print json.dumps(my_list)
f.close()
