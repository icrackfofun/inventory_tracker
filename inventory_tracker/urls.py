from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("ingredients/", views.IngredientsList.as_view(), name='ingredientslist'),
    path("menuitems/", views.MenuItemsList.as_view(), name="menuitemslist"),
    path("itemrequirements/", views.ItemRequirementsList.as_view(), name="itemrequirementslist"),
    path("purchases/", views.PurchasesList.as_view(), name="purchaseslist"),
    path("profit&loss/", views.ProfitAndLoss, name="profitandloss"),
    path("ingredients/delete/<pk>", views.IngredientsDelete.as_view(), name='ingredientsdelete'),
    path("itemrequirements/delete/<pk>", views.ItemRequirementsDelete.as_view(), name='itemrequirementsdelete'),
    path("menuitems/delete/<pk>", views.MenuItemsDelete.as_view(), name='menuitemsdelete'),
    path("purchases/delete/<pk>", views.PurchasesDelete.as_view(), name="purchasesdelete"),    
    path("purchases/add/", views.PurchasesCreate.as_view(), name="purchasescreate"),
    path("menuitems/add/", views.MenuItemsCreate.as_view(), name="menuitemscreate"),
    path("itemrequirements/add/", views.ItemRequirementsCreate.as_view(), name="itemrequirementscreate"),
    path("ingredients/add/", views.IngredientsCreate.as_view(), name="ingredientscreate"),
    path("ingredients/update/<pk>", views.IngredientsUpdate.as_view(), name="ingredientsupdate"),
]