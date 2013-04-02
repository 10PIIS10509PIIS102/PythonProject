import re, urllib
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        #print "data called"
        if data!=" ":
            textfile1 = open('text.txt','a')
            textfile1.write(data)
            textfile1.close()
            return
class formatter():  
    def format(self):
        f= open('text.txt','r')
        w=open('format.txt','a')
        for line in f:
                newline = line.replace(' ', '')
                w.write(newline)
        f.close()
        w.close()
        return
    def write(self,myurl):
        #print "write called"
        textfile1 = open('text.txt','a')
        textfile1.write(myurl)
        textfile1.close()
        parser = MyHTMLParser()
        print myurl
        parser.feed(urllib.urlopen(myurl).read())
        return

s=formatter()
f=open("links2.txt","r")
for i in f.readlines():  
    myurl=i
    s.write(myurl)
subeen=formatter()
subeen.format()
