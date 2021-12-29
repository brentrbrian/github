import urllib, _webPARSER

class webSSDI:
    
    url = 'http://www.familytreelegends.com/records/ssdi/search?l=%s&f=%s&by=%s&bm=%s&bd=%s&dy=%s&dm=%s&dd=%s&offset=%d'
    wp = _webPARSER.webPARSER()
    
    def getListFromPage(self,first,last,by=0,bm=0,bd=0,dy=0,dm=0,dd=0,offset=0):
        if bm == 0: bm = '' # birth month
        if bd == 0: bd = '' # birth day
        if by == 0: by = '' # birth year
        if dm == 0: dm = '' # death month
        if dd == 0: dd = '' # death day
        if dy == 0: dy = '' # death year
        
        url = self.url % (last,first,by,bm,bd,dy,dm,dd,offset)
        page = urllib.urlopen(url).read()
        text = self.wp.getTextDict(page)
        
        rows = text['tr']
        
        # do we have enough rows to indicate there is data ?
        if len(rows) == 73: return None
    
        listDATA = []
    
        for r in rows:
            # skip row if not a list
            if type(r) == type(''): continue
            # skip row if less than 20 items
            if len(r) < 20: continue
            # skip row if it is the heading
            if r[1] == 'Name': continue
            # ,Name,,,Birth,,,Death,,,Age,,,Last Residence,,,Last Benefit,,,Issued By,,,SSN,,,,Extras,,
            (name,birth,death,age,residence,benefit,issued,ssn) = ([r[1],r[4].strip(),r[7].strip(),r[10],r[13],r[16],r[19],r[22]])
            listDATA.append((name,birth,death,age,residence,benefit,issued,ssn))        
    
        return listDATA
    
#######################################################
#
# UNIT TEST
#
####################################################### 
if __name__ == '__main__':
    ssdi = webSSDI()
    page = ssdi.getListFromPage('John','Brian','1917')
    for p in page:
      print p

