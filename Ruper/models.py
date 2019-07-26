from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.


class UserData(AbstractUser):
    password = models.CharField(verbose_name='Password', max_length=255,
                                validators=[RegexValidator(r'^[\W{2}\w+\d{3}.@+-]+$', message=
                                                           'Password Must start with two(2)'
                                                           'Capital Letters,Contain at least three(3) '
                                                           'Numbers and contain at least '
                                                           'two(2) Symbols',), ],
                                )

    def __str__(self):
        return self.email


