from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import re
import wget

# root = "http://3d.hel.ninja/data/citygml/Helsinki3D_CityGML_BUILDINGS_LOD2_NOTEXTURES_ZIP/"
# root = "https://www.businesslocationcenter.de/en/economic-atlas/download-portal/"
# root = "http://donnees.ville.montreal.qc.ca/dataset/maquette-numerique-batiments-citygml-lod2-avec-textures"
root = "https://download.data.grandlyon.com/files/grandlyon/localisation/bati3d/"
# dest = "/media/yuqiong/DATA/city/berlin/"
# dest = "/data/city/montreal/"
dest = "/data/city/lyon/"

html_page = urllib.request.urlopen(root)
soup = BeautifulSoup(html_page, features="lxml")
for link in soup.findAll('a'):
    href = link.get('href')
    if href and href.split(".")[-1] == "zip":
        download = href
        if download[0] != "_" and download[-8:] == "2015.zip":
            url = root + download
            print(url)
            wget.download(url, dest)
