from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.contrib.auth import authenticate
from django.db.models.signals import post_save
from .models import BankAccount


@receiver(post_save, sender=get_user_model(), dispatch_uid='add_bank_acct')
def add_bank_acct(sender, **kwargs):
    user = kwargs.get('instance')

    if not BankAccount.objects.filter(user=user).exists():
        new_acct = BankAccount.objects.create(user=user, balance=0)
        new_acct.save()


# @receiver(post_save, sender=get_user_model(), dispatch_uid='rephrase_password')
# def rephrase_password(sender, **kwargs):
#     user = kwargs.get('instance')
#     user.refresh_from_db()
#     if authenticate(kwargs.get('request'), username = user.email, password = user.password) is None:
#         user.set_password(user.password)
#         user.save()
