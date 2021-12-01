
def transferCurrency():
	global newReport
	while "USD" in newReport or "UKP" in newReport or "UER" in newReport:
		if "USD" in newReport:
			end_index=newReport.find("USD")
			start_index= newReport.rfind(" ", 0, end_index) + 1
			newReport=newReport.replace("USD", "EGP", 1)
			old_number=int(newReport[start_index:end_index])
			new_number=old_number*3
			newReport=newReport.replace(str(old_number), str(new_number), 1)
		if "UKP" in newReport:
			end_index = newReport.find("UKP")
			start_index = newReport.rfind(" ", 0, end_index) + 1
			newReport = newReport.replace("UKP", "EGP", 1)
			old_number = int(newReport[start_index:end_index])
			new_number = old_number * 4
			newReport = newReport.replace(str(old_number), str(new_number), 1)
		if "UER" in newReport:
			end_index = newReport.find("UER")
			start_index = newReport.rfind(" ", 0, end_index) + 1
			newReport = newReport.replace("UER", "EGP", 1)
			old_number = int(newReport[start_index:end_index])
			new_number = old_number * 5
			newReport = newReport.replace(str(old_number), str(new_number), 1)

def transferDate():
	global newReport
	while "UST" in newReport or "UKT" in newReport or "UET" in newReport:
		if "UST" in newReport:
			end_index=newReport.find("UST")
			start_index= newReport.rfind(" ", 0, end_index) + 1
			newReport=newReport.replace("UST", "EGT", 1)
			old_date=newReport[start_index:end_index]
			new_date=calcOnDate(old_date,8)
			newReport=newReport.replace(old_date,new_date, 1)
		if "UKT" in newReport:
			end_index=newReport.find("UKT")
			start_index= newReport.rfind(" ", 0, end_index) + 1
			newReport=newReport.replace("UKT", "EGT", 1)
			old_date=newReport[start_index:end_index]
			new_date=calcOnDate(old_date,4)
			newReport=newReport.replace(old_date,new_date, 1)
		if "UET" in newReport:
			end_index=newReport.find("UET")
			start_index= newReport.rfind(" ", 0, end_index) + 1
			newReport=newReport.replace("UET", "EGT", 1)
			old_date=newReport[start_index:end_index]
			new_date=calcOnDate(old_date,-4)
			newReport=newReport.replace(old_date,new_date, 1)

def calcOnDate(_date:str , tdifference:int):
	new_name=_date.split("/")
	number_list=[int(i) for i in new_name]
	number_list[0]= number_list[0] + tdifference
	if number_list[0]>=24:
		number_list[0]= number_list[0] - 24
		number_list[1]+=1
		if number_list[1]>30:
			number_list[1]=1
			number_list[2]+=1
			if number_list[2]>12:
				number_list[2]=1
				number_list[3]+=1
	elif number_list[0]<0:
		number_list[0]= number_list[0] + 24
		number_list[1]-=1
		if number_list[1]==0:
			number_list[1]=30
			number_list[2]-=1
			if number_list[2]==0:
				number_list[2]=12
				number_list[3]-=1
	string_list=[str(i) for i in number_list]
	new_date="/".join(string_list)
	return new_date
try:
	readPath=input("Please enter the file path you want to change it's currency and time (e.g E:\\report.txt)")
	file=open(readPath, "r")
	report=file.read()
	newReport=report
	writePath=input("Please enter the file path you want to write in it (e.g E:\\newreport.txt)")
	operation=input("Please enter the no. of operation you want to execute(1,2,3)? :"
	                "1- change currency"
	                "2- change time "
	                "3- change both currency and time")
	if operation=="1":
		transferCurrency()
	elif operation=="2":
		transferDate()
	elif operation=="3":
		transferCurrency()
		transferDate()
	else:
		print("Invalid number !")
	file2=open(writePath,"w")
	file2.write(newReport)
	print("The old report :")
	print(report)
	print("The new report :")
	print(newReport)
except:
	print("The file path you entered doesn't exist !")
finally:
	file.close()
	file2.close()





