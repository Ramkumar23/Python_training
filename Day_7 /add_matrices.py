class aa:
	def __init__(self,a,b):
		self.a = a
		self.b = b

	def add(a, b):
    		res = []
    		for i in range(len(a)):
        		row = []
        	for j in range(len(a[0])):
            		row.append(a[i][j]+b[i][j])
        		res.append(row)
    		return res

b = [[2,4], [7,0], [6,3]]
a = [[3,1], [-1,8], [-3, 3]]
aa(a,b)
print aa.add
