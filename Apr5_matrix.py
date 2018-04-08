def matrixMult(A, I):
	result = []
	for i in range(0,3):
		row = []
		for j in range(0,3):
			C= 0 
			for k in range(0,3):
				C += A[i][k]*I[k][j]
			row.append(C)
		result.append(row)
	return result

	
	
A = [[3,5,6],[4,8,10],[2,1,8]]
I = [[1,0,0],[0,1,0],[0,0,1]]
mul = matrixMult(A,I)
print("The result of multiplying A and I is ")
print(mul)