from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import cgi,CGIHTTPServer

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class myHandler(SimpleHTTPRequestHandler):
	#Handler for the GET requests
	#print HTTPServer.request
	def do_POST(self):
		f = open('log.txt','a')
		f.write(str(self.command)+' command from (ip,port)='+str(self.client_address)+'\n')
		f.close()
		self.send_response(200)
		#send header first
		self.send_header('Content-type','text-html')
		self.end_headers()
		df='''
			<html>
			<head>
			<title>cgi input</title>
			</head>
			<body>
			<h2>the keys are </h2> %s
			</body>
			</html>'''
	# Create instance of FieldStorage 
		form = cgi.FieldStorage(fp=self.rfile, headers=self.headers,
									environ = {'REQUEST_METHOD':'POST'},
									keep_blank_values = 1) 

	# Get data from fields
		first_name = form.getvalue('place')
		self.wfile.write(df%(form))
		
	def do_GET(self):
		f = open('log.txt','a')
		f.write(str(self.command)+' command from (ip,port)='+str(self.client_address)+'\n')
		f.close()		
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		form=''' <html>
					<head>
					<script type=text/javascript>
					function init()
					{
					var dis=document.getElementsByTagName("input");
					for(i=0;i<dis.length-1;i++)
					dis[i].style.display="none";
					}
					function deinit(id)
					{
					if(id==4 || id==7 || id==8 || id==9)
					{
					for(i=1;i<=5;i++)
					{
					var dis=document.getElementById(id+i.toString());
					dis.style.display="block";
					}
					}
					else
					{
					var dis=document.getElementById(id);
					dis.style.display="block";
					}
					}
					</script>
					</head>
					<body bgcolor=green onload=init()>
					<div style="font:24px monotype corsiva">
					<b><u>Enter the search criteria:</u></b><br /><br />
					<form action="" method=post>
					<b><label onclick=deinit(1)>Name of the place:</label></b>&nbsp;<input type=text name="place" id=1 value="None"/><br /><br />
					<b><label onclick=deinit(2)>Type of the place:</label></b>&nbsp;<input type=text name="typeplace" id=2 value="None"/><br /><br />
					<b><label onclick=deinit(3)>Type of the hotel:</label></b>&nbsp;<input type=text name="typehotel" id=3 value="None"/><br /><br />
					<b><label onclick=deinit(4)>Budget of the hotel::</label></b><br />
					<div style="margin-left:50px">
					Budget Range:&nbsp;lower&nbsp;<input id=41 type=text name="lowerbudget" value="None" />&nbsp;upper&nbsp;<input id=43 type=text name="upperbudget" value="None" /><br />
					Budget greater than:&nbsp;<input id=44 type=text name="budgetgt" value="None" /><br />
					Budget lesser than:&nbsp;<input id=45 type=text name="budgetlt" value="None" /><br /><br />
					</div>
					<b><label onclick=deinit(5)>Weather of the place:</label></b>&nbsp;<input id=5 type=text name="weather" value="None" /><br /><br />
					<b><label onclick=deinit(6)>Name of the hotel:</label></b>&nbsp;<input id=6 type=text name="hotel" value="None" /><br /><br />
					<b><label onclick=deinit(7)>Distance(Both Car & Flight)::</label></b><br />
					<div style="margin-left:50px">
					Distance Range:&nbsp;lower&nbsp;<input id=71 type=text name="lowerdistance" value="None"/>&nbsp;upper&nbsp;<input id=73 type=text name="higherdistance" value="None" /><br />
					Distance greater than:&nbsp;<input id=74 type=text name="distancegt" value="None" /><br />
					Distance lesser than:&nbsp;<input id=75 type=text name="distancelt" value="None" /><br /><br />
					</div>
					<b><label onclick=deinit(8)>Distance(Flight)::</label></b><br />
					<div style="margin-left:50px">
					Distance Range:&nbsp;lower&nbsp;<input id=81 type=text name=flowerdistance value="None"/>&nbsp;upper&nbsp;<input id=83 type=text name=fupperdistance value="None" /><br />
					Distance greater than:&nbsp;<input id=84 type=text name=fdistancegt value="None" /><br />
					Distance lesser than:&nbsp;<input id=85 type=text name=fdistancelt value="None" /><br /><br />
					</div>
					<b><label onclick=deinit(9)>Distance(car)::</label></b><br />
					<div style="margin-left:50px">
					Distance Range:&nbsp;lower&nbsp;<input id=91 type=text name=clowerdistance value="None"/>&nbsp;upper&nbsp;<input id=93 type=text name=cupperdistance value="None" /><br />
					Distance greater than:&nbsp;<input id=94 type=text name=cdistancegt value=None /><br />
					Distance lesser than:&nbsp;<input id=95 type=text name=cdistancelt value=None /><br /><br />
					</div>
					<b><label onclick=deinit(10)>No of days:</label></b>&nbsp;<input id=10 type=text name=days value="None" /><br /><br />
					<b><label onclick=deinit(11)>City:</label></b>&nbsp;<input id=11 type=text name=city value="None" /><br /><br />
					<b><label onclick=deinit(12)>State:</label></b>&nbsp;<input id=12 type=text name=state value="None" /><br /><br />
					<b><label onclick=deinit(13)>Name of the Month:</label></b>&nbsp;<input id=13 type=text name=month value="None" /><br />
					<br /><center><input type=submit name=submit value=Search style="width:200px"/></center><br />
					</form></div>
					</body></html> '''
		self.wfile.write(form)
		return

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	f = open('log.txt','a')
	f.write('Started httpserver on port'+str(PORT_NUMBER)+'\n')
	f.close()
	
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	f = open('log.txt','a')
	f.write('^C received, shutting down the web server'+'\n')
	f.close()
	server.socket.close()
