from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('USER', 'کاربر عادی'),
        ('TEACHER', 'مدرس'),
        ('SUPPORT', 'پشتیبان سایت'),
        ('ADMIN','مدیر')
    ]

    full_name = models.CharField(max_length=150, verbose_name='نام کامل')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='USER', verbose_name='نقش کاربر')
    activation_code = models.CharField(max_length=100,null=True,blank=True,verbose_name='کد فعالسازی')
    phone = models.CharField(max_length=15, null=True, blank=True,verbose_name='شماره تلفن')

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        # هر وقت کاربر ذخیره شد، username = email
        if self.email:
            self.username = self.email
        super().save(*args, **kwargs)
