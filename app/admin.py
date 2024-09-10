from django.contrib import admin

from app.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko', 'zgloszono','opis')
    list_filter = ('nazwisko', 'zgloszono')
    ordering = ('zgloszono',)
# Register your models here.
