import profile
from django.contrib import admin
from .models import Cashbook ,Comment
from account.models import Profile

# Register your models here.
admin.site.register(Cashbook)
admin.site.register(Profile)
admin.site.register(Comment)

