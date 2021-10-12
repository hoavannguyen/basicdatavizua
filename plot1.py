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

# Thí sinh không làm bài thi
not_take_exam=[0]*len(subjects)

for i in range(total_students):  
	for j in range(5,len(students[i])):
		if students[i][j]=="-1":   #Có thể thay thế bằng so sánh str
			not_take_exam[j-5]+=1  # j-5 vì điểm bắt đầu từ ô thứ 5 trong data

#Tính phần trăm thí sinh không làm bài thi các môn
not_take_exam_percentage=[0]*len(subjects)
for i in range(len(subjects)):
	not_take_exam_percentage[i]=round(not_take_exam[i]/total_students*100,2)

# Vẽ biểu đồ Barchart
import matplotlib.pyplot as plt
import numpy 

figure,axis=plt.subplots()

#list from 0-11
y_pos = numpy.arange(len(subjects))

#plot the barchart using 2 lists
plt.bar(y_pos, not_take_exam_percentage)

#Đổi tên trục nằm ngang
plt.xticks(y_pos, subjects)

#Đặt giá trị giới hạn cho trục y
axis.set_ylim(0,100)

#Tiêu đề, chú thích
plt.ylabel('Percentage')
plt.title('Số học sinh bỏ thi hoặc không đăng kí')

# Vẽ số của số học sinh trên đỉnh của các Bar
rects=axis.patches 

for rect, label in zip(rects, not_take_exam):
    height = rect.get_height()
    axis.text(
        rect.get_x() + rect.get_width() / 2, height +1 , label, ha="center", va="bottom")
plt.show()
