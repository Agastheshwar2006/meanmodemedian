from collections import Counter
import csv

with open("list_chart.csv",newline ="") as f:
    reader=csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
newdata = []
for i in range(len(file_data)):
    num = file_data[i][1]
    newdata.append(float(num))

data = Counter(newdata)
moderange ={
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for height,occurrence in data.items():
    if 50 < float(height)<60:
        moderange["50-60"]+=occurrence
    elif  60 < float(height)<70:
        moderange["60-70"]+=occurrence
    elif  70 < float(height)<80:
        moderange["70-80"]+=occurrence

mode_range,mode_occurrence=0,0
for range,occurrence in moderange.items():
    if occurrence > mode_occurrence:
        mode_range,mode_occurrence=[int(range.split("-")[0]),int(range.split("-")[1])],occurrence
        
mode = float((mode_range[0]+mode_range[1])/2)
print(f'mode is: {mode:2f} ')