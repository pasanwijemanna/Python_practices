import re

str = 'Hello Ben10?'

y = re.findall('\d',str)
print(y)

x = re.findall('\w',str)
print(x)

z = re.findall('\w\w\w\w\w',str)
print(z)


a = re.findall('\w{3}\d{2}',str)
print(a)

b = re.findall('\w{2}',str)
print(b)

c = re.findall('\w{2,3}',str)
print(c)

d = re.findall('\w+',str)
print(d)

e = re.findall('\w*',str)
print(e)

f = re.findall('\w?',str)
print(f)

g = re.findall('\w+$',str)
print(g)




txt = "i am pasanwijemanna54@gmail.com and i'm Machine Learning Engineer and Zuucrew@gmail.com"

h = re.findall('\w+@gmail.com',txt)
print(h)


i = re.search('Engineer',txt)
print(i)


g = re.split('\s',txt)
print(g)


k = re.sub('M\w{6}','AI',txt)
print(k)