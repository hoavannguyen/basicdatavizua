with open("clean_data.csv",encoding="utf-8") as file:
 	data=file.read().split("\n")

header = data[0]
students= data[1:]
students.pop()

total_students=len(students)

header=header.split(",")
subjects=header[5:]
#split each student
for i in range(total_students):
	students[i]=students[i].split(",")

# Vẽ
count_age=[0]*11
ages=["17","18","19","20","21","22","23","24","25","26"]
average_points_by_age=[0]*11
for s in students:
	age=2020-int(s[4])
	count=0
	total=0
	check=s[5:7]+s[9:]
	for i in check:
		if i!="-1":
			total+=float(i)
			count+=1
	diemtb=total/count
	for i in range(len(ages)):
		if age==int(ages[i]):
			average_points_by_age[i]+=diemtb
			count_age[i]+=1
	if age>26:
		average_points_by_age[-1]+=diemtb
		count_age[-1]+=1
ages.append(">26")
for i in range(len(average_points_by_age)):
	average_points_by_age[i]=average_points_by_age[i]/count_age[i]  #List điểm trung bình		

for i in range(len(average_points_by_age)):
	average_points_by_age[i]=average_points_by_age[i]*7000 # Nhân với 7000 để vẽ linechart so với cột số học sinh

import matplotlib.pyplot as plt
import numpy as np

x=np.arange(len(ages))
y=np.arange(len(ages))

fig, axis=plt.subplots()
#plot the barchart using 2 lists
plt.bar(x, count_age)
plt.plot(x,average_points_by_age,color="red",marker='o') # vẽ line chart
#Đổi tên trục nằm ngang
plt.xticks(x, ages)

#Đặt giá trị giới hạn cho trục y
axis.set_ylim(0,70000)
axis.set_ylabel("Số học sinh")
axis.set_xlabel("Tuổi")
#Tạo ticks bên  phải
ax2=axis.twinx()
ax2.tick_params('y',color="r")
ax2.set_ylabel("Điểm trung bình")
ax2.set_ylim(0,10)

#Tiêu đề, chú thích
plt.title('Điểm trung bình theo độ tuổi')

# Vẽ số của số học sinh trên đỉnh của các Bar
rects=axis.patches 

for rect, label in zip(rects, count_age):
    height = rect.get_height()
    axis.text(
        rect.get_x() + rect.get_width() / 2, height , label, ha="center", va="bottom")

plt.show()