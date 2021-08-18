import os
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import math


list_of_days=[]
not_found=0
did_found=0


places=["T35VME","T35VMC","T34UED"]
years=["2020"]

#Asukohad eraldi, aastad kokku

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
  plt.title(place+"\nAverage time distance: "+str(aver))
  plt.xlabel("Days between target tile and last clear tile in past")
  plt.ylabel("% of all target tiles")
  plt.savefig("results/"+place+"_allyears.png")
  plt.close()
  
#Aastad eraldi, asukohad kokku:
#Kuud eraldi, aastad ja asukohad kokku

months_days=[]
months_not_found=[]
months_did_found=[]

for k in range(5):
  temp=[]
  months_days.append(temp)
  months_not_found.append(0)
  months_did_found.append(0)

for year in years:
  place_days=[]
  place_not_found=0
  place_did_found=0
  
  
  for place in places:
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
          place_days.append(between)
          place_did_found+=1
          if(date_str[4:6]=="11"):
            months_days[0].append(between)
            months_did_found[0]+=1
          if(date_str[4:6]=="10"):
            months_days[1].append(between)
            months_did_found[1]+=1
          if(date_str[4:6]=="09"):
            months_days[2].append(between)
            months_did_found[2]+=1
          if(date_str[4:6]=="08"):
            months_days[3].append(between)
            months_did_found[3]+=1
          if(date_str[4:6]=="07"):
            months_days[4].append(between)
            months_did_found[4]+=1
          
        else:
          place_not_found+=1
          if(date_str[4:6]=="11"):
            months_not_found[0]+=1
          if(date_str[4:6]=="10"):
            months_not_found[1]+=1
          if(date_str[4:6]=="09"):
            months_not_found[2]+=1
          if(date_str[4:6]=="08"):
            months_not_found[3]+=1
          if(date_str[4:6]=="07"):
            months_not_found[4]+=1
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
  plt.title(year+"\nAverage time distance: "+str(aver))
  plt.xlabel("Days between target tile and last clear tile in past")
  plt.ylabel("% of all target tiles")
  plt.savefig("results/"+year+"_allplaces.png")
  plt.close()

  
#Kõik kokku:

all_days=did_found+not_found
aver=np.mean(list_of_days)
maks=np.max(list_of_days)
miinn=np.min(list_of_days)
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
values.append((not_found/all_days)*100)

fig, (ax1, ax2) = plt.subplots(1, 2)

bins2=[]
values2=[]
for j in range(len(bins)-1):
  bins2.append(bins[j])
  if(j==0):
    values2.append(values[j])
  else:
    values2.append(values2[j-1]+values[j])

ax1.bar(bins,values)
ax1.title("All data\nAverage time distance: "+str(aver))
ax1.xlabel("Days between target tile and last clear tile in past")
ax1.ylabel("% of all target tiles")
ax1.savefig("results/alldata.png")
ax1.grid()

ax2.plot(bins2,values2, ls='steps', linewidth=4.0)
ax2.title("All data\nAverage time distance: "+str(aver))
ax2.xlabel("Days between target tile and last clear tile in past")
ax2.ylabel("% of all target tiles")
ax2.savefig("results/alldata_acc.png")
plt.close()

#Kuude lõikes:

names=["November","October","September","August","July"]
for i in range(5):
  name=names[i]
  all_days=months_did_found[i]+months_not_found[i]
  aver=np.mean(months_days[i])
  maks=np.max(months_days[i])
  miinn=np.min(months_days[i])
  nr=int(math.ceil(maks/30))
  bins=[]
  values=[]
  for j in range(nr):
    bins.append("<"+str((j+1)*30))
    nr_of_days=0
    for val in months_days[i]:
      if(val>=j*30 and val<(j+1)*30):
        nr_of_days+=1
    values.append((nr_of_days/all_days)*100)
  bins.append("∞")
  values.append((months_not_found[i]/all_days)*100)
  plt.bar(bins,values)
  plt.title(name+"\nAverage time distance: "+str(aver))
  plt.xlabel("Days between target tile and last clear tile in past")
  plt.ylabel("% of all target tiles")
  plt.savefig("results/"+name+".png")
  plt.close()


