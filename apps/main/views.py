from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from .models import *
from datetime import datetime


# Create your views here.
def index(request):
	return render(request, 'main/index.html')

def login_user(request):
	if request.method == 'POST':
		login = User.objects.login_user(request.POST)
		if login:
			request.session['user_id'] = login[1].id
			return redirect('/view_dashboard')
		else:
			messages.error(request, 'Invalid credentials')
	
	return redirect('/')

def create_user(request):

	if User.objects.validate_user(request.POST):
		user = User.objects.create(
			name = request.POST.get('name'),
			email = request.POST.get('email'),
			date_of_birth = request.POST.get('dob'),
			password = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt(18))
		)
		request.session['user_id'] = user.id
		return redirect('/view_dashboard')
	return redirect('/')

def view_dashboard(request):
	context = {
		'current_user': User.objects.get(id=request.session['user_id']),
		
	}
	return render(request, 'main/view_dashboard.html', context)