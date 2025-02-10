from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ingredients, MenuItems, ItemRequirements, Purchases
from .forms import PurchaseCreateForm, MenuItemsCreateForm, IngredientsCreateForm, ItemRequirementsCreateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render (request, "inventory_tracker/home.html")


class SignUpView(CreateView):
   form_class=UserCreationForm
   success_url = reverse_lazy("login")
   template_name = "registration/signup.html"

class IngredientsList(LoginRequiredMixin, ListView):
    model = Ingredients
    template_name = "inventory_tracker/ingredients_list.html"

class IngredientsDelete(LoginRequiredMixin, DeleteView):
    model = Ingredients
    template_name = "inventory_tracker/ingredients_delete.html"
    success_url = reverse_lazy("ingredientslist")

class IngredientsCreate(LoginRequiredMixin, CreateView):
  model = Ingredients
  template_name = "inventory_tracker/ingredients_create_form.html"
  form_class = IngredientsCreateForm

class IngredientsUpdate(LoginRequiredMixin, UpdateView):
  model = Ingredients
  template_name = "inventory_tracker/ingredients_update_form.html"
  fields = "__all__"

class MenuItemsList(LoginRequiredMixin, ListView):
    model = MenuItems
    template_name = "inventory_tracker/menu_items_list.html"

class MenuItemsDelete(LoginRequiredMixin, DeleteView):
    model = MenuItems
    template_name = "inventory_tracker/menu_items_delete.html"
    success_url = reverse_lazy("menuitemslist")

class MenuItemsCreate(LoginRequiredMixin, CreateView):
  model = MenuItems
  template_name = "inventory_tracker/menu_items_create_form.html"
  form_class = MenuItemsCreateForm

class ItemRequirementsList(LoginRequiredMixin, ListView):
    model = ItemRequirements
    template_name = "inventory_tracker/item_requirements_list.html"

class ItemRequirementsDelete(LoginRequiredMixin, DeleteView):
    model = ItemRequirements
    template_name = "inventory_tracker/item_requirements_delete.html"
    success_url = reverse_lazy("itemrequirementslist")

class ItemRequirementsCreate(LoginRequiredMixin, CreateView):
  model = ItemRequirements
  template_name = "inventory_tracker/item_requirements_create_form.html"
  form_class = ItemRequirementsCreateForm

class PurchasesList(LoginRequiredMixin, ListView):
    model = Purchases
    template_name = "inventory_tracker/purchases.html"

class PurchasesDelete(LoginRequiredMixin, DeleteView):
    model = Purchases
    template_name = "inventory_tracker/purchases_delete.html"
    success_url = reverse_lazy("purchaseslist")

class PurchasesCreate(LoginRequiredMixin, CreateView):
  model = Purchases
  template_name = "inventory_tracker/purchases_create_form.html"
  form_class = PurchaseCreateForm

@login_required
def ProfitAndLoss (request):
   cost = float(Ingredients.total_quantity())
   revenue = float(Purchases.total_quantity())
   profit = round(revenue - cost, 2)
   context = {"profit":profit}
   return render (request, "inventory_tracker/profit_and_loss.html", context=context)


