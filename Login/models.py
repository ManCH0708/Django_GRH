
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class RHUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('L\'adresse email est obligatoire')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

class RHUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    objects = RHUserManager()

    USERNAME_FIELD = 'email'




