from django.contrib import admin

from app.models import User,MyAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko', 'zgloszono','opis')
    list_filter = ('nazwisko', 'zgloszono','status')
    ordering = ('zgloszono','status')

@admin.register(MyAdmin)
class MyAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'password')
