# the items in a tuple can not be changed

print('--------')

tupleA = (1,2,3,4,5)

for i in tupleA:
  print(i)
  
# a python tuple not an array of TYPE, it
# is a list of objects, numbers, alphabet, objects that are fixed (constant)
  
tupleA[3] = 'Z'

print('--------')

for i in listA:
  print(i)

