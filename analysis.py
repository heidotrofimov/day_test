import os
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import math


list_of_days=[]
not_found=0
did_found=0


places=["T35VME","T35VMC"]
years=["2020"]


for place in places:
  place_days=[]
  place_not_found=0
  place_did_found=0
  for year in years:
    for directory in os.listdir(place+"_"+year+"/target_images"):
      date_str=directory.split("_")[2]
      date_obj=datetime(int(date_str[0:4]),int(date_str[4:6]),int(date_str[6:8]))
      f=open(place+"_"+year+"/target_images/"+directory,"r")
      lines=f.readlines()
      f.close()
      for target_tile in lines:
        found_date=datetime(1900,1,1)
        found=False
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
        if(found):
          between=np.abs((date_obj-found_date).days)
          list_of_days.append(between)
          place_days.append(between)
          place_did_found+=1
          did_found+=1
        else:
          not_found+=1
          place_not_found+=1
  all_days=place_did_found+place_not_found
  aver=np.mean(place_days)
  maks=np.max(place_days)
  miinn=np.min(place_days)
  nr=int(math.ceil(maks/30))
  bins=[]
  values=[]
  for j in range(nr):
    bins.append("<"+str((j+1)*30))
    nr_of_days=0
    for val in place_days:
      if(val>=j*30 and val<(j+1)*30):
        nr_of_days+=1
    values.append((nr_of_days/all_days)*100)
  bins.append("∞")
  values.append((place_not_found/all_days)*100)
  plt.bar(bins,values)
  plt.title(place+"_"+year+"\nAverage time distance: "+str(aver))
  plt.xlabel("Days between target tile and last clear tile in past")
  plt.ylabel("% of all target tiles")
  plt.savefig("results/"+place+"_"+year+".png")
  plt.close()
  
  
        

