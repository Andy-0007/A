Tuple=(12,34,24,123,423,132,11,23,4323,2134,431,2,4113)
smallest=Tuple[0]
for i in Tuple:
    if i<smallest:
        smallest=i
print("smallest number is :",smallest)