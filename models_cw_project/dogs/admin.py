
#importing admin functions

from django.contrib import admin

# Register your models here.

#importing the models to register
from .models import Dogs
from .models import Account

#resgistering models

admin.site.register(Dogs)
admin.site.register(Account)