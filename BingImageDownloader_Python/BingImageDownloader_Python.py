from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import  urllib.request

def DownloadImage(urlForImage, FileName):
    print('Downloading image from ' + urlForImage)
    FileName = FileName+'.jpg'
    try:
        urllib.request.urlretrieve(urlForImage,FileName)
        print("Image from "+ urlForImage + " has been downloaded")
    except:
        print('Failed to download image from ' + urlForImage)

def Craw(RootUrl):
    try:
        print('Analyzing url.')
        req = Request(RootUrl)
        webpage = urlopen(req).read()
        #print(len(webpage))
        soup = BeautifulSoup(webpage,"html.parser")
        ImageList = set()
        for SthMayContainImage in soup.find_all('a',{'class':'thumb'}):
            ImageLink = SthMayContainImage.get('href')
            ImageList.add(ImageLink)
        return  ImageList
    except:
        print('Failed to analyze input url.')

SourceUrl = "https://www.bing.com/images/search?q=cat&qs=n&form=QBLH&scope=images&pq=cat&sc=8-3&sp=-1&sk=&cvid=A9357866FFFF458C890B6A339BBDA5CC"
ImageName="Default"
SourceUrl = input("Paste a url from bing image search result: \n")
ImageName = input("Type the image class for files naming: \n")

ImageList = Craw(SourceUrl)

Count =0
for ImageLink in ImageList :
        DownloadImage(ImageLink,ImageName+ " " + str(Count))
        Count+=1

print('Done.')
print('A_____A')
