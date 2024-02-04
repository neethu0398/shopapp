from django.urls import path
from . import views

urlpatterns=[
    path('cartdetails',views.cartdetails,name='cartdetails'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    path('cartdec/<int:product_id>/',views.min_cart,name='cartdec'),
    path('remove/<int:product_id>/',views.cart_delete,name='remove')
]