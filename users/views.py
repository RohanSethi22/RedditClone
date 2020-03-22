from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def login_view(request):
	message=''
	if request.method=='POST':
		if request.POST['password']=='' or request.POST['userid']=='':
			message+='The fields cannot be empty.\n'
		elif request.POST['signup']=='1':			# Signup Response
			if request.POST['password']!=request.POST['password2']:
				message+='Passwords don\'t match.\n'
			else:
				try:
					existing_user=User.objects.get(username=request.POST['userid'])
					message+='Username already taken.'
				except User.DoesNotExist:
					user = User.objects.create_user(username=request.POST['userid'], password=request.POST['password'], first_name=request.POST['fname'], last_name=request.POST['lname'])
					message+='User Created.\n'
					message+='Welcome '+user.first_name
					login(request,user)
					if 'next' in request.POST.keys():
						return redirect(request.POST['next'])
					else:
						return redirect('home')
			
		elif request.POST['signup']=='0':		# Login Response
			message='Login response'
			user = authenticate(username=request.POST['userid'], password=request.POST['password'])
			if user is not None:
				message='Welcome '+user.first_name
				login(request,user)
				if 'next' in request.POST:
					return redirect(request.POST['next'])
				else:
					return redirect('home')
			else:
				message='Invalid username/password'
		return render(request, 'users/login.html', {'message':message})
	else:
		return render(request, 'users/login.html', {'message':message})

def logout_view(request):
	if request.method=='POST':
		logout(request)
	else:
		pass
	return redirect('home')