from django.db import models
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField

APPLICATION_NAME = _('Услуги')


class Category(models.Model):
    page_title = models.CharField(max_length=70, blank=True, null=True, default=None, verbose_name=u"Заголовок в браузере")
    name = models.CharField(max_length=70, blank=True, null=True, default=None, verbose_name=u"Название категории")
    url_name = models.CharField(max_length=70, blank=True, null=True, default=None, verbose_name=u"URL страницы в адресной строке")

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Категория услуг'
        verbose_name_plural = 'Категории услуг'


class CategoryImg(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/img/categories')

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Фото категории услуг'
        verbose_name_plural = 'Фото категорий услуг'


class Service(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True, default=None, on_delete=models.CASCADE,
                                 verbose_name=u"Категория")
    page_title = models.CharField(max_length=70, blank=True, null=True, default=None,
                                  verbose_name=u"Заголовок в браузере")
    meta_tags = models.TextField(max_length=256, blank=True, null=True, default=None,
                                 verbose_name=u"Мета теги (для CEO)")
    name = models.CharField(max_length=70, blank=True, null=True, default=None, verbose_name=u"Название услуги")
    block1_header = HTMLField(default=None, verbose_name=u"Заголовок первого блока")
    block2_header = HTMLField(default=None, verbose_name=u"Заголовок второго блока")
    block2_text = HTMLField(default=None, verbose_name=u"Текст второго блока")
    block3_header = HTMLField(default=None, verbose_name=u"Заголовок третьего блока")
    price = models.CharField(max_length=20, blank=True, null=True, default=None, verbose_name=u"Цена")
    price_descriptor = HTMLField(default=None, verbose_name=u"Постскриптор в блоке цены")
    url_name = models.CharField(max_length=70, blank=True, null=True, default=None,
                                verbose_name=u"URL страницы в адресной строке")

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class ServiceImg(models.Model):
    service = models.ForeignKey(Service, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/img/categories', default=None)

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Фото услуги'
        verbose_name_plural = 'Фото услуг'


class ServiceComplexText(models.Model):
    service = models.ForeignKey(Service, blank=True, null=True, default=None, on_delete=models.CASCADE)
    text = HTMLField()

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Комплекс услуг'
        verbose_name_plural = 'Комплекс услуг'


class Documents(models.Model):
    service = models.ForeignKey(Service, blank=True, null=True, default=None, on_delete=models.CASCADE)
    text = HTMLField()

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Пакет документов'
        verbose_name_plural = 'Пакет документов'
