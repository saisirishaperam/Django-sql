from django.contrib import admin
from app1.models import student
# Register your models here.

class Std_admin(admin.ModelAdmin):

    class Meta:

        list_display = ['std_name','std_pin']

admin.site.register(student,Std_admin)
