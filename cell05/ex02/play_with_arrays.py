import array
original = array.array('i', [2, 8, 9, 48, 8, 22, -12, 2])
new = array.array('i', [x + 2 for x in original if x > 5])
print(original.tolist())
print(new.tolist())