from django.contrib import admin
from .models import TransferRequest, OTP, BankAccount


class BankAccountAdmin(admin.ModelAdmin):
    fields = ['user', 'balance', 'account_number', 'id']
    list_display = ['user', 'balance', 'account_number', 'id']
    search_fields = ['account_number', 'id', ]
    list_filter = []


class TransferRequestAdmin(admin.ModelAdmin):
    fields = ['user', 'amount', 'status',
              'bank_name', 'account_number', 'bank_swift', 'date', 'tx_id', 'transaction_type']
    list_display = ('user', 'amount', 'status',
                    'bank_name', 'account_number', 'bank_swift', 'date', 'tx_id', 'transaction_type')
    search_fields = ['status',
                     'bank_name', 'account_number', 'bank_swift',  'tx_id']
    list_filter = ['user', 'status',
                   'bank_swift', 'date', 'transaction_type']


# admin.site.register(TransferRequest, TransferRequestAdmin)
# # admin.site.register( OTP)
# admin.site.register(BankAccount, BankAccountAdmin)
