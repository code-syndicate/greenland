import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.core.mail import send_mail


# Returns  a unique accct number for a bank account
def generate_acct_num():
    k = uuid.uuid4().int
    return str(k)[:10]

# Bank Account


class BankAccount(models.Model):
    user = models.OneToOneField(
        get_user_model(), related_name='bank_account', on_delete=models.CASCADE)
    balance = models.PositiveIntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    account_number = models.CharField(max_length = 25, default = generate_acct_num)

    @property
    def encoded_account_number(self):
        return self.account_number[:4] + '******'

    def __str__(self):
        return self.user.get_full_name() + "'s account"

# Transfer Request \


class TransferRequest(models.Model):
    user = models.ForeignKey(
        get_user_model(), related_name='transfer_requests', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    tx_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    date = models.DateTimeField( default = timezone.now )
    bank_name = models.CharField(max_length=128, )
    bank_branch = models.CharField(max_length=128,)
    transaction_type = models.CharField(max_length= 25, verbose_name = 'Transaction type', default = 'debit', choices = (
        ('credit', 'Credit'),
        ('debit', 'Debit')
    ))
    ifsc_code = models.CharField(max_length=48, null= True)
    city = models.CharField(max_length=48, verbose_name = 'City', null =True)
    account_number = models.CharField(max_length=25)
    transfer_type = models.CharField(max_length=25, choices = (
        ('Intl', 'International Transfer'),
        ('local', 'Local Transfer')
    ), default= 'local')
    status = models.CharField(max_length=25, default='unverified', choices=(
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('declined', 'Declined'),
        ('unverified', 'Awaiting Verification'),
    ))

    def __str__(self):
        return str(self.tx_id)

# OTP generator


def generate_otp():
    code = uuid.uuid4().clock_seq
    return code

# Otp


class OTP(models.Model):
    code = models.CharField(max_length=8, default=generate_otp, unique=True)
    user = models.ForeignKey(
        get_user_model(), related_name='codes', on_delete=models.CASCADE)
    created_at = models.DateTimeField( auto_now_add = True , editable=False)
    timeline_in_minutes = models.PositiveIntegerField(default=60)
    valid = models.BooleanField(default=True)
    used = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'IFSC Code'
        verbose_name_plural  = 'IFSC Codes'

    def __str__(self):
        return 'IFSC Code for ' + self.user.email

    @property
    def is_valid(self):
        if not(self.valid):
            return self.valid

        elapsed = ( timezone.now() - self.created_at).total_seconds()
        valid = elapsed < (self.timeline_in_minutes * 60)
        if not valid:
            self.valid = valid
            self.save()
        return valid

    def send(self):
        if not self.valid:
            return
        msg = " Hello {0}, you requested for an OTP to complete a transaction on our site.Please your OTP {1} to" \
        "authorize your transaction.Do not disclose your OTP to anyone.If you did not initiate thise, send us a mail" \
        "at info@banking.com.Thank you.".format(self.user.firstname, self.code)
        send_mail("Cruise Banking Services", msg, from_email='banking@cruise.com',
                  recipient_list=[self.user.email, ], fail_silently=True, )

    @staticmethod
    def check_otp_against_user(otp,user):
        otp_obj = None
        try:
            otp_obj = OTP.objects.get( code = otp, user = user)
        except OTP.DoesNotExist:
            return None
        else:
            if otp_obj.is_valid and not(otp_obj.used):
                return otp_obj
            else:
                return False



