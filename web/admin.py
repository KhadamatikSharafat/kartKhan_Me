from django.contrib import admin

from .models import login , register

@admin.register(login)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','codeMeli']
    list_filter = ['codeMeli']
    search_fields = ['codeMeli']

@admin.register(register)
class PosRegisterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'family', 'codeMeli']
    list_filter = ['id', 'name', 'family', 'codeMeli']
    search_fields = ['id', 'name', 'family', 'codeMeli']
