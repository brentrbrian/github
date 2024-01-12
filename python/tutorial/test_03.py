# a dictionary can be changed, and it has an iterator

print('--------')

dictA = { 'brent' : 'firmware', 'randy' : 'owner' }

for i in dictA:
  print(i)

print('--------')

for i in dictA:
  print(i, dictA[i])
  
dictA['brent'] = 'Sr. firmware'

print('--------')

for i in dictA:
  print(i, dictA[i])