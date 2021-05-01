from django.contrib import admin
from .models import TransferRequest, OTP, BankAccount


class BankAccountAdmin(admin.ModelAdmin):
    fields = ['user', 'balance', 'account_number', 'id']
    list_display = ['user', 'balance', 'account_number', 'id']
    search_fields = ['account_number', 'id', ]
    list_filter = []


class TransferRequestAdmin(admin.ModelAdmin):
    fields = ['user', 'amount', 'status',
              'bank_name', 'account_number', 'ifto_code', 'date', 'tx_id', 'transaction_type']
    list_display = ('user', 'amount', 'status',
                    'bank_name', 'account_number', 'ifto_code', 'date', 'tx_id', 'transaction_type')
    search_fields = ['status',
                     'bank_name', 'account_number', 'ifto_code',  'tx_id']
    list_filter = ['user', 'status',
                   'ifto_code', 'date', 'transaction_type']


# admin.site.register(TransferRequest, TransferRequestAdmin)
# # admin.site.register( OTP)
# admin.site.register(BankAccount, BankAccountAdmin)
