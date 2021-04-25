from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# User Manager
class NewUserManager(BaseUserManager):
    def create_user(self, firstname, lastname, email, password):
        user = self.model(firstname=firstname, lastname=lastname,
                          email=self.normalize_email(email))
        user.save(using=self._db)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, firstname, lastname, email, password):
        user = self.create_user(
            firstname=firstname, lastname=lastname, email=email, password=password)
        user.is_admin = True
        user.save()
        return user

# User Model


class User(AbstractBaseUser):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    email = models.EmailField(max_length=255, unique=True, primary_key=True)
    country = models.CharField(max_length=48)
    state = models.CharField(max_length=48)
    phone = models.CharField(max_length=25)
    is_admin = models.BooleanField(default=False)
    picture = models.ImageField( blank = True,max_length = 255, upload_to = 'staticfiels/' )

    objects = NewUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'password']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.firstname + ' ' + self.lastname

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, app=None):
        return True

    def has_module_perms(self, app_label=None):
        return True
