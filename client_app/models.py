from django.db import models

from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Restoran(models.Model):
    name = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to='image/restoran/' ,default='image/restoran/default.png', null=True)
    tables = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to='image/restoran/' ,default='image/restoran/default.png', null=True)
    restoran = models.ForeignKey(Restoran, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    STATUS_PORTION = 1
    STATUS_PIECES = 2
    STATUS_LITER = 3
    STATUS_CUP =4

    STATUS_CHOICES = (
        (STATUS_PORTION, _('порция')),
        (STATUS_PIECES, _('штук')),
        (STATUS_LITER, _('литр')),
        (STATUS_CUP, _('стакан')),
    )

    name = models.CharField(max_length=150, blank=True)
    body = models.TextField()
    status = models.SmallIntegerField(choices=STATUS_CHOICES, blank=True)
    unit = models.SmallIntegerField(blank=True)
    price = models.IntegerField(blank=True)
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/restoran/' ,default='image/restoran/default.png', null=True)

    def __str__(self):
        return self.name

class ImageProduct(models.Model):
    image = models.ImageField(upload_to='image/restoran/' ,default='image/restoran/default.png', null=True)
    product_image = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.url

class Table(models.Model):
    STATUS_GREEN = 1
    STATUS_YELLOW = 2
    STATUS_RED = 3
    STATUS_RED_YELLOW = 4
    STATUS_BLUE = 5

    STATUS_CHOICES = (
        (STATUS_GREEN, _('Green')), 
        (STATUS_YELLOW, _('Yellow')), 
        (STATUS_RED, _('Red')), 
        (STATUS_RED_YELLOW, _('Red Yellow')), 
        (STATUS_BLUE, _('Blue')),
    )
    number = models.SmallIntegerField(blank=True)
    restoran = models.ForeignKey(Restoran, blank=True, on_delete=models.CASCADE)
    color = models.SmallIntegerField(choices=STATUS_CHOICES, blank=True, default=1)

    def __str__(self):
        return str(self.number)

class TableProducts(models.Model):
    STATUS_PROCCES = 1
    STATUS_DONE = 2
    STATUS_CHOICES = (
        (STATUS_PROCCES, _('Жасалуда')),
        (STATUS_DONE, _('Дайын')),
    )
    table = models.IntegerField(blank=True)
    product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, blank=True, default=1)
    unit = models.SmallIntegerField(blank=True)

    def __str__(self):
        return str(self.table.number)
        