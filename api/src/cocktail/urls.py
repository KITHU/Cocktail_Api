from django.urls import path
from .views import (CocktailCreateApiView,
                    CocktailretriveAPiView,
                    CocktailListAPiView)



urlpatterns = [
    path('create/',CocktailCreateApiView.as_view(), name='create_cocktail'),
    path('retrieve/',CocktailretriveAPiView.as_view(), name='retrive_cocktail'),
    path('list/',CocktailListAPiView.as_view(), name='list_cocktail'),
]
