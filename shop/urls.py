from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('<slug:c_slug>/',views.homepage,name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>',views.prodetails,name='details'),
    path('search',views.searching,name='search')
]