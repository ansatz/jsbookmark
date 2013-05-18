import BaseHTTPServer
import SimpleHTTPServer
import SocketServer
from urlparse import urlparse
from urlparse import parse_qsl
from urlparse import parse_qs


#1.user-defined define class
class myGET(SimpleHTTPServer.SimpleHTTPRequestHandler):
        #2.override do_GET func
        def do_GET(self):
                self.my_do()
                SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

        def my_do(self):
                CTG = {'daily': 'ctg/daily.html',
                       'research': 'ctg/research.html',
                       'sysadmin': 'ctg/sysadmin.html',
                       'thesis': 'ctg/thesis.html' }

                #parse ;param #fragment
                #ourl = urlparse.unquote(self.requestline)
                purl = urlparse(self.requestline)
                ourl = parse_qs(self.requestline)
                print 'link',  self.path, self.requestline, purl, #ourl['link']
                #tag =  ourl.fragment # / / #daily
                #urll =  ourl.params   # /path;params    /path;params?query
                #launch remote
                if self.path == CTG['daily'] :
                        print 'no-good'
                        #return
                #write to file
                else:
                        f = open( CTG['daily'], 'a' )
                        print 'file open ', CTG['daily']
                        s = str(ourl)
                        s += s + "<br>"
                        if f: print 'file open: ', CTG['daily'], " ",ourl
                        f.write(s)
                        f.close()



#class myHndl(BaseHTTPServer.BaseHTTPRequestHandler):
#        def parse_request(self):
#                """Parse a request (internal).
#
#                The request should be stored in self.raw_requestline; the results
#                are in self.command, self.path, self.request_version and
#                self.headers.
#
#                Return True for success, False for failure; on failure, an
#                error is sent back.
#
#                """
#                self.command = None # set in case of error on the first line
#                self.request_version = version = self.default_request_version
#                self.close_connection = 1
#                requestline = str(self.raw_requestline, 'iso-8859-1')
#                requestline = requestline.rstrip('\r\n')
#                self.requestline = requestline
#                words = requestline.split()
#                if len(words) == 3:
#                        command, path, version = words
#                        if version[:5] != 'HTTP/':
#                                self.send_error(400, "Bad request version (%r)" % version)
#                                return False
#                        try:
#                                base_version_number = version.split('/', 1)[1]
#                                version_number = base_version_number.split(".")
#                                # RFC 2145 section 3.1 says there can be only one "." and
#                                # - major and minor numbers MUST be treated as
#                                # separate integers;
#                                # - HTTP/2.4 is a lower version than HTTP/2.13, which in
#                                # turn is lower than HTTP/12.3;
#                                # - Leading zeros MUST be ignored by recipients.
#                                if len(version_number) != 2:
#                                        raise ValueError
#                                version_number = int(version_number[0]), int(version_number[1])
#                        except (ValueError, IndexError):
#                                self.send_error(400, "Bad request version (%r)" % version)
#                                return False
#                        if version_number >= (1, 1) and self.protocol_version >= "HTTP/1.1":
#                                self.close_connection = 0
#                                if version_number >= (2, 0):
#                                        self.send_error(505,
#                                                        "Invalid HTTP Version (%s)" % base_version_number)
#                                        return False
#                                elif len(words) == 2:
#                                        command, path = words
#                                        self.close_connection = 1
#                                        if command != 'GET':
#                                                self.send_error(400,
#                                                                "Bad HTTP/0.9 request type (%r)" % command)
#                                                return False
#                                        elif not words:
#                                                return False
#                                        else:
#                                                self.send_error(400, "Bad request syntax (%r)" % requestline)
#                                                return False
#                                        self.command, self.path, self.request_version = command, path, version
#
#                                        # Examine the headers and look for a Connection directive.
#                                        try:
#                                                self.headers = http.client.parse_headers(self.rfile,
#                                                                                         _class=self.MessageClass)
#                                        except http.client.LineTooLong:
#                                                self.send_error(400, "Line too long")
#                                                return False
#
#                                        conntype = self.headers.get('Connection', "")
#                                        if conntype.lower() == 'close':
#                                                self.close_connection = 1
#                                        elif (conntype.lower() == 'keep-alive' and
#                                              self.protocol_version >= "HTTP/1.1"):
#                                                self.close_connection = 0
#                                                # Examine the headers and look for an Expect directive
#                                                expect = self.headers.get('Expect', "")
#                                                if (expect.lower() == "100-continue" and
#                                                    self.protocol_version >= "HTTP/1.1" and
#                                                    self.request_version >= "HTTP/1.1"):
#                                                        if not self.handle_expect_100():
#                                                                return False
#                                        HDR = {'path': self.path, 'command': self.command, 'headers': self.headers}
#                                        return HDR
#
#        def printHdr():
#                hdr = self.parse_request()
#                print 'path: ',hdr['path'],'\n','cmd: ',hdr['command'],'\n','headers: ',hdr['headers']
##def link_content( srv=SocketServer.TCPServer, hnd=BaseHTTPServer.BaseHTTPRequestHandler ):
##        hostport = ( "", 8888 )
##
##        #2.instantiate server obj
##	SERVER = srv( hostport, hnd )
##
##        #3.process-handling #cannot access class instance variables
##        print ' b', hnd.__dict__
##        #print ' bl', hnd.parse_request(path)
##        #print 'path', BaseHTTPServer.BaseHTTPRequestHandler.path(hnd)
##        print 'server ', hnd.server_version  #class variable
##        print 'client ', hnd.address_string  #instance method
##        print 'msg ', hnd.MessageClass
##        url= o.geturl()
##        frg= urlparse.urldefrag
##        print 'header: ', hdr
##        print 'url: ', url
##        print 'frg: ', frg
##        SERVER.serve_forever()
#
#
#def lnkSrv(srv=SocketServer.TCPServer,hnd=myHndl):
#        HOSTPORT=("localhost",8888)
#        SERVER = srv( HOSTPORT, hnd )
#        hnd.printHdr()
#        print "server: ", HOSTPORT
#        SERVER.serve_forever()

if __name__ == "__main__":
        #SimpleHTTPServer.test(HandlerClass=myGET)
        #Handler=SimpleHTTPServer.SimpleHTTPRequestHandler
        #Handler.do_GET=do_GET
        httpd = SocketServer.TCPServer(("", 8888), myGET)
        print 'serving myGET'
        httpd.serve_forever()
        # BaseHTTPServer.test(myHndl)





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
