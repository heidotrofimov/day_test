import os
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt

list_of_days=[]
not_found=0
did_found=0


place="T35VME"
year="2020"

for directory in os.listdir(place+"_"+year+"/target_images"):
  date_str=directory.split("_")[2]
  date_obj=datetime(int(date_str[0:4]),int(date_str[4:6]),int(date_str[6:8]))
  f=open(place+"_"+year+"/target_images/"+directory,"r")
  lines=f.readlines()
  f.close()
  for target_tile in lines:
    found_date=datetime(1900,1,1)
    found=False
    found_clear=""
    for directory2 in os.listdir(place+"_"+year+"/clear_images"):
      date_str2=directory2.split("_")[2]
      date_obj2=datetime(int(date_str2[0:4]),int(date_str2[4:6]),int(date_str2[6:8]))
      if(date_obj>date_obj2):
        f=open(place+"_"+year+"/clear_images/"+directory2,"r")
        lines2=f.readlines()
        f.close()
        for clear_tile in lines2:
          if(clear_tile==target_tile):
            found=True
            if(date_obj2>found_date):
              found_date=date_obj2
              found_clear=directory2+"/"+clear_tile
    if(found):
      print(directory+"/"+target_tile+" with "+found_clear)
      between=np.abs((date_obj-found_date).days)
      list_of_days.append(between)
      did_found+=1
    else:
      not_found+=1

        
print(not_found)
print(did_found)
print(np.min(list_of_days))
print(np.max(list_of_days))
print(np.mean(list_of_days))

largest_between=np.max(list_of_days)
for j in range(not_found):
  list_of_days.append(largest_between+35)

print(np.max(list_of_days))
bins=np.arange(np.min(list_of_days),np.max(list_of_days),30)
n, bins, patches = plt.hist(list_of_days, bins,histtype=u'step',facecolor='g')
plt.savefig("T35VMC_2020.png")
