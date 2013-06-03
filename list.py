from HTMLParser import HTMLParser
import urllib2
import os


# schoena, dresden, meissen
allowed_ids = ['501060', '501010', '501080']

basepath = 'http://www.umwelt.sachsen.de/de/wu/umwelt/lfug/lfug-internet/hwz'

class LocationParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # location id in list
        if tag == "a" and attrs[0][1].find('MP/') == 0:
            href = attrs[0][1]
            location_id = href[href.find('MP/')+3:href.rfind('/')]
            subpath = href[:href.rfind('/')]
            
            if location_id not in allowed_ids:
                return
            try:
                os.stat(location_id)
            except:
                os.mkdir(location_id)
            # get the files
            files = {'/index.html', '/durchfluss.png', '/wasserstand.png'}
            for f in files:
                try:
                    print "Trying to get " + basepath + '/' + subpath + f
                    response = urllib2.urlopen(basepath + '/' + subpath + f)
                except urllib2.HTTPError as e:
                    pass
                else:
                    content = response.read()
                    newfile = open(location_id + f, "w")
                    newfile.write(content)

    def handle_endtag(self, tag):
        pass
    def handle_data(self, data):
        pass

def main():
    parser = LocationParser()
    try:
        response = urllib2.urlopen(basepath + '/inhalt_re.html')
        html = response.read()
    except urllib2.URLError as e:
        print e
    except urllib2.HTTPError as e:
        print e
        # try again later...
    else:
       parser.feed(html)
if __name__ == '__main__': main()
