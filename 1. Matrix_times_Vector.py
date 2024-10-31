## Question:
## Write a Python function that takes the dot product of a matrix and a vector. return -1 if the matrix could not be dotted with the vector

## Soluition
def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
		
	if len(a) == len(b):
		c = []
		for _list in a:
			if len(_list) == len(b):
				check = sum(map(lambda x,y:x*y, _list, b)) 
				c.append(check)
			else:
				return -1
		return c
	return -1

## test case#1: print(matrix_dot_vector([[1,2,3],[2,4,5],[6,8,9]],[1,2,3]) == [14, 25, 49])
## test case#2: print(matrix_dot_vector([[1,2],[2,4],[6,8],[12,4]],[1,2,3]) == -1) 