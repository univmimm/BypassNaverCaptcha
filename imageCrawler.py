# Made by universe
# This script is crawling images on my server.
# modified 2019-08-03

import requests         # To send a request to the project server.
import urllib           # To get images data.
from bs4 import BeautifulSoup   # To get a image links and answer.
import os      # To rename downloaded images name and create a folder.


print("[*] Crawling start.")

savePath = '/var/www/project/crawler'
imageCount = 0

for folderName in range(0,1001):   # This is folder count
    try:
        os.makedirs(savePath+"/"+str(folderName))
    except Exception:
        print('[!] Directory already exists')
        continue
    
    for getImageCount in range(1,101):  # This is image count.
        # Send a request to the project server and parse the response's body section.
        res = requests.get('http://project.univ-blog.xyz')
        body = BeautifulSoup(res.text, 'html.parser')
        
        # Get a image link.
        imageURL = body.find('img', {'id' : 'captcha_image'}).get('src')
        
        # Download a image using above image link. Save a image with a temporary name.
        urllib.urlretrieve('http://project.univ-blog.xyz'+imageURL, savePath+'/'+str(folderName)+'/0.jpg')
        
        # Send a request for getting answer to the project server.
        # And save a result into 'imageAnswer' variable.
        imageAnswer = requests.get('http://project.univ-blog.xyz/getCode.php').text
        
        # Rename the downloaded image's temporary name to the answer.
        os.rename( savePath+'/'+str(folderName)+'/0.jpg',  savePath+'/'+str(folderName)+'/'+imageAnswer+'.jpg')
        imageCount += 1
        print("[*] "+str(imageCount)+" Success save image. "+imageAnswer+".jpg")
    
