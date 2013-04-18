from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import cgi,CGIHTTPServer
from SocketServer import ThreadingMixIn
import threading
import urllib2

PORT_NUMBER = 8050

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
		type= form.getvalue('Type')
		state= form.getvalue('State')
		budget= form.getvalue('Budget')
		print type,state,budget
		self.wfile.write(df%(form))
		
	def do_GET(self):
		f = open('log.txt','a')
		f.write(str(self.command)+' command from (ip,port)='+str(self.client_address)+'\n')
		f.close()		
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		form='''<html>
<head>
<script>
function budget(id)
{
bud=document.getElementById("bu")
if(id==3||id==4) {
bud.style.display="block";
} 
else {
bud.style.display="none";
} }
</script>
</head>
<body>
<h1>Query</h1>
<hr><hr>
<h3>Type of Tourist Place:</h3>

<form action="" method=post>
<select size=1 name="Type">
<option value="none">Select the type of place</option>
<option id=1  value="Beach" onclick=budget(id)>Beach</option>
<option id=2  value="Hill Station" onclick=budget(id)>Hill Station</option>
<option id=3  value="Hotel" onclick=budget(id)>Hotel</option>
<option id=4  value="Beach Resort" onclick=budget(id)>Beach Resort</option>
</select>
<div id=bu style="display:none"><h3>Enter your Budget:</h3>
<input type=text name="Budget" value="none"/></div>
<h3>Enter State:</h3>
<input type=text name="State" value="none"/><br /><br />
<input type=submit value=Search /><input type=reset />
</form>
</body></html>'''
		
		self.wfile.write((form))
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	"""Handle requests in a separate thread."""
try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = ThreadedHTTPServer(('', PORT_NUMBER), myHandler)
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
