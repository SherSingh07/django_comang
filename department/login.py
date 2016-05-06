
from company.settings import USERNAME, PASSWORD

	#method to verify user authentication	
def verify_user(request):
	print ("====>verifying user ")
	if request.GET.get('username') == USERNAME and request.GET.get('password') == PASSWORD:
		request.session['username'] = request.GET.get('username')
		request.session['password'] = request.GET.get('password')

	if request.session['username'] == USERNAME and request.session['password'] == PASSWORD:
		print ("====>user authorized ") 
		return True
	else:
		return False


def logout_user(request):
	request.session['username'] = ''
	request.session['password'] = ''
	
