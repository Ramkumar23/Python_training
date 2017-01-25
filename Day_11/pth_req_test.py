import requests as r
g= r.post('http://122.181.186.42:9200/raaga',{'name':'raaga'})
a= r.get('http://122.181.186.42:9200/raaga')
print a.text
