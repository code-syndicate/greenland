from django.contrib.admin import AdminSite
from users.models import User
from django.utils import timezone
from datetime import timedelta
from users.admin import UserAdmin
from users.models import User
from banking.models import TransferRequest,BankAccount
from banking.admin import TransferRequestAdmin,BankAccountAdmin


class AdminSite1(AdminSite):
	site_header = 'Reserve Bank of India(Administration)'
	site_title = 'RBI Admin'
	index_title = 'Manage RBI '
	site_url = 'http://localhost:8000/'


admin_site1 = AdminSite1(name='godmode')

admin_site1.register(TransferRequest, TransferRequestAdmin)
admin_site1.register(BankAccount, BankAccountAdmin )
admin_site1.register(User, UserAdmin)


