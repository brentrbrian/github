#!/usr/bin/env python3
#
# _cgi.py - html class for python scripts
#
# (C) 2012 Brian Enterprises
#

import _config

class CGI_EXT:

  nl = "\n"  

  def __init__(self):
    pass

  def newlines(self,on=True):
    if on:
      self.nl = "\n"
    else:
      self.nl = ''

  def a(self,url,text):
    return '<a href="%s">%s</a>%s' % (url,text,self.nl)

  def image(self,image):
    return '<img src="%s">%s' % (image,self.nl)

  def comment(self,comment):
    return '<! -- %s -- >%s' % (self.nl) 

  def button(self,name,value,label):
    return '<button type="submit" name="%s" value="%s">%s</button>%s' % (name,value,label,self.nl) 

  def text(self,name,text,size):
    return '<input type="text" name="%s" value="%s" size="%d" maxlength="%d">%s' % (name,text,size,size,self.nl)

  def hidden_text(self,name,value):
    return '<input type="hidden" name="%s" value="%s">%s' % (name,value,self.nl) 

  def title(self,title):
    return '<title>%s</title>%s' % (title,self.nl)

  def hr(self,align,percent):
    return '<hr align="%s" width="%s">%s' % (align,percent,self.nl)

  def h1(self,text): 
    return '<h1>%s</h1>%s' % (text,self.nl) 

  def brk(self): 
    return '<br>%s' % (self.nl) 

  def start_head(self,CSS=None):
    a =  '<head>%s' % (self.nl)
    a += '<meta http-equiv="CONTENT-TYPE" content="text/html; charset=utf-8">%s' % (self.nl)
    a += '<meta name="viewport" content="width=device-width, initial-scale=1">%s' % (self.nl)
    if CSS: a += '%s%s' % (CSS,self.nl)
    return a

  def end_head(self):
    return '</head>%s' % (self.nl)

  def start_bold(self):
    return '<b>%s' % (self.nl)

  def end_bold(self):
    return '</b>%s' % (self.nl)

  def bold(self,text): 
    return '<b>text</b>%s' % (text,self.nl)

  def option_select(self,value,text,select):
    return '<option value="%s" >%s%s%s' % (value,text,select,self.nl)

  def select(self,name,options):
    return '<select name="%s">%s</select>%s' % (name,options,self.nl) 

  def start_p(self):
    return '<p>%s' % (self.nl) 

  def end_p(self):
    return '</p>%s' % (self.nl) 

  def start_form(self,url):
    return '<form method="get" action="%s">%s' % (url,self.nl) 

  def end_form(self):
    return '</form>%s' % (self.nl) 

  def start_html(self):
    a  = ''
    #a += '<!DOCTYPE html>%s' % (self.nl)
    a += '<html>%s' % (self.nl)
    return a 

  def end_html(self):
    return '</html>%s' % (self.nl) 

  def start_body(self):
    return '<body>%s' % (self.nl) 
  
  def end_body(self): 
    return '</body>%s' % (self.nl) 

  def start_center(self):  
    return '<center>%s' % (self.nl) 

  def end_center(self):  
    return '</center>%s' % (self.nl) 

  def start_tt(self):
    return '<tt>%s' % (self.nl) 

  def end_tt(self):  
    return '</tt>%s' % (self.nl) 

  def start_pre(self):
    return '<pre>%s' % (self.nl) 

  def end_pre(self):
    return '</pre>%s' % (self.nl)

  def tabledata(self,tableparm,data):
    return '<td %s>%s</td>%s' % (tableparm,data,self.nl)

  def tablerow(self,row):
    return '<tr>%s</tr>%s' % (row,self.nl)

  def table(self,tableparm,tabledata):
    return '<table %s>%s</table>%s' % (tableparm,tabledata,self.nl)

  def meta_content(self,name,value):
    return '<meta name="%s" content="%s">%s' % (name,value,self.nl)

  def MakeTableFromLinks(self,listLinks):
    a  = ''
    for link in listLinks:
      a += link
    return a

  def FileDialog(self,label='FILENAME'):
    return '%s: <input type="file" name="filename"><br>' % (label)


  def PageHeader(self,HELP=None,TITLE='',CSS=None,ROBOT=True):
    a  = self.start_html()
    a += self.start_head(CSS)
    if not ROBOT:
      a += self.meta_content('robot','noindex,nofollow')
      a += self.meta_content('robots','noindex,nofollow')
      a += self.meta_content('msnbot','noindex,nofollow')
      a += self.meta_content('googlebot','noindex,nofollow')
    a += self.title(_config.SITE)
    a += self.end_head()
    a += self.start_body()
    a += self.start_center()
    a += self.h1(TITLE)
    if HELP: a += self.a(HELP,'HELP') + '  -  '
    a += self.a(_config.URL_HOME, 'HOME') + '  -  '
    a += self.a(_config.EMAIL_GEN,'CONTACT US') + "\n"
    a += self.brk()
    a += self.brk()
    a += self.end_center()
    return a

  def PageFooter(self,msg=''):
    a = ''
    if msg:
      a += self.brk()
      a += self.hr('center','100%')
      a += self.brk()
      a += self.start_center()
      a += self.start_pre()
      a += self.start_p()
      a += self.start_bold() + msg + self.end_bold()
      a += self.end_p()
      a += self.end_pre()
      a += self.end_center()
      a += self.brk()
    a += self.end_body()
    a += self.end_html()
    return a

  def PageError(self,msg=''):
    a  = self.start_center()
    a += self.start_pre()
    a += self.start_p()
    a += self.start_bold() + msg + self.end_bold()
    a += self.end_p()
    a += self.end_pre()
    a += self.end_center()
    return a
