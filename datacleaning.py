import csv
file = open("raw_data.txt","r")

#Đọc toàn bộ file
datas= file.read().split("\n")

#file=open("test.txt",encoding="utf8",mode="w")

with open("clean_data.csv",encoding="utf8",mode="w",newline='') as file_csv:
	header=["sbd","tên","dd","mm","yy","toán","ngữ văn","khxh","khtn","lịch sử","địa lí","gdcd","sinh học","vật lí","hóa học","tiếng anh"]
	writer=csv.writer(file_csv)
	writer.writerow(header)
sbd=2000000
for data in datas:
#Trước đó dùng try except để in ra các sbd bất thường
	sbd+=1
	if sbd in [2000521,2002776,2002833,2005380,2005472,2005733,2005820,2005876,2006091,2006300,2006364,2006544,2006712,2006720,2006904,2008746,2009196,2012503,2019593,2020755,2024536,2027212,2031588,2031948,2035434,2036693,2042067,2042972,2043577,2044668,2046177,2046483,2046496,2046651,2046766,2046771,2046788,2046810,2046841,2046998,2047031,2047122,2047241,2047273,2047304,2047486,2047636,2047834,2047843,2047856,2047865,2048225,2048271,2048279,2048397,2048424,2048427,2048592,2048660,2048701,2048723,2048858,2049069,2049090,2049104,2049164,2049234,2049312,2049383,2049663,2049763,2049775,2049891,2049971,2050378,2050476,2050488,2050516,2050526,2050540,2050576,2050642,2050649,2050722,2050809,2050814,2050899,2050959,2050978,2050984,2050985,2051006,2051072,2051181,2051191,2051234,2051422,2051468,2051472,2051495,2051615,2051616,2051736,2052013,2052030,2052089,2052314,2052373,2052591,2052663,2052711,2052791,2052856,2053000,2053106,2053259,2053593,2053699,2053860,2054235,2054306,2054374,2054508,2054733,2054787,2055119,2055200,2055290,2055296,2055606,2055683,2055803,2055829,2055912,2055930,2055986,2056020,2056032,2056105,2056139,2056186,2056190,2056238,2056273,2056291,2056298,2056333,2056350,2056377,2056393,2056782,2056823,2056865,2056871,2057014,2057294,2057410,2057496,2058404,2058498,2058518,2058789,2058938,2059095,2059163,2059740,2059751,2059769,2059774,2059807,2059852,2060462,2060492,2060536,2060610,2060652,2060656,2060660,2060730,2060738,2061813,2062212,2062236,2062391,2062440,2062898,2063109,2063114,2063179,2063180,2063181,2063207,2063272,2063653,2063707,2063716,2063752,2063754,2063825,2064369,2064704,2064783,2064990,2065104,2065323,2065604,2065877,2065995,2066106,2066212,2066835,2067172,2067291,2067316,2067371,2067383,2067401,2067446,2067467,2067550,2067563,2067659,2067672,2067698,2067762,2067909,2067971,2067996,2068089,2068119,2068156,2068174,2068178,2068243,2068287,2068365,2068382,2068427,2068453,2068548,2068550,2068627,2068667,2068702,2068732,2068846,2068970,2069028,2069043,2069066,2069156,2069290,2069362,2069397,2069843,2069990,2070203,2070870,2071102,2071574,2072480,2072549,2072755,2072823,2073036,2073372,2073477,2073556,2073964,2074135,2074254,2074281,2074367,2074607,2074719]:
			continue
	sbd_str="0"+str(sbd)
	#Chia thành list
	data= data.split("\\n") # với \n cần dùng 2 dấu \\n đây là th đặc biệt

	#Làm sạch data
	for i in range(len(data)):
		data[i]=data[i].replace("\\r","")  #với tất cả ký tự có \ đều dùng \\
		data[i]=data[i].replace("\\t","")
		data[i]=data[i].replace(data[i][data[i].find("<"):data[i].find(">")+1],"")  #Xóa các tag
		data[i]=data[i].replace(data[i][data[i].find("<"):data[i].find(">")+1],"")
		data[i]=data[i].strip()
	data=[i for i in data if i !=""] #Xóa kí tự trống

	#Choose relevent infomation
	name=data[7]
	date=data[8]
	scores=data[9]
	data=[name,date,scores]

	#Tạo dictionary chứa các code kí tự đặc biệt để xử lý data 
	diction={}
	file=open("unicode.txt","r",encoding="utf8")
	unicode_table=file.read().split("\n")

	for i in unicode_table:
		s=i.split(" ")
		diction[s[1]]=s[0]

	#Thay thế các code kí tự đặc biệt
	for i in range(len(data)):
		for j in diction.keys():
			if j in data[i]:
				data[i]=data[i].replace(j,diction[j])
	# Thay thế kí tự chr
	for i in range(len(data)):
		for j in range(len(data[i])):
			if data[i][j:j+2] == "&#":
				data[i]=data[i][:j]+chr(int(data[i][j+2:j+5]))+data[i][j+6:]
	# Cách khác nhưng cách này bị thêm ; ở cuối chr
	#	if data[i].find("&#") !=-1:
	#		z=data[i].find("&#")
	#		data[i]=data[i].replace(data[i][z:z+5],chr(int(data[i][z+2:z+5])))
	#		z=data[i].find("&#")
	#		data[i]=data[i].replace(data[i][z:z+5],chr(int(data[i][z+2:z+5])))
	newname=data[0].upper()
	data[2]=data[2].lower()
	#split ngày sinh
	dob_list=data[1].split("/")
	dd=dob_list[0]
	mm=dob_list[1]
	yy=dob_list[2]

	#Xử lý điểm:
	data[2]=data[2].replace(":","")
	data[2]=data[2].replace("khxh","khxh   ")
	data[2]=data[2].replace("khtn","khtn   ")
	scores_list=data[2].split("   ")
	#Thêm điểm vào dữ liệu
	data=[sbd_str,newname,dd,mm,yy]
	for subject in ["toán","ngữ văn","khxh","khtn","lịch sử","địa lí","gdcd","sinh học","vật lí","hóa học","tiếng anh"]:
		if subject in scores_list:
			data.append(str(float(scores_list[scores_list.index(subject)+1])))
		else:
			data.append("-1")

	with open("clean_data.csv","a",encoding='utf-8',newline='') as file_csv:
		writer=csv.writer(file_csv)
		writer.writerow(data)
#Thêm vào file cách thông thường. Ở trên dùng thư viện csv
"""
	file=open("test.txt",encoding="utf8",mode="a")
	for i in range(len(data)):
		if i==len(data)-1:
			file.write(data[i])
		else:
			file.write(data[i]+",")
	file.write("\n")
"""