from django.db import models
from django.db.models import Sum, F

# Create your models here.
class Ingredients (models.Model):
    ingredient = models.CharField(max_length=200)
    quantity = models.IntegerField(default = 0)
    price_per_unit = models.FloatField()

    class Meta:
        ordering = ["ingredient"]

    def __str__(self):
        return str(self.ingredient)
    
    def get_absolute_url(self):
        return "/ingredients/"
    
    @classmethod
    def total_quantity(cls):
        revenue = cls.objects.aggregate(total=Sum(F('price_per_unit')*F('quantity')))['total'] or 0
        return revenue
    
class MenuItems (models.Model):
    item = models.CharField(max_length=200, null=False)
    price = models.FloatField()

    class Meta:
        ordering = ["item"]

    def __str__(self):
        return str(self.item)
    
    def get_absolute_url(self):
        return "/menuitems/"
    
class ItemRequirements (models.Model):
    item = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete = models.RESTRICT)
    quantity = models.IntegerField(default=1)

    class Meta:
        ordering = ["item"]

    def __str__(self):
        return str(self.item)
    
    def get_absolute_url(self):
        return "/itemrequirements/"

class Purchases (models.Model):
    item = models.ForeignKey(MenuItems, on_delete=models.RESTRICT)
    date = models.DateField()
    time = models.TimeField()
    price = models.FloatField()

    class Meta:
        ordering = ["time"]

    def __str__(self):
        return str(self.item)
    
    def get_absolute_url(self):
        return "/purchases/"
    
    @classmethod
    def total_quantity(cls):
        revenue = cls.objects.aggregate(total=Sum(F('price')))['total'] or 0
        return revenue