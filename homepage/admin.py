from django.contrib import admin
from .models import option
from .models import UserDetails

admin.site.register(option)
admin.site.register(UserDetails)