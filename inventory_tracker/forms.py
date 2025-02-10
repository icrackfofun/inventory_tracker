from django import forms
from .models import Ingredients, MenuItems, ItemRequirements, Purchases

class PurchaseCreateForm(forms.ModelForm):
  class Meta:
    model = Purchases
    fields = "__all__"

class MenuItemsCreateForm(forms.ModelForm):
  class Meta:
    model = MenuItems
    fields = "__all__"

class IngredientsCreateForm(forms.ModelForm):
  class Meta:
    model = Ingredients
    fields = "__all__"

class ItemRequirementsCreateForm(forms.ModelForm):
  class Meta:
    model = ItemRequirements
    fields = "__all__"

