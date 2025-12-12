from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Haftakun, Kurs, Oquvchi

admin.site.register(Haftakun)
admin.site.register(Kurs)
admin.site.register(Oquvchi)

