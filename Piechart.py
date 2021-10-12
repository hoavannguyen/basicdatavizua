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


#Vẽ biểu đồ piechart tỉ lệ số môn học sinh thi

listcountsomonthi=[0]*10  # Do có 9 môn học
diemtbtheosomonthi=[0]*10
for s in students:
	count=0
	total=0
	check=s[5:7]+s[9:]
	for i in check:
		if i!="-1":
			total+=float(i)
			count+=1
	diemtb=total/count
	diemtbtheosomonthi[count]+=diemtb  # Ở đây mới tính đc tổng
	listcountsomonthi[count]+=1
	#check=s[5:7]+s[9:]
	#count=9-check.count("-1")
	#listcountsomonthi[count]+=1


for i in range(10):
	if listcountsomonthi[i] != 0:
		diemtbtheosomonthi[i]=round(diemtbtheosomonthi[i]/listcountsomonthi[i],2)
print(listcountsomonthi,"\n",diemtbtheosomonthi)


# Pie chart phần trăm số môn thí sinh tham gia thi
labels = "0","1","2","3","4","5","6","7","8","9"

fig1, ax1 = plt.subplots()
ax1.pie(listcountsomonthi, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


#Barchart điểm trung bình 
figure,axis=plt.subplots()

#list from 0-11
y_pos = numpy.arange(len(listcountsomonthi))

#plot the barchart using 2 lists
plt.bar(y_pos, diemtbtheosomonthi)

#Đổi tên trục nằm ngang
plt.xticks(y_pos, labels)

#Đặt giá trị giới hạn cho trục y
axis.set_ylim(0,10)

#Tiêu đề, chú thích
plt.ylabel('Average')
plt.title('Điểm trung bình của các thí sinh theo số môn dự thi')

# Vẽ số của số học sinh trên đỉnh của các Bar
rects=axis.patches 

for rect, label in zip(rects, diemtbtheosomonthi):
    height = rect.get_height()
    axis.text(
        rect.get_x() + rect.get_width() / 2, height , label, ha="center", va="bottom")

plt.show()