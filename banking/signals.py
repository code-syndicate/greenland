from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.contrib.auth import authenticate
from django.db.models.signals import post_save
from .models import BankAccount, TransferRequest


@receiver(post_save, sender=get_user_model(), dispatch_uid='add_bank_acct')
def add_bank_acct(sender, **kwargs):
    user = kwargs.get('instance')

    if not BankAccount.objects.filter(user=user).exists():
        new_acct = BankAccount.objects.create(user=user, balance=0)
        new_acct.save()


@receiver(post_save, sender=TransferRequest, dispatch_uid='deduct_amount')
def deduct_amount(sender, request=None, **kwargs):
    transfer = kwargs.get('instance')
    user = transfer.user
    if transfer.status == 'approved':
        if transfer.deducted:
            return
        else:
            if transfer.amount > user.bank_account.balance:
                return
            user.bank_account.balance = user.bank_account.balance - transfer.amount
            user.bank_account.save()
            transfer.deducted = True
            transfer.save()
