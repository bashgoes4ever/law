from django.http import JsonResponse
from .models import Order


def apply(request):
    r = request.POST
    if len(r) != 0:
        name = r.get("name")
        phone = r.get("phone")
        text = ''
        if 'text' in r:
            text = r.get("text")
        type = r.get("type")
        Order.objects.create(name=name, phone=phone, type=type, text=text)

    return JsonResponse(r)
