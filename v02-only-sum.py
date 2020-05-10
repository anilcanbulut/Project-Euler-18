import os
import numpy as np

with open('file.txt', 'r') as f:
    lines = f.read().splitlines()		#splitline looks at the line breaks
    last_line = lines[-1]				#get the last line

    size_last_line = len(last_line.split())		#find the size of last line
    arr = np.zeros((size_last_line, size_last_line), dtype=int)		#create a 2D square array with same size of the last line

    for i in range(size_last_line):
    	for j in range(len(lines[i].split())):
    		word = lines[i].split()
    		arr[i][j] = word[j]

for i in range(size_last_line):
	for j in range(size_last_line-i-1):
		
		#Starting from the bottom row, we compare sequential two columns and decide which one is greater.
		#The greater one is added to its adjacent which is its above row.
		#Applying same steps until the top then we get the max sum.
		if (arr[(size_last_line-1) - i][j] > arr[(size_last_line-1) - i][j+1]):
			arr[(size_last_line-1) - i - 1][j] += arr[(size_last_line-1) - i][j]
		else:
			arr[(size_last_line-1) - i - 1][j] += arr[(size_last_line-1) - i][j+1]


print(arr[0][0])


