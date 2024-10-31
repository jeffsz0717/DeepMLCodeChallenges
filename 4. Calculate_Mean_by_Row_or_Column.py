## Question: Write a Python function that reshapes a given matrix into a specified shape

## Solution:
import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	#reshaped_matrix = np.reshape(a, new_shape)
	
        r_old, c_old = len(a), len(a[0])
        r, c = new_shape[0], new_shape[1]
        
        new_mat = [[0]*c for i in range(r)]
        for i in range(r*c):
                new_mat[i//r][i%c] = a[i//r_old][i%c_old]
                
        return new_mat