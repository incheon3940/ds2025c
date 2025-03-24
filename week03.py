import array

arr = array.array('f',[90, 8, -7, 0, 16])
for i in range(len(arr)):
    print(f"{arr[i]:2} {id(arr[i])}")

l = [99, 99]
print(id(0), id(1))

