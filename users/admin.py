from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
	fields = ['email', 'firstname', 'lastname','state','city','phone','is_admin']
	list_display = ('email', 'firstname', 'lastname',
	                'city',  'state', 'phone', 'is_admin')
	list_filter = ['state', 'is_admin', 'city', ]
	search_fields = ['id', 'email', 'firstname', 'city', 'lastname']
