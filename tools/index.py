
import re
import os
import json
import requests
from datetime import datetime
import xml.etree.ElementTree as ET



def datecvt(date_str):
    # 2024-03-02T17:06:43-05:00
    datetimeFmt = "%Y-%m-%dT%H:%M:%S%z"
    # ymd = re.findall(r'\d{4}-\d{2}-\d{2}', date_str)
    # datetime_object = datetime.strptime(ymd[0], "%Y-%m-%d").date()
    datetime_object = datetime.strptime(date_str, datetimeFmt)
    # print(datetime_object)
    return datetime_object

# curl -i POST \
#   -H "Content-Type: application/json; charset=utf-8" \
#   -d '{
#     "host": "example.com", 
#     "key":"ffb3f16ace204c8eb58efc30b2e2674d", 
#     "keyLocation": "https://example.com/indexnow-key.txt",
#     "urlList": [
#       "https://example.com/url1",
#       "https://example.com/url2"
# ]}' \
# https://www.bing.com/indexnow

def buildObj(urls):
    indexKey = os.getenv('INDEXNOW')
    data = { 
        "host": "solve.bhmystery.com",
        "key": indexKey,
        "keyLocation": "https://solve.bhmystery.com/{0}.txt".format(indexKey),
        "urlList":urls
        }
    y = json.dumps(data)
    print(y)
    return y


def callIndexNow(data):
    headers={"Content-type":"application/json", "charset":"utf-8"}
    url = 'https://bing.com/indexnow'
    response = requests.post(url, headers=headers, data=data)
    print(response.status_code)
    print(response.text)
    print(response)


def getUrls():
    ns = {'schema': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

    # tree = ET.parse('../content/sitemap.xml')
    tree = ET.parse('../public/sitemap.xml')
    root = tree.getroot()


    r = requests.get('https://solve.bhmystery.com/sitemap.xml')
    extRoot = ET.fromstring(r.text)
    update = []
    # Find urls currently in sitemap
    # Find urls not currently in sitemap
    # Find urls no longer in sitemap?? This would be there's a url in extURL and not locally <- so should it be removed?
    for url in root.findall('schema:url', ns):
        loc = url.find('schema:loc',ns)
        lastmod = url.find('schema:lastmod',ns)
        lastmodObj = datecvt(lastmod.text)
        found = False
        for extURL in extRoot.findall('schema:url', ns):
            extLoc = extURL.find('schema:loc',ns)
            
            # Find urls currently in sitemap
            if (extLoc.text == loc.text and found == False):
                found = True
                extLastmod = extURL.find('schema:lastmod',ns)
                extLastmodObj = datecvt(extLastmod.text)
                #compare dates last changed
                # if (lastmodObj > extLastmodObj) this is true - then we need to slate this url for an index update.
                if (lastmodObj > extLastmodObj):
                    update.append(loc.text)
                print("Location: {0}\n\tLastMod Local:\t{1}\n\tLastMod Remote:\t{2}\n\tLocal Newer:\t{3}\n".format(loc.text,lastmodObj,extLastmodObj, lastmodObj > extLastmodObj))
        
        # Find urls not currently in sitemap
        if (found == False):
            print("Location Not in Remote: {0}\n\tLastMod Local:\t{1}\n".format(loc.text,lastmodObj))
            update.append(loc.text)
    # print(update)
    data = buildObj(update)
    # callIndexNow(data)
    # print(data)


if __name__ == '__main__':
    getUrls()