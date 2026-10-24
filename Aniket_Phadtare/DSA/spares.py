A=[
    [0,0,1,0],
    [1,0,0,2],
    [0,0,0,0]
    ]

zero=0
non_zero=0
for r in A:
    for x in r:
        if x==0:
            zero+=1
        else:
            non_zero+=1

if zero>non_zero:
    print("Matrix is Sparse")
else:
    print("Matrix is Not Sparse")            