from django.contrib import admin
from . models import *


class CategoryImgInline(admin.TabularInline):
    model = CategoryImg
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]
    inlines = [CategoryImgInline]

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)


class ServiceImgInline(admin.TabularInline):
    model = ServiceImg
    extra = 0


class ServiceComplexTextInline(admin.TabularInline):
    model = ServiceComplexText
    extra = 3


class DocumentsAdminInline(admin.TabularInline):
    model = Documents
    extra = 5


class ServiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]
    inlines = [ServiceImgInline, ServiceComplexTextInline, DocumentsAdminInline]

    class Meta:
        model = Service


admin.site.register(Service, ServiceAdmin)
