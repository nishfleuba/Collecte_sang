from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('centreCollecte/',views.centreCollecte,name='centreCollecte'),
    path('donneur/', views.donneur, name='donneur'),
    path('login/', views.login, name='login'),
    path('receveur/',views.receveur,name='receveur'),
  


    # path('login/<int:id>/', views.login_view, name='login'),

]

