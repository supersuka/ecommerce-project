from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:category_slag>', views.home, name='products_by_category'),
    path('product/', views.product, name='product'),

]
