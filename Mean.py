import csv

file=open("SOCR-HeightWeight.csv")
read_file=csv.reader(file)

new_list=list(read_file)
new_list.pop(0)

content=[]

for i in range(len(new_list)):
    height_data=new_list[i][1]
    content.append(float(height_data))

total=0

for j in content:
    total=total+j

mean=total/len(content)

#printing mean
print(mean)

content.sort()

if len(content) % 2 == 0:
    median1 = float(content[len(content)//2])
    median2 = float(content[len(content)//2 -1])
    result=(median1+median2)/2
else:
    result = content[len(content)//2]

#printing median
print(result)