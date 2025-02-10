from django.contrib import admin
from .models import Ingredients, MenuItems, ItemRequirements, Purchases

#Register your models here.
admin.site.register(Ingredients)
admin.site.register(MenuItems)
admin.site.register(ItemRequirements)
admin.site.register(Purchases)