import pickle
my_list = [1,2,3,4,5]
my_dict={'name':'hari'}
my_str=' asm_tech'
f = open('a.txt','w')
pickle.dump(my_list,f)
pickle.dump(my_dict,f)
pickle.dump(my_str,f)
#print pickle.dumps(my_list)
f.close()
