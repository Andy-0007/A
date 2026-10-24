rows=int(input("Enter the Number of Rows: "))
columns=int(input("Enter the Number of Columns: "))

A=[]
print("Enter the Elements of First Matrix:")
for i in range(rows):
  row=[]
  for j in range(columns):
    x=int(input("Enter the elements: "))
    row.append(x)
    A.append(row)
    print("Matrix a is", A)

B=[]
print("Enter the Elements of Second Matrix:")
for i in range(rows):
  row=[]
  for j in range(columns):
    x=int(input("Enter the elements: "))
    row.append(x)
  B.append(row)
  print("Matrix a is", B)

C=[]
for i in range(rows):
      row=[]
      for j in range(columns):
        row.append(A[i][j]+ B[i][j])
        C.append(row)
print("Result Matrix is:",C)

