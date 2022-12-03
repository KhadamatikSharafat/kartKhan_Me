from django.contrib import admin

from .models import login, register


@admin.register(register)
class PosRegisterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'family', 'codeMeli','cerated_time','updated_time']
    list_filter = ['id', 'name', 'family', 'codeMeli']
    search_fields = ['id', 'name', 'family', 'codeMeli']


class PosRegisterInlineAdmin(admin.StackedInline):
    model = register
    fields = ['id', 'name', 'family', 'codeMeli']
    extra = 0

@admin.register(login)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','codeMeli']
    list_filter = ['codeMeli']
    search_fields = ['codeMeli']
    inlines = [PosRegisterInlineAdmin]
