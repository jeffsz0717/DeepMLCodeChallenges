## Question
##Write a Python function that computes the transpose of a given matrix.

## Solution
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	c = len(a[0])	
	output = [[] for i in range(c)]
	while a:
		_list = a.pop(0)
		for i, v in enumerate(_list):
			output[i].append(v)
	return output

## Time Complexity: O(r * c)
## Best Solution: return [list(zip(*a))] ; The TC is still O(r*c) but runs much faster as the in-built solution.