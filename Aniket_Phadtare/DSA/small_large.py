arr=[25,10,45,5,30]
smallest=arr[0]
largest=arr[0]
for i in arr:
    if i<smallest:
        smallest=i
        if i>largest:
            largest=i
print("Smallest element:",smallest)
print("Largest element:",largest)            