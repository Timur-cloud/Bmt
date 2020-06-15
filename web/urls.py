from django.urls import path
from .views import shop
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('shop/', views.shop, name='shop'),
    path('tovar/', views.tovar, name='tovar'),
    path('partner/', views.partner, name='partner'),
    path('about/', views.about, name='about'),
    path('diplomi/', views.diplomi, name='diplomi'),
    path('innovations/', views.innovations, name='innovations'),
    path('postavshiki/', views.postavshiki, name='postavshiki'),
    path('medkab/', views.medkab, name='medkab'),
    path('sanit/', views.sanit, name='sanit'),
    path('tovar/<int:pk>/', views.tovar.as_view() , name = 'tovar'),
]
