Tuple=(12,34,24,123,423,132,11,23,4323,2134,431,2,4113)
largest=Tuple[0]
for i in Tuple:
    if i>largest:
        largest=i
print("largest number is :",largest)