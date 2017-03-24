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
		"quotes": Quote.objects.all(),
    	"favorites":Favorite.objects.filter(user__id=request.session["user_id"]).distinct()
		
	}
	return render(request, 'main/view_dashboard.html', context)

def logout(request):
	request.session.clear()
	return redirect('/')

def contrib_quote(request):
    if Quote.objects.validate_quote(request.POST):
        quote = Quote.objects.create(
        author = request.POST.get("author"),
        message = request.POST.get("message"),
        user = User.objects.get(id=request.session["user_id"])
        )
        return redirect ("/view_dashboard")
    else:
        messages.error(request,'Quoted by or Message is too short')
        return redirect ("/view_dashboard")

def favorites(request, id):
    user = User.objects.get(id=request.session["user_id"])
    quote = Quote.objects.get(id=id)
    
    favorite = Favorite.objects.create(
    quote = quote,
    user = user
    )
    request.session["favs"]=favorite.quote.id
    return redirect ("/view_dashboard")

def remove(request, id):
    favorite=Favorite.objects.filter(quote__id=id).delete()
    return redirect("/view_dashboard")

def user_info(request, id):
    context = {
    "user":User.objects.get(id=id),
    "posts":Quote.objects.all().filter(user=id)
    }
    return render(request,'main/user_profile.html',context)

