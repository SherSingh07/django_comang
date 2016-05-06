from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.http import HttpResponse
from .form import ComputerForm
from django.views.decorators.csrf import csrf_exempt
from models import Computer
from models import Attendence
from login import verify_user, logout_user
from util.utils import save_atten_to_database


# Create your views here.

@csrf_exempt
def home(request):	
	computers = Computer.objects.all()

	for computer in computers:	
		#print "Id : %d" % (int(computer.id))
		print "Name : " + computer.name
		#print "Designation : " + computer.designation
	return render_to_response("index.html", {"computers":computers})

@csrf_exempt	
def main(request):
	if verify_user(request) == True:
		print "====>redirecting to main page"

		employees = Attendence.objects.all()
		for employee in employees:
			fd = 'name'
			print "employee  is :using field " + getattr(employee, 'name')
		return render_to_response("home.html", {"employees":employees})
	else:
		print "====>authentication failed"
		return render_to_response("index.html")

@csrf_exempt
def save_attendence(request):
	save_atten_to_database(request.POST)
	print("data from page ================> %s"%(request.POST))
	for key in request.POST:
		print 'name is : ' + key +'attendence is ' + request.POST.get(key) 

	return HttpResponse("attendence saved")
	

@csrf_exempt
def department(request):
	print "------------------------------------------------------"
	print "User try to login: department "
	print("Credential :    %s             %s   "%(request.GET.get('username'), request.GET.get('password')))
	
	print "=============Current computer============= "
	print "ID : %s        Name  	 %s        Designation : %s  Profile : %s   Salary : %s      Address  :  %s "\
	 % (request.GET.get('id'), request.GET.get('name'), request.GET.get('designation'), \
	request.GET.get('profile'), request.GET.get('salary'), request.GET.get('address'))
	
	name_val =  request.GET.get('name')
	desig_val = request.GET.get('designation')
	profile_val = request.GET.get('profile')
	salary_val = request.GET.get('salary')
	address_val= request.GET.get('address')

	# check for null values
	if name_val != '' and name_val != None and desig_val != '' and desig_val != None \
	 and profile_val != ''  and profile_val != None and salary_val != '' \
	and salary_val is not  None and address_val is not '' and address_val is not None:
	# make a object of model
		comp = Computer(name= name_val, designation=desig_val, work_profile=profile_val,\
	 	salary=salary_val, address=address_val)
		comp.save()
		print "saving values"
	else:
		print("Please enter all values..")
	
	return render_to_response("next.html")
	
	#staff page
def staff(request):
	if verify_user(request) == True:
		return render_to_response("staff.html")
	else:
		print "====>authentication failed"
		return render_to_response("index.html")	
	
	#project page
def projects(request):
	if verify_user(request) == True:
		return render_to_response("projects.html")
	else:
		print "====>authentication failed"
		return render_to_response("index.html")	

	#revenue and expenses page
def rev_exp(request):
	if verify_user(request) == True:
		return render_to_response("revenueExpenses.html")
	else:
		print "====>authentication failed"
		return render_to_response("index.html")


def workhours(request):
	if verify_user(request) == True:
		return render_to_response("workhours.html")
	else:
		print "====>authentication failed"
		return render_to_response("index.html")
	

def carrier(request):
	if verify_user(request) == True:
		return render_to_response("carrier.html")
	else:
		print "====>authentication failed"
		return render_to_response("index.html")

def about_us(request):
	if verify_user(request) == True:
		return render_to_response("about.html")
	else:
		print "====>authentication failed"
		return render_to_response("index.html")

def sign_up(request):
	print("carrier about us")
	return render_to_response("signin.html")

def user_logout(request):
	print("----------------user logging out-------------------")
	logout_user(request)
	return redirect('/')
