#!/usr/bin/env python

import sys
import glob
import re 
import logging
import logging.config
import bo

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
    # print("lookupTag(%s)" % toLookupTag)
    found = False
    count = -1
    for t in allTags:
        if toLookupTag.find(t) != -1:
            # print(t + " found : " + toLookupTag)
            count += 1
            found = True
        else:
            if found == False:
                count += 1
    return count
    
def buildObject(block, obj):
    print("Block: %s" % str(block))
    print(len(block))
    indx = 0
    while indx < len(block):
        tag = lookupTag(block[indx], _tags)
        if tag != -1:
            obj[tag] = block[indx+1]
        indx += 2
    print("OBJ : %s" % str(obj))
    order = bo.Bookorders()
    for k in obj.keys():
        # print("%d %s" % (k, obj[k]))
        if k == _NAME_INDEX:
            order.first_name = obj[k]
            # print("Name:"+obj[k])
        if k == _EMAIL_INDEX:
            order.email = obj[k]
            # print("Email:"+obj[k])
        if k == _MOBILE_INDEX:
            order.mobile_number = obj[k]
            # print("Mobile Number:"+obj[k])
        if k == _PIN_INDEX:
            order.pin_postal_zip_code = obj[k]
            # print("Pin:"+obj[k])
        if k == _APARTMENT_INDEX:
            order.flat_house_building = obj[k]
            # print("Flat:"+obj[k])
        if k == _LANDMARK_INDEX:
            order.landmark = obj[k]
            # print("Landmark:"+obj[k])
        if k == _TOWN_INDEX:
            order.town_city = obj[k]
            # print("Town:"+obj[k])
        if k == _STATE_INDEX:
            order.state_prov = obj[k]
            # print("State:"+obj[k])
        if k == _COUNTRY_INDEX:
            order.country = obj[k]
            # print("Country:"+obj[k])
        if k == _QTY_INDEX:
            order.language = obj[k]
            # print("Qty:"+obj[k])
    # ss = order.show()
    print("Name: %s" % order.first_name)
    print("Email: %s" % order.email)
    print("Mobile: %s" % order.mobile_number)
    order.save()
        
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
        outBlock = []
        for l in lines:
            if len(l) > 0:
                if l.find('DHARMYOG') == -1:
                    # print("%s" % l)
                    outBlock.append(l)
        # print("%d : %s" % (len(outBlock), str(outBlock)))
        buildObject(outBlock, oneRecord)
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
        outName = "./Emlfiles/" + r1.groups()[0]
        print(f, outName)
        oneOrder = bo.Bookorders()
        parse(f, outName, oneOrder)
    # addOne(order)
