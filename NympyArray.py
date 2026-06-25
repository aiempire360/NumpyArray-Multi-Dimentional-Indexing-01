import numpy as np

#lst= [ 10, 20, 30 , 40]

#numArray = np.array([ 10, 20, 30 , 40])

#doublelist= lst * 2
#print(doublelist)

#doubleArray = numArray * 2

#print(doubleArray)

#print(numArray.ndim)

#dimention

numArray = np.array ( [
                     [ ['A', 'B', 'C' ],['D', 'E', 'F'], ['G', 'H', 'I'] ],
                     [ [ 'J', "K", 'L' ], ['M', 'N', 'O'], ['P', 'Q', 'R'] ],
                     [ ['S', 'T', 'U'], [ 'V', 'W', 'X'], ['Y', 'Z', ' '] ]
                       ])

print(numArray.shape)

#chain indexing

print(numArray[1][2][0])

#multidimentional indexing
print(numArray[1][2][1])

text = numArray[0][0][0] + numArray[0][2][2] + numArray[2][2][2] + numArray[0][1][1] + numArray[1][1][0] + numArray[1][2][0] + numArray[0][2][2] + numArray[1][2][2] + numArray[0][1][1]
print(text)