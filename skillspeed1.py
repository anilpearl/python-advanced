# def funGenerator(n):
# 	return lambda x : x * n


# f5 = funGenerator(5) #func that takes arg & returns 5 multiple of it
# f6 = funGenerator(6) #func that takes arg & returns 6 multiple of it

# print f5(5)
# print f6(7) 

# functions = [lambda x : x * 2, lambda x : x * 4]

# for i in range(1,5):
# 	for f in functions:
# 		print f(i)


# f = lambda x,y: x+y

# print f(5,6)

# l = [ [5,6], [2,-1], [33,5], [99,4] ]
# print sorted(l, key = lambda x: x[1])


#Packing
# def func(*vargs):
# 	for varg in vargs:
# 		print varg,

# func(1,2)
# func(4,6,7,7)

#Unpacking
# l = ['awantik', 'bangalore']

# def func(name,loc):
# 	print name,loc

#func(*l)


#Default Arguments

# def func(name,age=30,location='Bangalore'):
# 	print name,location,age

# func('Awantik Das',90,'Mumbai')
# func('Awantik',77)
# func('Awi')

#Named Arguments

# def namedFunc(name,address):
# 	print name,address

# namedFunc(address='Bangalore',name='Awantik')

# def kwargs(n,*args,**kwargs):
# 	print n,args,kwargs

# kwargs('Awantik','saterday',1000,name='Awi',location='Bangalore',age=10)

db = {'name':'Awantik','location':'Bangalore'}

def kwargs(name,location):
	print name,location

kwargs(**db)



