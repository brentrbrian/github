import _MyBMGEN, _webSSDI, _webPARSER

dictMonths = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12 }

def compareDates(date1,date2):
    d1 = db.getDate(date1)
    d2 = db.getDate(date2)
    for i in ['year','month','day']:
        if d1[i] < d2[i]: return -1
        if d1[i] > d2[i]: return 1
    return 0
  
def getDate(date):
    
    result =  { 'year':0, 'month':0, 'day':0 }
    
    try:
        f = date.split(' ')
        if len(f) == 1:
            result =  { 'year':int(f[0]), 'month':0, 'day':0 }
        if len(f) == 2:
            result =  { 'year':int(f[1]), 'month':dictMonths[f[0]], 'day':0 }
        if len(f) == 3:
            result =  { 'year':int(f[2]), 'month':dictMonths[f[1]], 'day':int(f[0]) }
    except:
        pass
      
    return result 

def getHusbandSurnames(data):
    if len(data['marriagefid']):
      listMarr = data['marriagefid'].split(',')
      for marr in listMarr:
          m = db.getFamily(marr)
          if m:
              h = db.getIndividual(m['husbandiid'])
              if h:
                  data['last'].append(h['surname'])

def getDataStd(ind):    
    data = {}
    data['birth'] = getDate(ind['birthdate'])
    data['birthplace'] = ind['birthplace']
    data['death'] = getDate(ind['deathdate'])
    data['name'] = ind['name'].upper()
    data['first'] = ind['name'].split(' ')[0].upper()
    data['last'] = [ind['surname']]
    data['marriagefid'] = ind['marriagefid']
    return data

def getDataMale(ind):
    data = getDataStd(ind)
    return data

def getDataFemale(ind):
    data = getDataStd(ind)
    if (data['marriagefid']): getHusbandSurnames(data)
      
    return data

def print_it(fd,data):
    
    fd.write('%s\n' % (data))
    print data

########################################
#
# main
#
########################################

db = _MyBMGEN.MyBMGEN()
ss = _webSSDI.webSSDI()

fd = open("ssdi_report.txt","w")

db.connect()

cursor = db.DBH.cursor()

query = 'select max(iid) from individuals'

cursor.execute(query)
maxCount = cursor.fetchone()[0]
cursor.close()

for iid in xrange(1,maxCount+1):
  
    ind = db.getIndividual(iid)
    
    if not ind: continue
    
    if ind['sex'].strip() == 'M':
        data = getDataMale(ind)
    else:
        data = getDataFemale(ind)
        
    if '*' in ind['surname']: continue
   
    if data['birth']['year'] == 0: continue
    if data['birth']['year'] and data['death']['year']: continue        
    if data['birth']['year'] and data['birth']['year'] < 1860: continue            
    if data['death']['year'] and data['death']['year'] < 1920: continue

    by = data['birth']['year']
    dy = data['death']['year']
    first = data['first']
  
    head = '%5d %-35s %11s %11s %-20s' % (iid,ind['name'].upper(),ind['birthdate'],ind['deathdate'],ind['birthplace'])

    for last in data['last']:
     
      listPage = ss.getListFromPage(first,last,by,0,0,0,0,0,0)
      
      if not listPage or len(listPage) == 0: continue
      
      if head: 
        print_it(fd,'\n%s' % (head))
        head = None
  
      for t in listPage:
        (name,birth,death,age,residence,benefit,issued,ssn) = t
        print_it(fd,'      %-35s %11s %11s %s %s %s %s' % (name,birth,death,age,residence,benefit,issued))

fd.close()           
            
