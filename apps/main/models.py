from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import re, bcrypt
from datetime import datetime

class QuoteManager(models.Manager):
    def validate_quote(self,post):
        isValid = True
        if len(post.get("author"))<4:
            isValid = False
        if len(post.get("message"))<11:
            isValid = False
        return isValid







class UserManager(models.Manager):
	def validate_user(self, post):
		isValid = True
		if len(post.get('name')) == 0:
			isValid = False
		if len(post.get('email')) == 0:
			isValid = False
			
		if len(post.get('password')) < 8:
			isValid = False
		if post.get('password') != post.get('password_confirmation'):
			isValid = False
		return isValid	


	def login_user(self, post):
		user = self.filter(email=post.get('email')).first()
		if user and bcrypt.hashpw(post.get('password').encode(), user.password.encode()) == user.password:
			return (True, user)
		else:
			return (False)



# Create your models here.
class User(models.Model):
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	date_of_birth = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Quote(models.Model):
    author = models.CharField(max_length=200)
    message = models.TextField()
    user = models.ForeignKey(User,related_name='quotes')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = QuoteManager()

class Favorite(models.Model):
    user = models.ForeignKey(User,related_name='favorites')
    quote = models.ForeignKey(Quote,related_name='favorites')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
