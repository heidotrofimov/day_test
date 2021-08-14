import os
from datetime import datetime, timedelta
import numpy as np

list_of_days=[]
not_found=0

for directory in os.listdir("target_images"):
  date_str=directory.split("_")[2]
  date_obj=datetime(int(date_str[0:4]),int(date_str[4:6]),int(date_str[6:8]))
  for target_tile in os.listdir("target_images/"+directory):
    found_date=datetime(1900,1,1)
    found=False
    for directory2 in os.listdir("clear_images"):
      date_str2=directory2.split("_")[2]
      date_obj2=datetime(int(date_str2[0:4]),int(date_str2[4:6]),int(date_str2[6:8]))
      if(date_obj>date_obj2):
        for clear_tile in os.listdir("clear_images/"+directory2):
          if(clear_tile==target_tile):
            found=True
            if(date_obj2>found_date):
              found_date=date_obj2
      if(found):
        print(directory+target_tile+" with "+directory2+clear_tile)
        between=np.abs((date_obj-date_obj2).days)
        list_of_days.append(between)
      else:
        not_found+=1
        
        
print(list_of_days)                       
print(not_found)
