from django.shortcuts import render
from main_page.models import *
from services.models import *

def site(request):
    faqs = Faq.objects.all()
    replies = RepliesImg.objects.all()
    prices = PriceHead.objects.all()
    services = CategoryImg.objects.all()
    return render(request, 'site/index.html', locals())


def contacts(request):
    services = CategoryImg.objects.all()
    return render(request, 'site/contacts.html', locals())


def about(request):
    stuff = StuffImg.objects.all()
    services = CategoryImg.objects.all()
    return render(request, 'site/about.html', locals())