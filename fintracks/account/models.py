
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    GENDER_TYPE = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    gender_type = models.CharField(max_length=100, blank=False, null=False, choices=GENDER_TYPE)
    college = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)
    last_login = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-last_login']
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        

class Account(models.Model):
    ACCOUNT_TYPE = (
        ('robinhood', 'Robinhood'),
        ('webull', 'Webull'),
        ('e*trade', 'E*Trade'),
        ('TD Ameritrade', 'TD Ameritrade'),
        ('charles schwab', 'Charles Schwab'),
        ('fidelity', 'Fidelity'),
    )
    INVESTMENT_CLASS = (
        ('savings', 'Savings'),
        ('stocks', 'Stocks'),
        ('bonds', 'Bonds'),
        ('crypto', 'Crypto'),
    )
    account_owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=100, blank=False, null=False)
    account_type = models.CharField(max_length=100, choices=ACCOUNT_TYPE, blank=False, null=False)
    investment_class = models.CharField(max_length=100, choices=INVESTMENT_CLASS, blank=False, null=False)
    balance = models.IntegerField( blank=False, null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.account_name
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'






    
    
    


    
