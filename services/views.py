from django.shortcuts import render
from services.models import *


def cat(request, url_name):
    services = CategoryImg.objects.all()
    serv = Category.objects.get(url_name=url_name)
    imgs = ServiceImg.objects.filter(service__category__url_name=url_name)
    return render(request, 'site/level2.html', locals())


def service(request, url_name, url):
    services = CategoryImg.objects.all()
    cat = Category.objects.get(url_name=url_name)
    serv = Service.objects.get(url_name=url)
    texts = ServiceComplexText.objects.filter(service__url_name=url)
    documents = Documents.objects.filter(service__url_name=url)
    return render(request, 'site/level3.html', locals())