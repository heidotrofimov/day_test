import os
import time
from pathlib import Path

f=open("login.txt","r")
lines=f.readlines()
username=lines[0].rstrip()
password=lines[1].rstrip()
f.close()

print(username)
print(password)

def download_xml(product, out_path):
    user_name = username
    user_password = password
    scihub_url = "https://scihub.copernicus.eu/dhus/search?q="
    command = "wget --no-verbose --no-check-certificate --user={user} --password={pwd} --output-document={out}"\
                  " {url}".format(user=user_name, pwd=user_password, out=out_path, url="\""+scihub_url + product+"&rows=100\"")

    print("Downloading product as " + command)
    os.system(command)
    time.sleep(1.5)  # scihub does not allow too frequent queries; therefore wait a bit before a new query
    
def read_xml(out_path):
    product_list=[]
    txt = Path(out_path).read_text()
    products=txt.split("<title>")
    for i in range(1,len(products)):
        product=products[i].split("</title>")
        product_list.append(product)
    print(len(product_list))
    print(product_list)
        
download_xml("S2*MSIL2A*202006*T35VMC*","proov.xml")
read_xml("proov.xml")
