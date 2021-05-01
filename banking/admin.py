from django.contrib import admin
from .models import TransferRequest, OTP, BankAccount


class BankAccountAdmin(admin.ModelAdmin):
    fields = ['user', 'balance', 'account_number', 'id']
    list_display = ['user', 'balance', 'account_number', 'id']
    search_fields = ['account_number', 'id', ]
    list_filter = []


class TransferRequestAdmin(admin.ModelAdmin):
    fields = ['user', 'amount', 'status',
              'bank_name', 'account_number', 'ifsc_code', 'date', 'tx_id', 'transaction_type']
    list_display = ('user', 'amount', 'status',
                    'bank_name', 'account_number', 'ifsc_code', 'date', 'tx_id', 'transaction_type')
    search_fields = ['status',
                     'bank_name', 'account_number', 'ifsc_code',  'tx_id']
    list_filter = ['user', 'status',
                   'ifsc_code', 'date', 'transaction_type']

class OTPAdmin(admin.ModelAdmin):
    fields = ['user','timeline_in_minutes','valid','used']
    list_display = ('user', 'timeline_in_minutes','used', 'created_at', 'valid','code')
    search_fields = [ 'timeline_in_minutes', 'code']
    list_filter = ['user', 'created_at', 'valid', 'used']


# admin.site.register(TransferRequest, TransferRequestAdmin)
# # admin.site.register( OTP)
# admin.site.register(BankAccount, BankAccountAdmin)
