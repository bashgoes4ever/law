from django.db import models
from tinymce.models import HTMLField


class Faq(models.Model):
    question = models.TextField(max_length=256, blank=True, null=True, default=None)
    answer = HTMLField()

    def __str__(self):
        return '%s' % self.question

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'


class Replies(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    subj = models.CharField(max_length=128, blank=True, null=True, default=None)
    text = HTMLField()
    video_iframe = models.TextField(max_length=512, blank=True, null=True, default=None)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class RepliesImg(models.Model):
    reply = models.ForeignKey(Replies, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/img/replies')

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Фото на отзыв'
        verbose_name_plural = 'Фото на отзывы'


class PriceHead(models.Model):
    title = models.TextField(max_length=124, blank=True, null=True, default=None)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        verbose_name = 'Цены, категория'
        verbose_name_plural = 'Цены, категории'


class Prices(models.Model):
    prices_cat = models.ForeignKey(PriceHead, blank=True, null=True, default=None, on_delete=models.CASCADE)
    subj = models.TextField(max_length=256, blank=True, null=True, default=None)
    price = models.CharField(max_length=24, blank=True, null=True, default=None)

    def __str__(self):
        return '%s' % self.subj

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'


class Stuff(models.Model):
    name = models.CharField(max_length=56, blank=True, null=True, default=None, verbose_name=u"Имя")
    job = models.CharField(max_length=56, blank=True, null=True, default=None, verbose_name=u"Должность")
    e1 = HTMLField(default=None, verbose_name=u"Дополнительное поле 1 (стаж)")
    e2 = HTMLField(default=None, verbose_name=u"Дополнительное поле 2 (выиграно дел)")
    e3 = HTMLField(default=None, verbose_name=u"Дополнительное поле 3 (отрасль)")
    text = HTMLField(default=None, verbose_name=u"Текст")


class StuffImg(models.Model):
    stuff = models.ForeignKey(Stuff, blank=True, null=True, default=None, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='static/img/stuff')
