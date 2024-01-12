# the items in a list can be changed

print('--------')

listA = [1,2,3,4,5]

for i in listA:
  print(i)
  
# a python list not an array of TYPE, it
# is a list of objects, numbers, alphabet, objects
  
listA[3] = 'Z'

print('--------')

for i in listA:
  print(i)

