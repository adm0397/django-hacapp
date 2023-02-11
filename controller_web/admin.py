from .models import Instagram, Facebook, InstagramVideoUrl, FacebookVideoUrl
from django.contrib import admin


# Register your models here.
@admin.register(Instagram)
class InstagramAdmin(admin.ModelAdmin):
    list_display = ('login', 'id', 'password', 'status', 'date')


@admin.register(Facebook)
class FacebookAdmin(admin.ModelAdmin):
    list_display = ('login', 'id', 'password', 'status', 'date')


@admin.register(InstagramVideoUrl)
class InstagramVideoUrlAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'status', 'date')


@admin.register(FacebookVideoUrl)
class FacebookVideoUrlAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'status', 'date')
