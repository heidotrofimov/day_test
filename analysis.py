import os
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import math


list_of_days=[]
not_found=0
did_found=0


places=["T35VMC"]
years=["2020"]

pr=["2","3","5"]

months_days=[[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
months_found=[[[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0]]]
months_not_found=[[[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0]]]
names=["November","October","September","August","July"]

#Asukohad eraldi, aastad kokku

for place in places:
  for p in pr:
    months_days=[]
    months_not_found=[]
    months_found=[]
    for k in range(5):
      temp=[]
      months_days.append(temp)
      months_not_found.append(0)
      months_found.append(0)
    place_days=[]
    place_not_found=0
    place_did_found=0
    for year in years:
      for directory in os.listdir(place+"_"+year+"_256_pr/target_images"):
        date_str=directory.split("_")[2]
        date_obj=datetime(int(date_str[0:4]),int(date_str[4:6]),int(date_str[6:8]))
        f=open(place+"_"+year+"_256/target_images/"+directory,"r")
        lines=f.readlines()
        f.close()
        for target_tile in lines:
          found_date=datetime(1900,1,1)
          found=False
          for directory2 in os.listdir(place+"_"+year+"_256_pr/clear_images_"+p):
            date_str2=directory2.split("_")[2]
            date_obj2=datetime(int(date_str2[0:4]),int(date_str2[4:6]),int(date_str2[6:8]))
            if(date_obj>date_obj2):
              f=open(place+"_"+year+"_256_pr/clear_images_"+p+"/"+directory2,"r")
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
            if(date_str[4:6]=="11"):
              months_days[0].append(between)
              months_found[0]+=1
            if(date_str[4:6]=="10"):
              months_days[1].append(between)
              months_found[1]+=1
            if(date_str[4:6]=="09"):
              months_days[2].append(between)
              months_found[2]+=1
            if(date_str[4:6]=="08"):
              months_days[3].append(between)
              months_found[3]+=1
            if(date_str[4:6]=="07"):
              months_days[4].append(between)
              months_found[4]+=1
          else:
            not_found+=1
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
    nr=int(math.ceil(maks/5))
    bins=[]
    values=[]
    bins2=[]
    bins2.append(0)
    for j in range(nr):
      bins.append(str(j*5)+"<x<"+str((j+1)*5))
      bins2.append("<"+str((j+1)*5))
      nr_of_days=0
      for val in place_days:
        if(val>=j*5 and val<(j+1)*5):
          nr_of_days+=1
      values.append((nr_of_days/all_days)*100)
    bins.append("∞")
    values.append((place_not_found/all_days)*100)
    values2=[]

    values2.append(0)
    for j in range(len(bins)-1):
      values2.append(values2[-1]+values[j])

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle(place+"\nAverage time distance: "+str(int(aver))+"\n For "+str(place_did_found)+" tiles clear historical image was found, for "+str(place_not_found)+" tiles no clear historical image was found\nPercentage of polluted pixels allowed: "+p)
    fig.set_figheight(8)
    fig.set_figwidth(15)

    ax1.bar(bins,values)
    ax1.set(xlabel="Days between target tile and last clear tile", ylabel="% of all target tiles")
    ax1.set_xticklabels(bins, rotation=45)
    ax1.grid()
    xticklock=[]
    for w in range(len(bins2[1:])):
      xticklock.append(w+0.5)

    ax2.plot(bins2,values2, linestyle='--', drawstyle='steps')
    ax2.set_xticks(xticklock)
    print(bins2)
    ax2.set_xticklabels(bins2[1:])
    ax2.set(xlabel="Days between target tile and last clear tile", ylabel="% of all target tiles")
    ax2.set_yticks(np.arange(min(values2), max(values2)+5, 5.0))
    ax2.grid()
    plt.savefig("results/"+place+"_256_allyears_pr"+p+".png",bbox_inches='tight')
    plt.close()
    for q in range(5):
        all_days=months_found[q]+months_not_found[q]
        aver=np.mean(months_days[q])
        maks=np.max(months_days[q])
        miinn=np.min(months_days[q])
        nr=int(math.ceil(maks/5))
        bins=[]
        values=[]
        bins2=[]
        bins2.append(0)
        for j in range(nr):
          bins.append(str(j*5)+"<x<"+str((j+1)*5))
          bins2.append("<"+str((j+1)*5))
          nr_of_days=0
          for val in months_days[q]:
            if(val>=j*5 and val<(j+1)*5):
              nr_of_days+=1
          values.append((nr_of_days/all_days)*100)
        bins.append("∞")
        values.append((place_not_found/all_days)*100)
        values2=[]

        values2.append(0)
        for j in range(len(bins)-1):
          values2.append(values2[-1]+values[j])

        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.suptitle(names[q]+"\nAverage time distance: "+str(int(aver))+"\n For "+str(months_found[q])+" tiles clear historical image was found, for "+str(months_not_found[q])+" tiles no clear historical image was found\nPercentage of polluted pixels allowed: "+p)
        fig.set_figheight(8)
        fig.set_figwidth(15)

        ax1.bar(bins,values)
        ax1.set(xlabel="Days between target tile and last clear tile", ylabel="% of all target tiles")
        ax1.set_xticklabels(bins, rotation=45)
        ax1.grid()
        xticklock=[]
        for w in range(len(bins2[1:])):
          xticklock.append(w+0.5)

        ax2.plot(bins2,values2, linestyle='--', drawstyle='steps')
        ax2.set_xticks(xticklock)
        print(bins2)
        ax2.set_xticklabels(bins2[1:])
        ax2.set(xlabel="Days between target tile and last clear tile", ylabel="% of all target tiles")
        ax2.set_yticks(np.arange(min(values2), max(values2)+5, 5.0))
        ax2.grid()
        plt.savefig("results/"+place+"_"+names[q]+"_256_allyears_pr"+p+".png",bbox_inches='tight')
        plt.close()
      
    
    
'''  
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
    for directory in os.listdir(place+"_"+year+"_256/target_images"):
      date_str=directory.split("_")[2]
      date_obj=datetime(int(date_str[0:4]),int(date_str[4:6]),int(date_str[6:8]))
      f=open(place+"_"+year+"_256/target_images/"+directory,"r")
      lines=f.readlines()
      f.close()
      for target_tile in lines:
        found_date=datetime(1900,1,1)
        found=False
        for directory2 in os.listdir(place+"_"+year+"_256/clear_images"):
          date_str2=directory2.split("_")[2]
          date_obj2=datetime(int(date_str2[0:4]),int(date_str2[4:6]),int(date_str2[6:8]))
          if(date_obj>date_obj2):
            f=open(place+"_"+year+"_256/clear_images/"+directory2,"r")
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
  bins2=[]
  bins2.append(0)
  for j in range(nr):
    bins.append(str(j*30)+"<x<"+str((j+1)*30))
    bins2.append("<"+str((j+1)*30))
    nr_of_days=0
    for val in place_days:
      if(val>=j*30 and val<(j+1)*30):
        nr_of_days+=1
    values.append((nr_of_days/all_days)*100)
  bins.append("∞")
  values.append((place_not_found/all_days)*100)
  values2=[]

  values2.append(0)
  for j in range(len(bins)-1):
    values2.append(values2[-1]+values[j])
  
  fig, (ax1, ax2) = plt.subplots(1, 2)
  fig.suptitle(year+"\nAverage time distance: "+str(int(aver))+"\n For "+str(place_did_found)+" tiles clear historical image was found, for "+str(place_not_found)+" tiles no clear historical image was found")
  fig.set_figheight(8)
  fig.set_figwidth(15)
    
  ax1.bar(bins,values)
  ax1.set(xlabel="Days between target tile and last clear tile", ylabel="% of all target tiles")
  ax1.set_xticklabels(bins, rotation=45)
  ax1.grid()

  ax2.plot(bins2,values2, linestyle='--', drawstyle='steps')
  ax2.set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
  ax2.set_xticklabels(bins2[1:])
  ax2.set(xlabel="Days between target tile and last clear tile", ylabel="% of all target tiles")
  ax2.set_yticks(np.arange(min(values2), max(values2)+5, 5.0))
  ax2.grid()
  plt.savefig("results/"+year+"_256_allplaces.png",bbox_inches='tight')
  plt.close()
  
  
#Kõik kokku:

all_days=did_found+not_found
aver=np.mean(list_of_days)
maks=np.max(list_of_days)
miinn=np.min(list_of_days)
nr=int(math.ceil(maks/30))
bins=[]
values=[]
bins2=[]
bins2.append(0)
for j in range(nr):
  bins.append(str(j*30)+"<x<"+str((j+1)*30))
  bins2.append("<"+str((j+1)*30))
  nr_of_days=0
  for val in list_of_days:
    if(val>=j*30 and val<(j+1)*30):
      nr_of_days+=1
  values.append((nr_of_days/all_days)*100)
bins.append("∞")
values.append((not_found/all_days)*100)

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle("\nAverage time distance: "+str(int(aver))+"\n For "+str(did_found)+" tiles clear historical image was found, for "+str(not_found)+" tiles no clear historical image was found")
fig.set_figheight(8)
fig.set_figwidth(15)

values2=[]

values2.append(0)
for j in range(len(bins)-1):
  values2.append(values2[-1]+values[j])

ax1.bar(bins,values)
ax1.set(xlabel="Days between target tile and last clear tile", ylabel="% of all target tiles")
ax1.set_xticklabels(bins, rotation=45)
ax1.grid()

ax2.plot(bins2,values2, linestyle='--', drawstyle='steps')
ax2.set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
ax2.set_xticklabels(bins2[1:])
ax2.set(xlabel="Days between target tile and last clear tile", ylabel="% of all target tiles")
ax2.set_yticks(np.arange(min(values2), max(values2)+5, 5.0))
ax2.grid()
plt.savefig("results/alldata_256.png",bbox_inches='tight')
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
  
  bins2=[]
  bins2.append(0)
  values2=[]

  values2.append(0)
    
  for j in range(nr):
    bins.append(str(j*30)+"<x<"+str((j+1)*30))
    bins2.append("<"+str((j+1)*30))
    nr_of_days=0
    for val in months_days[i]:
      if(val>=j*30 and val<(j+1)*30):
        nr_of_days+=1
    values.append((nr_of_days/all_days)*100)
  bins.append("∞")
  values.append((months_not_found[i]/all_days)*100)
  for j in range(len(bins)-1):
    values2.append(values2[-1]+values[j])
  xlabels=[]
  for k in range(len(bins2)-1):
    xlabels.append(k+0.5)
  fig, (ax1, ax2) = plt.subplots(1, 2)
  fig.suptitle(name+"\nAverage time distance: "+str(int(aver))+"\n For "+str(months_did_found[i])+" tiles clear historical image was found, for "+str(months_not_found[i])+" tiles no clear historical image was found")
  fig.set_figheight(8)
  fig.set_figwidth(15)
    
  ax1.bar(bins,values)
  ax1.set(xlabel="Days between target tile and last clear tile", ylabel="% of all target tiles")
  ax1.set_xticklabels(bins, rotation=45)
  ax1.grid()

  ax2.plot(bins2,values2, linestyle='--', drawstyle='steps')
  ax2.set_xticks(xlabels)
  ax2.set_xticklabels(bins2[1:])
  ax2.set(xlabel="Days between target tile and last clear tile", ylabel="% of all target tiles")
  ax2.set_yticks(np.arange(min(values2), max(values2)+5, 5.0))
  ax2.grid()
  plt.savefig("results/"+name+"_256_allplaces_allyears.png",bbox_inches='tight')
  plt.close()
'''
