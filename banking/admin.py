from django.contrib import admin
from .models import TransferRequest,OTP,BankAccount

admin.site.register( TransferRequest)
admin.site.register( OTP)
admin.site.register(BankAccount)

