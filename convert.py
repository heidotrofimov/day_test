import os

os.system("mkdir T35VMC_2020_2")

os.system("mkdir T35VMC_2020_2/clear_images")

os.system("mkdir T35VMC_2020_2/target_images")

for dire in os.listdir("T35VMC_2020/target_images"):
  f=open("T35VMC_2020_2/target_images/"+dire+".txt","w")
  for filename in os.listdir("T35VMC_2020/target_images/"+dire):
    f.write(filename.split(".")[0]+"\n")
  f.close()
  
for dire in os.listdir("T35VMC_2020/clear_images"):
  f=open("T35VMC_2020_2/clear_images/"+dire+".txt","w")
  for filename in os.listdir("T35VMC_2020/clear_images/"+dire):
    f.write(filename.split(".")[0]+"\n")
  f.close()
