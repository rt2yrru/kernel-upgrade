from HTMLParser import HTMLParser
import urllib
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag

    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag

    def handle_data(self, data):
        print "Encountered some data  :", data

# instantiate the parser and fed it some HTML
f = urllib.urlopen("http://kernel.ubuntu.com/~kernel-ppa/mainline")
s = f.read()
parser = MyHTMLParser()
parser.feed(s)
