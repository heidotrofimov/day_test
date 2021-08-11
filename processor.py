import os
import time
from pathlib import Path

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
    current_list=[]
    txt = Path(out_path).read_text()
    products=txt.split("<title>")
    for i in range(2,len(products)):
        product=products[i].split("</title>")[0]
        product_list.append(product)
    return current_list

f=open("login.txt","r")
lines=f.readlines()
username=lines[0].rstrip()
password=lines[1].rstrip()
f.close()

print(username)
print(password)

year="2020"
place="T35VMC"
months=["11","10","09","08","07","06","05","04"]
active_months=["11","10","09","08","07"]
passive_months=["06","05","04"]

product_list=[]

for month in months:
    download_xml("S2*MSIL2A*"+year+"*"+place+"*",month+".xml")
    month_list=read_xml(month+".xml")
    for product in month_list:
        product_list.append(product)

print(product_list)
