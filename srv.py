#headers.items()
#import sys, urllib as ul; print ul.unquote_plus(sys.argv[1])
#he list of client values contains the encoded query arguments
#file = urllib.urlopen
#file.read ... will just decode ?
#urlparse(encodedString)


#SocketServer.TCPServer,
#hnd = SimpleHTTPServer.SimpleHTTPRequestHandler

# f=C.x;print f() == x(f)

#INSTANCE objs only understand attr.refernces variables methods x.f()
#method object, can be stored and called later
#xf = x.f
#print xf()

#CLASS variables methods
#function object MyClass.f
#here x.f equivalent to MyClass.f(x)

import BaseHTTPServer
import SimpleHTTPServer
import SocketServer
import urllib

#1.user-defined define class
def link_content( srv=SocketServer.TCPServer, hnd=BaseHTTPServer.BaseHTTPRequestHandler ):
        hostport = ( "", 8888 )
        #2.instantiate server obj
	SERVER = srv( hostport, hnd )
        #3.process-handling
        #hnd.headers =
        #SERVER.headers
        print 'server ', hnd.server_version
        print 'client ', hnd.address_string
        print 'msg ', hnd.MessageClass
        #print BaseHTTPServer.BaseHTTPRequestHandler.handle(hnd)
        print BaseHTTPServer.BaseHTTPRequestHandler.headers(hnd)
        print SERVER.header
        o= urlparse(hdr)
        url= o.geturl()
        frg= urlparse.urldefrag
        print 'header: ', hdr
        print 'url: ', url
        print 'frg: ', frg
        SERVER.serve_forever()

#if __name__ == "__main__":
link_content()









#response = urllib.urlopen('http://localhost:8888/')
#for line in response:
#	    print line.rstrip()

#print response.path

# minimal web server.  serves files relative to the
# current directory.

#PORT = 8888

#Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

#httpd = SocketServer.TCPServer(("", PORT), Handler)

#print "serving at port", PORT
#httpd.serve_forever()
