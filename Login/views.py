from django.shortcuts import render
from django.http import HttpResponse
from Login.dao import Dao 

def Login(request):
	# emailid = request.POST.get('emailid')
	# password = request.POST.get('password')
	# dao = Dao()
	# userdetails = dao.Login(emailid, password)
	# if userdetails is not None :
	# 	time1 = datetime.now()
	# 	request.session.set_expiry(600)
	# 	request.session["emailid"] = emailid
	# 	emailid = request.session["emailid"]
	# 	usertype = userdetails[0][0]
	# 	if (usertype == 1):
	# 		return render(request, 'schedules/Dashboard.html')
	# 	elif(usertype == 2):
	# 		return render(request, 'Faculty/faculty_dashboard.html')
	# 	elif(usertype == 3):
	# 		return render(request, 'Student/students_dashboard.html')
	# 	else:
	# 		return render(request, 'schedules/index.html')
	# else:
	return render(request, 'login.html')
