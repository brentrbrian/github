# a dictionary can be multi-dimensional

dictPERSONNEL = \
{
  'brent' : { 'hair' : 'not so much', 'title' : 'firmware', 'location' : 'Raleigh, NC, USA' },
  'randy' : { 'hair' : 'a little',    'title' : 'owner',    'location' : 'York, SC, USA'    }
}

print(dictPERSONNEL['brent']['location'])
print(dictPERSONNEL['randy']['title'])