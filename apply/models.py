from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None, verbose_name=u'Имя')
    phone = models.CharField(max_length=24, blank=True, null=True, default=None, verbose_name=u'Телефон')
    type = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name=u'Тип заявки')
    text = models.CharField(max_length=1024, blank=True, null=True, default=None, verbose_name=u'Комментарий')
    is_processed = models.BooleanField(default=False, verbose_name=u'Обработана?')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=u'Была оставлена')

    def __str__(self):
        return '%s - %s' % (self.name, self.phone)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
