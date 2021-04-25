from django.forms import Form
from django import forms


class LocalTransferForm(Form):
    # account_type = forms.CharField(
        # max_length=10, min_length=4, strip=True, required=True, label='Account Type')
    account_number = forms.IntegerField(min_value = 100000000, required=True, label = 'Account Number')
    amount = forms.IntegerField(
        min_value=10, required=True, label='Amount')


class IntlTransferForm(LocalTransferForm):
    iban_code = forms.CharField(
        max_length=25, min_length=3, strip=True, required=True, label='IBAN code')
    swift_code = forms.CharField(
        max_length=25, min_length=3, strip=True, required=True, label='SWIFT code')
    bank_name = forms.CharField(
        max_length=256, min_length=10, strip=True, required=True, label='Bank name')
    bank_address = forms.CharField(
        max_length=256, min_length=10, strip=True, required=True, label='Bank address')
    country = forms.CharField(max_length=35, min_length=2, strip=True, required=True, label = 'country')



class SigninForm(Form):
    email = forms.EmailField(max_length= 255, min_length = 8,required=True, label = 'Email')
    password = forms.CharField( max_length = 25, min_length = 8, strip = True, required  =True, label = 'Password' )


class VerifyOTPForm(Form):
    otp = forms.CharField(max_length = 16,  min_length = 4, strip = True, required = True )
    reqID = forms.UUIDField(strip=True, required=True)
