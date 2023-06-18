from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# from django.db.models.signals import post_save, post_delete, pre_delete
# from django.dispatch import receiver

# Create your models here.

# for users
class Users(AbstractUser):
    username = models.CharField(max_length=100, blank=True, null=True, unique=True) # ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    total = models.IntegerField(default=0, null=True)
    bonus = models.IntegerField(default=0, null=True)
    percentage = models.IntegerField(default=0, null=True)
    money = models.IntegerField(default=0, null=True)
    number = models.IntegerField(default=0, null=True)
    pin = models.IntegerField(default=0, null=True)
    picture = models.ImageField(upload_to='pics',)
    block = models.BooleanField(default=False)

    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField()
    gender = models.CharField(max_length=10)
    occupation = models.CharField(max_length=100)

    def __str__(self):
        return self.username


# @ receiver(post_save, sender=User)
# def save_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Users.objects.create(name=instance)

#  for wallets address
class Wallet(models.Model):
    address = models.TextField()
    type = models.CharField(max_length=1000)

    def __str__(self):
        return self.type

# for payment and pacentage
class Payment(models.Model):
    price = models.IntegerField()
    percentage = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return self.price


# for message
class Message(models.Model):
    sender = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    message = models.TextField()
    time = models.DateTimeField(verbose_name="last login", auto_now=True)

    def __str__(self):
        return self.time

# for saving withdrawed history
class W_history(models.Model):
    name = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField(default=0, null=True)
    time = models.DateTimeField(verbose_name="last login", auto_now=True)
    address = models.TextField()

    def __str__(self):
        return self.name




