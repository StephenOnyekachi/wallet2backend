from django.contrib import admin
from . models import Users, Wallet, W_history, Message, Payment

# Register your models here.
admin.site.register(Users)
admin.site.register(Wallet)
admin.site.register(W_history)
admin.site.register(Message)
admin.site.register(Payment)

