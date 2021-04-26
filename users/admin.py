from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
	fields = ['email', 'firstname', 'lastname','country','state','phone','is_admin']
	list_display = ('email', 'firstname', 'lastname', 'country', 'state', 'phone', 'is_admin')
	list_filter = ['country','state','is_admin',]
	search_fields = ['id', 'email', 'firstname', 'lastname']
