from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
	fields = ['email', 'firstname', 'lastname','state','password','country','phone','is_admin']
	list_display = ('email', 'firstname', 'lastname',
	                'country',  'state', 'phone', 'is_admin')
	list_filter = ['state', 'is_admin', 'country', ]
	search_fields = ['id', 'email', 'firstname', 'country', 'lastname']
