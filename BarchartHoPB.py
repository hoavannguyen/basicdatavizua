import matplotlib.pyplot as plt
import numpy 
with open("clean_data.csv",encoding="utf-8") as file:
 	data=file.read().split("\n")

header = data[0]
students= data[1:]
students.pop()

total_students=len(students)

header=header.split(",")
#split each student
for i in range(total_students):
	students[i]=students[i].split(",")

lastnames=[]
names_count=[]
for s in students:
	s_name=s[1].split(" ")
	lastname=s_name[0]
	if lastname not in lastnames:
		lastnames.append(lastname)
		names_count.append(0)
		names_count[lastnames.index(lastname)]+=1  #đếm vào đúng địa chỉ tương ứng với listnames
	else:
		names_count[lastnames.index(lastname)]+=1

#Sắp xếp lại 2 list dùng ctdl gt
for i in range(len(names_count)-1):
	for j in range(len(names_count)):
		if names_count[i]>names_count[j]:
			temp=names_count[i]
			names_count[i]=names_count[j]
			names_count[j]=temp

			temp=lastnames[i]
			lastnames[i]=lastnames[j]
			lastnames[j]=temp
print(lastnames,names_count)

import matplotlib.pyplot as plt
import numpy 
#Barchart
figure,axis=plt.subplots()

#list from 0-11
y_pos = numpy.arange(len(lastnames[0:20]))


#plot the barchart using 2 lists
plt.bar(y_pos, names_count[0:20])

#Đổi tên trục nằm ngang
plt.xticks(y_pos, lastnames[0:20])

#Đặt giá trị giới hạn cho trục y
axis.set_ylim(0,30000)

#Tiêu đề, chú thích
plt.ylabel('Số thí sinh')
plt.title('20 họ phổ biến nhất trong kì thi')

# Vẽ số của số học sinh trên đỉnh của các Bar
rects=axis.patches 

for rect, label in zip(rects, names_count[0:20]):
    height = rect.get_height()
    axis.text(
        rect.get_x() + rect.get_width() / 2, height , label, ha="center", va="bottom")

plt.show()