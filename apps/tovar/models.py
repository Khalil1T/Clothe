from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=255,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Product(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=255,
    )
    description = models.TextField(
        _('Description'),
    )
    price = models.PositiveIntegerField(
        _('Price'),
        default=0,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name=_('Category'),
    )
    brand = models.CharField(
        _('Brand'),
        max_length=255,
    )
    model = models.CharField(
        _('Model'),
        max_length=255,
    )
    quantity = models.PositiveIntegerField(
        _('Quantity'),
        default=0,
    )

    image = models.ImageField(
        default='1.png',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductSpecifications(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='specifications',
        verbose_name=_('Product'),
    )
    name = models.CharField(
        _('Name'),
        max_length=255,
    )
    value = models.CharField(
        _('Value'),
        max_length=255,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product specification')
        verbose_name_plural = _('Product specifications')
