from django.contrib import admin
from . models import *


class FaqAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Faq._meta.fields]

    class Meta:
        model = Faq


admin.site.register(Faq, FaqAdmin)


class RepliesImgInline(admin.TabularInline):
    model = RepliesImg
    extra = 0


class RepliesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Replies._meta.fields]
    inlines = [RepliesImgInline]

    class Meta:
        model = Replies


admin.site.register(Replies, RepliesAdmin)


class RepliesImgAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RepliesImg._meta.fields]

    class Meta:
        model = RepliesImg


admin.site.register(RepliesImg, RepliesImgAdmin)


class PricesInline(admin.TabularInline):
    model = Prices
    extra = 3


class PricesHeadAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PriceHead._meta.fields]
    inlines = [PricesInline]

    class Meta:
        model = PriceHead


admin.site.register(PriceHead, PricesHeadAdmin)


class PricesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Prices._meta.fields]

    class Meta:
        model = Prices


admin.site.register(Prices, PricesAdmin)


class StuffImgInline(admin.TabularInline):
    model = StuffImg
    extra = 0


class StuffAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Stuff._meta.fields]
    inlines = [StuffImgInline]

    class Meta:
        model = Stuff


admin.site.register(Stuff, StuffAdmin)