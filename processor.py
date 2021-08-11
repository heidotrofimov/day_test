import os
import time

f=open("login.txt","r")
lines=f.readlines()
username=lines[0].rstrip()
password=lines[1].rstrip()

print(username)
print(password)

def download_xml(product, out_path):
    user_name = username
    user_password = password
    scihub_url = "https://scihub.copernicus.eu/dhus/search?q="
    command = "wget --no-verbose --no-check-certificate --user={user} --password={pwd} --output-document={out}"\
                  " {url}".format(user=user_name, pwd=user_password, out=out_path, url=(scihub_url + product))

    print("Downloading product as " + command)
    time.sleep(1.5)  # scihub does not allow too frequent queries; therefore wait a bit before a new query
        
download_xml("S2*MSIL2A*202006*T35VMC*","/home/heido/proov.xml")
