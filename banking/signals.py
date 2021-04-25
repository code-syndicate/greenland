from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import BankAccount



@receiver(post_save, sender = get_user_model(), dispatch_uid = 'add_bank_acct')
def add_bank_acct( sender, **kwargs ):
    user = kwargs.get('instance')
    # if not user.check_password(user.password):
    #     user.set_password(user.password)
    #     user.save()

    if not BankAccount.objects.filter(user = user).exists():
        new_acct = BankAccount.objects.create(user = user, balance = 0)
        new_acct.save()

    return

