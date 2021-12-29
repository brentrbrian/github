#!/usr/bin/env python3
#
# bmgen_db.py - apache script for database access
#
# (C) 2012 Brian Enterprises
#


from mod_python import util
import os, cgitb, urllib, _config, _cgi, _db

TREE = '/var/www/python/htm/tree.htm'
URL  = '/python/bmgen_db.py'
HELP = '/help_db.html'
USER = ''

CX = _cgi.CGI_EXT()
DB = _db.DB()

def index(req):
  #global USER
  cgitb.enable(display=1, logdir=_config.LOG)
  #req.add_common_vars()
  #USER = req.subprocess_env.get("HTTP_USER_AGENT")
  return main(req)
  
def main(req):
  DB.connect()
  a = PageHeader()
  a += ParseParameters(req)
  a += PageFooter()
  DB.disconnect()
  return a


#
#	parse the parameters coming in from apache
#
def ParseParameters(req):

  params = util.FieldStorage(req)

  f = params.get('f', None)

  if f == "SurName": 
    x = params.get('x', None)
    if x:
      x = x.strip()
      x = x.upper()
      return PageFindSurnames(x)
    else:
      return CX.PageError('Error in request [%s,%s]' % (f,x))

  if f == "GivenName":
    x = params.get('x', None)
    if x:
      x = x.strip()
      x = x.upper()
      return PageFindGivenNames(x)
    else:
      return CX.PageError('Error in request [%s,%s]' % (f,x))

  if f == "FirstLetter":
    v = params.get('x', None)
    if v:
      v = v.strip()
      v = v.upper()    
      return PageAllSurnames(v)
    else:
      return CX.PageError('Error in request [%s,%s]' % (f,v))

  if f == "AnyName":
    x = params.get('x', None)
    if x:
      x = x.strip()
      x = x.upper()    
      return PageFindAnyName(x)
    else:
      return CX.PageError('Error in request [%s,%s]' % (f,x))

  if f == "Single":
    x = params.get('x', None)
    x = x.strip()
    x = x.upper()    
    if x:
      return PageSingle(x)
    else:
      return CX.PageError('Error in request [%s,%s]' % (f,x))

  if f == "OneSurname": 
    v = params.get('v', None)
    if v:
      v = v.strip()
      v = v.upper()
      return PageSingleSurname(v)
    else:
      return CX.PageError('Error in request [%s,%s]' % (f,v))

  if f == "Number":
    v = params.get('x', None)
    if v:
      v = v.strip()
      v = v.upper()    
      return PageIndividual(v)
    else:
      return CX.PageError('Error in request [%s,%s]' % (f,v))

  if f == "Individual":
    v = params.get('v', None)
    if v:
      v = v.strip()
      v = v.upper()    
      return PageIndividual(v)
    else:
      return CX.PageError('Error in request [%s,%s]' % (f,v))

  if f == "Tree":
    v = params.get('v', None)
    if v:
      v = v.strip()
      v = v.upper()    
      return PageTree(v)
    else:
      return CX.PageError('Error in request [%s,%s]' % (f,v))

  return ''

#
#
#
def formatDate(date):
  if date:
    date = date.strip()
    date = date.replace(' ','-')
  return date

#
#
#
def MakeGivenNameTable(listRefDict=[]):

  if not listRefDict or not len(listRefDict):
    return CX.PageError('No Data found')

  t  = CX.tablerow(CX.tabledata('align="right" width="9%"',"BIRTH DATE") + 
                   CX.tabledata('align="right" width="9%"',"DEATH DATE") +
                   CX.tabledata('align="right" width="1%"',"") +
                   CX.tabledata('width="80%"',"INDIVIDUAL"))

  t += CX.tablerow(CX.tabledata('align="right" width="9%"','=============') +
                   CX.tabledata('align="right" width="9%"','=============') +
                   CX.tabledata('align="right" width="1%"','') +
                   CX.tabledata('width="80%"','========================================'))

  p  = CX.start_pre()

  for ref in listRefDict:

    if not ref['birthdate']:
      ref['birthdate'] = ''
  
    if not ref['deathdate']:
      ref['deathdate'] = ''

    t += CX.tablerow(CX.tabledata('align="right" width="9%"','%-11s' % (formatDate(ref['birthdate']))) +
                     CX.tabledata('align="right" width="9%"','%-11s' % (formatDate(ref['deathdate']))) +
                     CX.tabledata('align="right" width="1%"','') +
                     CX.tabledata('width="80%"',MakeIndividualHyperlink(ref)))

  p += CX.table('width="100%"',t)
  p += CX.end_pre()
  p += CX.brk()

  return p

#
#
#
def MakeIndividualHyperlink(Ind):
  
  if not Ind:
    return ''

  if not Ind:
    return ''

  hyperlink = "<a href=%s?f=Individual&v=%s>%s</a>\n" % (URL,Ind['iid'],Ind['name'])

  if Ind['parentsfid']:
    hyperlink += "<a href=%s?f=Tree&v=%s>[T]</a>\n" % (URL,Ind['iid'])
      
  return hyperlink


#
#
#
def PageSingle(Id):
  Ind = DB.getIndividual(Id)
  p  = CX.start_pre()
  p += CX.start_p()
  if Id:
    p += '%-40s [%11s] [%11s] %s' % (Ind['name'],formatDate(Ind['birthdate']),formatDate(Ind['deathdate']),Ind['sex'].strip())
    p += CX.end_p()
    p += CX.end_pre()
  return p

#
#
#
def PageAllSurnames(FirstLetter='B'):
  query = "select surname from surnames where surname like '%s'" % (FirstLetter + "%")
  data = DB.getManyFromQuery(query)

  if not data or not len(data):
    return CX.PageError('No data found')

  listLinks = []
  for ref in data:
    listLinks.append("<a href=%s?f=OneSurname&v=%s>%s</a> \n" % (URL,ref['surname'],ref['surname']) + CX.brk())

  return CX.MakeTableFromLinks(listLinks)

#
#
#
def PageFindGivenNames(GivenName):

  listGivenName = GivenName.upper().split(' ')

  if len(listGivenName) <= 1:
    return CX.PageError('Given name must have at NAME plus SURNAME, like: John Jones')

  surname = listGivenName[-1]

  query = "select * from individuals where surname = '%s'" % (surname)
  data = DB.getManyFromQuery(query)

  if not data or not len(data):
    return CX.PageError('No data found')

  results = []
  new_results = []

  for i in range(0,len(data)):

    ref = data[i]

    name = ref['name'].upper().split(' ')

    match_count = 0

    for n in name:
      if n in listGivenName:
        match_count += 1
        
    if match_count > 1:
      results.append((match_count,i))

  if not len(results):
    return CX.PageError('No data found')

  results.sort(reverse=True)
    
  for (match_count,i) in results:
    new_results.append(data[i])

  return MakeGivenNameTable(new_results)


#
#
#
def PageFindAnyName(AnyName):

  AnyName = AnyName.upper()

  nameparts = AnyName.split(' ')

  data = {}

  if not len(nameparts) == 1:
    return CX.PageError('Any name must be a single name, like: John')

  AnyName = nameparts[0].capitalize()
  query = "select * from individuals where name like '%s%s%s'" % ('%',AnyName,'%')
  data = DB.getManyFromQuery(query)

  if not data or not len(data):
    return CX.PageError('No data found')

  return MakeGivenNameTable(data)


#
#
#
def PageFindSurnames(Surname='BRIAN'):
  query = "select surname from surnames where surname like '%s'" % (Surname)
  data = DB.getManyFromQuery(query)

  if not data or not len(data):
    return CX.PageError('No data found')

  p = CX.start_p()

  for ref in data:
    url = "<a href=%s?f=OneSurname&v=%s>%s</a> \n" % (URL,ref['surname'],ref['surname'])
    p += url
    p += CX.brk()

  p += CX.end_p()
  return p

#
#
#
def PageSingleSurname(Surname='BRIAN'):
  query = "select * from individuals where surname = '%s' order by name" % (Surname)
  data = DB.getManyFromQuery(query)

  if not data or not len(data):
    return CX.PageError('No data found')

  return MakeGivenNameTable(data)

#
#
#
def PageIndividual(Id):

  Ind = DB.getIndividual(Id)
  
  if not Ind or not len(Ind):
    return CX.PageError('No data found')
  

  t  = CX.tablerow(CX.tabledata('width="10%"', 'RECORD:') +
                   CX.tabledata('width="10%"', Id) +
                   CX.tabledata('width="10%"', "") +
                   CX.tabledata('width="70%"', ""))

  t += CX.tablerow(CX.tabledata('width="10%"', '') + 
                   CX.tabledata('width="10%"', '') +
                   CX.tabledata('width="10%"', '') +
                   CX.tabledata('width="70%"', ''))

  t += CX.tablerow(CX.tabledata('width="10%"', 'EVENT/NAME') +
                   CX.tabledata('width="10%"', 'BORN/MARR') +
                   CX.tabledata('width="10%"', 'DIED/DIV') +
                   CX.tabledata('width="70%"', 'NAME/LOCATION'))

  t += CX.tablerow(CX.tabledata('width="10%"', '=============') + 
                   CX.tabledata('width="10%"', '=============') +
                   CX.tabledata('width="10%"', '=============') +
                   CX.tabledata('width="70%"', '=============================='))

  ind_name = 'NAME (%s):' % (Ind['sex'].strip())

  t += CX.tablerow(CX.tabledata('width="10%"', ind_name) +
                   CX.tabledata('width="10%"', formatDate(Ind['birthdate'])) +
                   CX.tabledata('width="10%"', formatDate(Ind['deathdate'])) +
                   CX.tabledata('width="70%"', MakeIndividualHyperlink(Ind)))

  if Ind['birthplace']:

    t += CX.tablerow(CX.tabledata('width="10%"', 'BIRTH LOC:') +
                     CX.tabledata('width="10%"', '') +
                     CX.tabledata('width="10%"', '') +
                     CX.tabledata('width="70%"', Ind['birthplace']))

      
  if Ind['deathplace']:

    t += CX.tablerow(CX.tabledata('width="10%"', 'DEATH LOC:') +
                     CX.tabledata('width="10%"', '') +
                     CX.tabledata('width="10%"', '') +
                     CX.tabledata('width="70%"', Ind['deathplace']))

      
  if Ind['parentsfid']:

    parents = DB.getFamily(Ind['parentsfid'])
    father = DB.getIndividual(parents['husbandiid'])
    mother = DB.getIndividual(parents['wifeiid'])

    if parents:

      if father:
      
        t += CX.tablerow(CX.tabledata('width="10%"', '..FATHER:') +
                         CX.tabledata('width="10%"', formatDate(father['birthdate'])) +
                         CX.tabledata('width="10%"', formatDate(father['deathdate'])) +
                         CX.tabledata('width="70%"', MakeIndividualHyperlink(father)))

      if mother:

        t += CX.tablerow(CX.tabledata('width="10%"', '..MOTHER:') + 
                         CX.tabledata('width="10%"', formatDate(mother['birthdate'])) +
                         CX.tabledata('width="10%"', formatDate(mother['deathdate'])) +
                         CX.tabledata('width="70%"', MakeIndividualHyperlink(mother)))

  if Ind['marriagefid']:

    marriagefids = Ind['marriagefid'].split(',')

    for marriagefid in marriagefids:

      marriage = DB.getFamily(marriagefid)

      if not marriage:
        continue

      if marriage['husbandiid'] == Ind['iid']:
        spouse = DB.getIndividual(marriage['wifeiid'])
      else:
        spouse = DB.getIndividual(marriage['husbandiid'])

      if not spouse:
        continue

      t += CX.tablerow(CX.tabledata('width="10%"', '=============') +
                       CX.tabledata('width="10%"', '=============') +
                       CX.tabledata('width="10%"', '=============') +
                       CX.tabledata('width="70%"', '============================='))

      spouse_sex = 'SPOUSE (%s):' % (spouse['sex'].strip())

      t += CX.tablerow(CX.tabledata('width="10%"', spouse_sex) +
                       CX.tabledata('width="10%"', formatDate(spouse['birthdate'])) +
                       CX.tabledata('width="10%"', formatDate(spouse['deathdate'])) +
                       CX.tabledata('width="70%"', MakeIndividualHyperlink(spouse)))


      if marriage['marrplace'] or marriage['marrdate']:

        t += CX.tablerow(CX.tabledata('width="10%"', 'MARR:') +
                         CX.tabledata('width="10%"', formatDate(marriage['marrdate'])) +
                         CX.tabledata('width="10%"', '') +
                         CX.tabledata('width="70%"', marriage['marrplace']))

      if marriage['divplace'] or marriage['divdate']:

        t += CX.tablerow(CX.tabledata('width="10%"', 'DIV:') +
                         CX.tabledata('width="10%"', '') +
                         CX.tabledata('width="10%"', formatDate(marriage['divdate'])) +
                         CX.tabledata('width="70%"', marriage['divplace']))

      if marriage['childreniid']:

        childiids = marriage['childreniid'].split(',')

        for childiid in childiids:

          child = DB.getIndividual(childiid) 

          child_sex = 'CHILD (%s):' % (child['sex'].strip())

          t += CX.tablerow(CX.tabledata('width="10%"', child_sex) +
                           CX.tabledata('width="10%"', formatDate(child['birthdate'])) +
                           CX.tabledata('width="10%"', formatDate(child['deathdate'])) +
                           CX.tabledata('width="70%"', MakeIndividualHyperlink(child)))

  p  = CX.start_tt()
  p += CX.start_pre() 
  p += CX.table('width="100%"',t)
  p += CX.end_pre()
  p += CX.end_tt()
  p += CX.brk()

  return p

#
#
#
def PageTree(Id):
  #                      
  #                 _ifff
  #           _iff
  #                 _iffm
  #     _if
  #                 _ifmf
  #           _ifm
  #                 _ifmm
  # _i
  #                 _imff
  #           _imf
  #                 _imfm
  #     _im
  #                 _immf
  #           _imm
  #                 _immm
  #

  tags = {
            '_i'   : { 'name':'', 'birthdate':'', 'deathdate':'', 'parentsfid':'' },
            '_if'  : { 'name':'', 'birthdate':'', 'deathdate':'', 'parentsfid':'' },
            '_im'  : { 'name':'', 'birthdate':'', 'deathdate':'', 'parentsfid':'' },
            '_iff' : { 'name':'', 'birthdate':'', 'deathdate':'', 'parentsfid':'' },
            '_ifm' : { 'name':'', 'birthdate':'', 'deathdate':'', 'parentsfid':'' },
            '_imf' : { 'name':'', 'birthdate':'', 'deathdate':'', 'parentsfid':'' },
            '_imm' : { 'name':'', 'birthdate':'', 'deathdate':'', 'parentsfid':'' },
            '_ifff': { 'name':'', 'birthdate':'', 'deathdate':'', 'parentsfid':'' },
            '_iffm': { 'name':'', 'birthdate':'', 'deathdate':'', 'parentsfid':'' },
            '_ifmf': { 'name':'', 'birthdate':'', 'deathdate':'', 'parentsfid':'' },
            '_ifmm': { 'name':'', 'birthdate':'', 'deathdate':'', 'parentsfid':'' },
            '_imff': { 'name':'', 'birthdate':'', 'deathdate':'', 'parentsfid':'' },
            '_imfm': { 'name':'', 'birthdate':'', 'deathdate':'', 'parentsfid':'' },
            '_immf': { 'name':'', 'birthdate':'', 'deathdate':'', 'parentsfid':'' },
            '_immm': { 'name':'', 'birthdate':'', 'deathdate':'', 'parentsfid':'' }
        }

  listTags = [['_i'],['_if','_im'],['_iff','_ifm','_imf','_imm'],['_ifff','_iffm','_ifmf','_ifmm','_imff','_imfm','_immf','_immm']]

  Spouse = 'Spouses:' + CX.brk()

  ref = DB.getIndividual(Id)

  if ref['marriagefid']:

    fids = ref['marriagefid'].split(',')

    for fid in fids:
      F = DB.getFamily(fid)

      if int(Id) == F['husbandiid']:
        S = DB.getIndividual(F['wifeiid'])
      else:
        S = DB.getIndividual(F['husbandiid'])

      Spouse += MakeIndividualHyperlink(S)
      Spouse += CX.brk()

  Siblings = 'Siblings:'+ CX.brk()

  if ref['parentsfid']:

    F = DB.getFamily(ref['parentsfid'])

    if F['childreniid']:
      iids = F['childreniid'].split(',')
      for iid in iids:
        if Id != iid:
          S = DB.getIndividual(iid)
          Siblings = Siblings + MakeIndividualHyperlink(S) + CX.brk()

  tags['_i']['name'] = MakeIndividualHyperlink(ref)
  tags['_i']['birthdate'] = formatDate(ref['birthdate'])
  tags['_i']['deathdate'] = formatDate(ref['deathdate'])
  tags['_i']['parentsfid'] = ref['parentsfid']

  p = CX.start_pre()

  for i in xrange(0,3):

    for tag in listTags[i]:

      fathertag = tag + 'f'
      mothertag = tag + 'm'

      tags[fathertag]['name'] = 'Father Unknown'
      tags[mothertag]['name'] = 'Mother Unknown'

      if tags[tag]['parentsfid']:

        parentsiid = DB.getFamily(tags[tag]['parentsfid'])

        Father = DB.getIndividual(parentsiid['husbandiid'])

        if Father:
          tags[fathertag]['name'] = MakeIndividualHyperlink(Father)
          tags[fathertag]['birthdate'] = formatDate(Father['birthdate'])
          tags[fathertag]['deathdate'] = formatDate(Father['deathdate'])
          tags[fathertag]['parentsfid'] = Father['parentsfid']

        Mother = DB.getIndividual(parentsiid['wifeiid'])

        if Mother:
          tags[mothertag]['name'] = MakeIndividualHyperlink(Mother)
          tags[mothertag]['birthdate'] = formatDate(Mother['birthdate'])
          tags[mothertag]['deathdate'] = formatDate(Mother['deathdate'])
          tags[mothertag]['parentsfid'] = Mother['parentsfid']

  fd = open(TREE,'r')

  for L in fd:

    if '_spouse' in L:
      L = L.replace('_spouse',Spouse)

    if '_siblings' in L:
      L = L.replace('_siblings',Siblings)

    if '_i' in L:

      b = L.find('_i')
      e = L.find('<',b)
      tag = L[b:e]

      dates = ''

      if tags[tag]['birthdate']:
        birthdate = tags[tag]['birthdate']
      else:
        birthdate = '__________'

      birthdate = 'b. %s,  ' % (birthdate)

      if tags[tag]['deathdate']:
        deathdate = tags[tag]['deathdate']
      else:
        deathdate = '__________'

      deathdate = 'd. %s' % (deathdate)

      data = tags[tag]['name'] + CX.brk() + birthdate + deathdate

      L = L.replace(tag,data)

    p += L

  fd.close()
  
  p += CX.end_pre()

  return p

#
#
#
def PageHeader():

  letters = ''

  a  = CX.PageHeader(HELP,'DATABASE SEARCH')
  a += CX.start_center()
  a += CX.start_form(URL)
  a += CX.text('x','',40) + ' ' 
  a += CX.brk()
  a += CX.brk()
  a += CX.button('f','GivenName','Given Name') + ' ' 
  a += CX.button('f','SurName','Surname') + ' '
  a += CX.button('f','AnyName','Any Name') + ' '
  a += CX.button('f','FirstLetter','First Letter Of Surname') + ' ' 
  a += CX.button('f','Number','Number')
  a += CX.end_form()
  a += CX.end_center()
  a += CX.brk()
  return a

def PageFooter():
  return CX.PageFooter()

