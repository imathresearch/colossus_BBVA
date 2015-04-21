'''
File to be  located at /etc/colossus/colossus.config
'''

import sys
import numpy
import os
import pickle


#f = open ("/mount_iMathCloud/fichero.txt", "w")
#f.write("Running exec startClient\n")
#f.close()

module_name = sys.argv[1]
class_name = sys.argv[2]

b= module_name.split('.')
b.pop();
parent_name = '.'.join(b)

print module_name
print parent_name
print class_name

try:
        colossus_subclass = getattr(__import__(module_name, fromlist=[parent_name]), class_name)
except ImportError, exception:
        print "Could not find module: {0}".format(sys.argv[1])
        quit()

#data = [[755, 683, 249, 430, 342], [778, 849, 531, 416, 938], [568, 275, 170, 428, 550], [11, 525, 314, 6, 485], [346, 507, 552, 230, 537], [578, 575, 23, 455, 682], [531, 214, 287, 396, 855], [798, 173, 126, 929, 152], [134, 660, 483, 600, 567], [184, 460, 652, 566, 990]]


#datas = []
#aux = numpy.array(data) + 1
#datas = datas + [aux]

#datas =  pickle.load( open( sys.argv[6], "rb" ) )

print sys.argv[6:]
colossus_subclass(*sys.argv[6:]).startClient(sys.argv[3], sys.argv[4], sys.argv[5])

