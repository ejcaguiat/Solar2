from django.contrib import admin

# Register your models here.
from SolarDB.models import *

admin.site.register(Post)
admin.site.register(User)