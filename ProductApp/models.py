from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=250)
    price = models.FloatField()
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, related_name='products')

    class Meta:
        verbose_name = ('Продукт')
        verbose_name_plural = ('Продукты')

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    class Meta:
        verbose_name = ('Категория')
        verbose_name_plural = ('Категории')

    def __str__(self):
        return self.name


