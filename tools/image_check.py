import os
import re
from urllib.parse import urlparse
from urllib.request import urlopen
from urllib.error import *
import json 

def uri_validator(x):
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc])
    except AttributeError:
        return False

def url_reachable(url,results):
    # try block to read URL
    try:
        html = urlopen(url)
    
    except HTTPError as e:
        print(f"{e}:\t{url}")
        results["httpError"].append(url)
        
    except URLError as e:
        print(f"{e}:\t{url}")
        results["urlError"].append(url)

    except:
        print(f"Something else happened:\t{url}")
        results["otherError"].append(url)
    else:
        results["passed"].append(url)
    

def scrape_file(file,urls):
    pattern = re.compile(r"<meta property=\"og:image\" content=\"(http://localhost:1313/images/+[a-zA-Z]{2,6}(?:\/[^\s]*)*\.(?:jpg|jpeg|png|gif|bmp|webp|svg))\">")
    result = pattern.findall(file.read())

    for match in result:
        urls.append(match)


def read_files_by_extension(directory, extension):
    """Recursively reads all files with a given extension in a directory."""

    urls = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                with open(os.path.join(root, file), 'r',  encoding="utf8") as f:
                    scrape_file(f,urls)
    urls = list(set(urls))
    print(f"------------------------\nChecking {len(urls)} urls...\n------------------------")

    results = dict(httpError = [], urlError = [], otherError = [], passed = [])
    for url in urls:
        # print(uri_validator(url))
        url_reachable(url,results)
    # Convert and write JSON object to file
    with open("image_url_results.json", "w") as outfile: 
        json.dump(results, outfile)

# Example usage
read_files_by_extension(".\public\/", ".html")