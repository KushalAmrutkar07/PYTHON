import requests
import re
from urllib.parse import urlparse
from sys import *
import os

def is_downloadable(url):
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True

def get_filename_from_cd(cd):
    a = urlparse(cd)
    return os.path.basename(a.path)

def MarvellousDownload(url):
    allowed = is_downloadable(url)
    
    if allowed:
        try:
            res = requests.get(url, allow_redirects=True)
            res.raise_for_status()
            filename = get_filename_from_cd(url)
            fd = open(filename,"wb") # write binary

            for buffer in res.iter_content(1024):
                fd.write(buffer)

            fd.close()
            return True
        except Exception as E:
            return False
    else:
        return False                
  

def main():
    print("---- Marvellous Infosystems by Piyush Khairnar-----")

    print("Application name : " +argv[0])


    if (len(argv) == 2):
        if (argv[1] == "-h") or (argv[1] == "-H"):
            print("This Script is used to Download file")
            exit()

        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("usage : ApplicationName AbsolutePath_of_Directory Extension")
            exit()

    url = 'https://img.freepik.com/premium-photo/astronaut-outer-open-space-planet-earth-stars-provide-background-erforming-space-planet-earth-sunrise-sunset-our-home-iss-elements-this-image-furnished-by-nasa_150455-16829.jpg?w=2000'

    results = MarvellousDownload(url)
        
    if results:
        print("File successfully Downloaded")
    else:
        print("Failed to download....")    

if __name__ == "__main__":
    main()
