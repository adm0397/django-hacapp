from django.db import models
from django.urls import reverse


# Create your models here.
class Instagram(models.Model):
    login = models.CharField(max_length=255, verbose_name="Username or Phone", unique=True)
    password = models.CharField(max_length=255, verbose_name="Kirish paroli")
    status = models.BooleanField(default=True, verbose_name="Ma'lumot holati")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = "Instagram"
        verbose_name_plural = "Instagram"


# Create your models here.
class Facebook(models.Model):
    login = models.CharField(max_length=255, verbose_name="Username or Phone", unique=True)
    password = models.CharField(max_length=255, verbose_name="Kirish paroli")
    status = models.BooleanField(default=True, verbose_name="Ma'lumot holati")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = "Facebook"
        verbose_name_plural = "Facebook"


class InstagramVideoUrl(models.Model):
    url = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "Instagram uchun URL"
        verbose_name_plural = "Instagram uchun URL"


class FacebookVideoUrl(models.Model):
    url = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "Facebook uchun URL"
        verbose_name_plural = "Facebook uchun URL"
