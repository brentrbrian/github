#!/usr/bin/python
#
# _db.py - database class for python scripts
#
# (C) 2012 Brian Enterprises
#

import pgdb

class MyBMGEN:

  DBH = None

  def __init__(self):
    pass
    
  def connect(self):
    self.DBH = pgdb.connect(host=localhost,user='JohnDoe',password='password',database='db')  
    return self.DBH

  def disconnect(self):
    self.DBH.close()
    return

  def escape_string(self,string):
    return pgdb.escape_string(string)

  def rowToDict(self,row=[],desc=[]):
    if row is None or desc is None: return None
    cols = [ d[0] for d in desc ]
    return dict(zip(cols, row))

  def rowsToDict(self,rows=[],desc=[]):
    if rows is None: return None
    cols = [ d[0] for d in desc ]
    ret = []
    for row in rows:
      ret.append(dict(zip(cols,row)))
    return ret

  def getFamily(self,fid=0):
    query = "select * from families where fid = %s" % (fid)
    cursor = self.DBH.cursor()
    cursor.execute(query)
    rows = cursor.fetchone()
    desc = cursor.description
    cursor.close()
    return self.rowToDict(rows,desc)

  def getIndividual(self,iid=0):
    query = "select * from individuals where iid = %s" % (iid)
    cursor = self.DBH.cursor()
    cursor.execute(query)
    rows = cursor.fetchone()
    desc = cursor.description
    cursor.close()
    return self.rowToDict(rows,desc)

  def getManyFromQuery(self,query):
    cursor = self.DBH.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    desc = cursor.description
    cursor.close()
    return self.rowsToDict(rows,desc)

  def execute(self,query):
    cursor = self.DBH.cursor()
    cursor.execute(query)
    cursor.close()
    return

  def getSchemaDictionary(self):
    dictSchema = {}
    cursor = self.DBH.cursor()

    query = "SELECT column_name FROM information_schema.columns WHERE table_name ='individuals'"  
    cursor.execute(query)
    dictSchema['individuals'] = []
    for i in cursor.fetchall():
      dictSchema['individuals'].append(i[0])

    query = "SELECT column_name FROM information_schema.columns WHERE table_name ='families'"  
    cursor.execute(query)
    dictSchema['families'] = []
    for f in cursor.fetchall():
      dictSchema['families'].append(f[0])

    cursor.close()
    return dictSchema
  
 
  
###############################################################
#
# main()
#
###############################################################
if __name__ == '__main__':
    
  db = MyBMGEN()
  
  db.connect()
  
  schema = db.getSchemaDictionary()
  
  print schema['individuals']
  print schema['families']
  
  db.disconnect()
    


