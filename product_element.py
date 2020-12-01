#This script generate the product of a set of elements of an arbitrary lenght (= all the possible combinations)
#sest: ABC, lenght: 4
#Combinations: AAAA, AAAB,AAAC, AABA, AABB, AABC, ecc..

import itertools

#Set elements and lenght:
set_elements = '01'
set_lenght = 5

all_list = []
all_list = list(itertools.product(set_elements, repeat=set_lenght))

print "Number of sets: "+str(len(all_list))

#print all sets, one per line
for set in all_list:
	for item in set:
		print item,		
	print

'''

#other code that can be useful
for set in all_list:
    #assign a variable for each element of the combination; useful if you need the sequence as input for other stuff
	var1,var2,var3,var4,var5 = set
	print var1
	print var2
	print var3
	print var4
	print var5
'''