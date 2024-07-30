#!/usr/bin/env python

import sys
import glob
import re 
import order

#sys.path.append("D:/src/venv/lib/site-packages")

# for p in sys.path:
#     print(p)

data = []
oneRecord = {}


try:
    import bs4
except:
    sys.stderr.writelines("Unable to load BeautifulSoup4 module")
    
# print(dir(bs4))
bfsoup4 = bs4.BeautifulSoup()

_tags = [ 
        "Full Name:",
        "Email Address:", 
        "Mobile Number:",
        "Pin/Postal/Zip Code:",
        "Flat, House no., Building, Company, Apartment:",
        "Landmark e.g. near apollo hospital:",
        "Town/City:",
        "State:",
        "Country:",
        "How many copies and indicate which language:",
        ]

_NAME_INDEX = 0
_EMAIL_INDEX = 1
_MOBILE_INDEX = 2
_PIN_INDEX = 3
_APARTMENT_INDEX = 4
_LANDMARK_INDEX = 5
_TOWN_INDEX = 6
_STATE_INDEX = 7
_COUNTRY_INDEX = 8
_QTY_INDEX = 9

def lookupTag(toLookupTag, allTags):
    print("lookupTag")
    print("lookupTag(%s, %s)" % (toLookupTag, allTags))
    found = False
    count = -1
    for t in allTags:
        if toLookupTag.find(t) != -1:
            print(t + " found : " + toLookupTag)
            count += 1
            found = True
        else:
            if found == False:
                count += 1
    return count
    
def buildObject(indx, value, obj):
    if indx == _NAME_INDEX:
        obj.set_first_name(value)
    if indx ==  _MOBILE_INDEX:
        obj.set_mobile_number(value)
    ss = obj.show()
    print(ss)
        
def parse(inName, outName, obj):
    print("Parse : %s %s" % (inName, outName))
    # return
    html = ''
    # print(sys.argv)
    try:
        allLines = open(inName)
        print("Processing : %s" % inName)
        allLines = open(inName, 'rt').readlines()
        # print(len(allLines))
        startHtml = False
        for l in allLines:
            if startHtml == False:
                if l.startswith("<!doctype"):
                    startHtml = True
                    html += l
                    # print("*START* : "+l)
            else:
                html += l
        # print(len(html))        
        fw = open(outName+".html", 'wt')
        fw.write(html)
        fw.close()
        soup = bs4.BeautifulSoup(html, 'html.parser')
        v = soup.get_text()
        
        # print(v)
        
        lines = v.split("\n")
        fw = open(outName + ".txt", "wt")
        # print(len(lines))
        for l in lines:
            if len(l) > 0:
                if l.find('DHARMYOG') == -1:
                    print("%s" % l, end=" ")
                    if l in _tags:
                        tagFound = lookupTag(l, _tags)
                        if tagFound != -1:
                            print("Found in tags %d " % tagFound)
                            buildObject(tagFound, l, obj)
                    else:
                        print(" ")
                    fw.write(l + "\n")
        fw.close()
    except:
        print(sys.exc_info())


if __name__ == "__main__":
    print(sys.argv)
    ipName = sys.argv[1]
    fList = []
    exp = re.compile('[A-Za-z]* Form_([0-9]+).eml')
    if ipName.find('*') > 1:
        print("Contains wildcard")
        fList = glob.glob(ipName)
        print(fList)
    else:
        fList.append(ipName)
    for f in fList:
        r1 = exp.search(f)        
        outName = "../Emlfiles/" + r1.groups()[0]
        print(f, outName)
        oneOrder = order.Order()
        parse(f, outName, oneOrder)
    # addOne(order)

