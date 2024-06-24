#Importing Modules
import numpy as np
import pandas as pd
from art import text2art

#Create numpy array of size 10 of zeros 
my_array1=np.zeros(10)
print(my_array1)

#Create 9x9 numpy array of random numbers 
my_array2=np.random.randint(0,21,81).reshape(9,9)
print(my_array2)

#Create 3 numpy array of size 1x3 
first_array=np.array([1,2,3])
second_array=np.array([4,5,6])
third_array=np.array([7,8,9])
my_array3=np.vstack([first_array,second_array,third_array])
print(my_array3)

# Save the arrays to the file with headers
with open('test1.txt', 'w') as f:
    f.write('# Array 1\n')
    np.savetxt(f,my_array1)
    f.write('# Array 2\n')
    np.savetxt(f, my_array2)
    f.write('# Array 3\n')
    np.savetxt(f, my_array3)

# Function to read arrays from the file
def read_arrays_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    arrays = []
    current_array = []
    for line in lines:
        if line.startswith('#'):
            if current_array:
                arrays.append(np.array(current_array))
                current_array = []
        else:
            current_array.append(list(map(float, line.split())))
    if current_array:
        arrays.append(np.array(current_array))
    
    return arrays

#appending number to the first array
my_array1_new=np.append(my_array1,0)
with open('test1.txt', 'a') as f:
    f.write('# Array 1 new\n')
    np.savetxt(f,my_array1_new)
    
#Reshaping array 3
my_array2_new=my_array2.reshape((3,27))
with open('test1.txt', 'a') as f:
    f.write('# Array 2 new\n')
    np.savetxt(f,my_array2_new)


# Read the arrays from the file
arrays = read_arrays_from_file('test1.txt')

# Print the arrays to verify
for i, array in enumerate(arrays, 1):
    print(f"Array {i}:\n{array}\n")

print(text2art("Joe Amin",font='slant'))
