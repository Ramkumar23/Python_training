class ss:
	def __init__(self):
		print 'ss'

class rr(ss):
	def __init__(self,a,b):
		self.a = a
		self.b = b
	
	def ar(self):
		return self.a*self.b;
	def __str__(self):
		
		return str(self.a)+str(self.b);
		
	def pr(self):
		return 2 * self.a + self.b;



c=rr(10,50)
print c.ar()
print c.pr()
