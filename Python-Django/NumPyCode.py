#Numpy - Core library for scientific computing. 
#Provides high performance muti dimentional array object, and tools for working with these arrays  

import numpy as np 
'''
a = np.array([1,2,3,8])
print type(a)
print a.shape

print a[0], a[1]

a[0] = 5

print a

b = np.array([ [[1],[2],[3]], [[4],[5],[6]] ])

print b.shape


print b[1,1]

a = np.zeros((2,2))
print a

a = np.ones((1,2))
print a

a = np.full((5,5),9)
print a
'''
'''
a = np.array([ [1,2,3,4], [5,6,7,8], [9,10,11,12] ])

print a
print a.shape

b = a[:2,1:3]

print b

a = np.array([ [1,2,3,4], [5,6,7,8], [9,10,11,12] ])

r1 = a[1, :]
print r1

print a[:, 2]

#dimension
print a.ndim

print a.size
print a.dtype
print a.itemsize

b = np.arange(6)
print b

b = np.arange(12).reshape(3,4)
print b


print np.arange(10000).reshape(100,100)


a = np.array( [ 20,30,40,50 ] )
b = np.arange( 4 )

c = a - b
print c

print b**2

print 10*np.sin(a)

print a < 35



A = np.array([ [1,1], [2,2] ])
B = np.array([ [3,3], [4,4] ])

print A*B

print np.dot(A,B)


def f(x,y):
	return x+y

b = np.fromfunction(f,(4,5), dtype=int)
print b
'''

#SciPy - SciPy adds more functionality by adding large number of functions

'''
from scipy.misc import imread, imsave, imresize

img = imread('b.jpg')
print img.dtype, img.shape
print img.ndim

img_changed = img * [1, 0.95, 0.9]
img_changed = imresize(img_changed, (300,300))

imsave('c.jpg',img_changed)
'''


import numpy as np
from scipy.misc import imread, imsave, imresize
import matplotlib.pyplot as plt 

'''
x = np.arange(0, 3*np.pi , 0.1)

y = np.sin(x)
z = np.cos(x)

plt.plot(x,y)
plt.plot(x,z)
plt.xlabel('x-axis label')
plt.ylabel('y-axis label')
plt.title('Graph')
plt.legend(['Sine','Cosine'])
plt.show()

x = np.arange(0,3 *np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)
plt.subplot(2,1,1)
plt.plot(x,y)

plt.subplot(2,1,2)
plt.plot(x,z)

plt.show()



img = imread('v.jpg')
img_tinted = img * [ 1, 0.95, 0.9]
plt.subplot(1,2,1)
plt.imshow(img)

plt.subplot(1,2,2)
plt.imshow(np.uint8(img_tinted))

plt.show()
'''

'''
import urllib
import urllib2

#import this to open search results for viewing
import webbrowser

#'item' is the key for form input field, for more fields keep adding elements in dictionary
search = urllib.urlencode({'item': 'Python'})

#url of form submission - mentioned in action attribute of form
url = 'http://www.zekelabs.com/search-courses/'
full_url = url + '?' + search
response = urllib2.urlopen(full_url)

#Get the result on form submission in response
with open("search-results.html", "w") as f:
    f.write(response.read())

#open the contents in browser 
webbrowser.open("search-results.html")
'''

#For better understading view source of the website

'''
import urllib
import urllib2

#import this to open search results for viewing
import webbrowser

#'item' is the key for form input field, for more fields keep adding elements in dictionary
search = urllib.urlencode({'item': 'Python'})

#url of form submission - mentioned in action attribute of form
url = 'http://www.zekelabs.com/search-courses/'
full_url = url + '?' + search
response = urllib2.urlopen(full_url)

#Get the result on form submission in response
with open("search-results.html", "w") as f:
    f.write(response.read())

#open the contents in browser 
webbrowser.open("search-results.html")
'''

