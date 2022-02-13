from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField('Название', max_length=64)
    price = models.IntegerField('Цена')
    image = models.ImageField('Изображение')
    release_date = models.DateField('Дата выпуска')
    lte_exists = models.BooleanField('Поддержка LTE')
    slug = models.SlugField(max_length=64)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
