from django.shortcuts import render,get_object_or_404,redirect
from . models import *
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.core.exceptions import ObjectDoesNotExist
from shop.models import *
# Create your views here.

def cartdetails(request,tot=0,count=0,ct_items=None):
    try:
        ct=cartlist.objects.get(cart_id=carts_id(request))
        ct_items=items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            tot+=(i.prdt.price*i.qty)
            count+=i.qty
    except ObjectDoesNotExist:
        pass
    return render(request,"cart.html",{'ci':ct_items,'t':tot,'co':count})

def carts_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id

def add_cart(request,product_id):
    prod=products.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cart_id=carts_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=carts_id(request))
        ct.save()
    try:
        c_items=items.objects.get(prdt=prod,cart=ct)
        if c_items.qty < c_items.prdt.stock:
            c_items.qty+=1
        c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(prdt=prod,qty=1,cart=ct)
        c_items.save()
    return redirect('cartdetails')

def min_cart(request,product_id):
    ct=cartlist.objects.get(cart_id=carts_id(request))
    prod=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(prdt=prod,cart=ct)
    if c_items.qty > 1:
        c_items.qty -= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartdetails')

def cart_delete(request,product_id):
    ct = cartlist.objects.get(cart_id=carts_id(request))
    prod = get_object_or_404(products, id=product_id)
    c_items = items.objects.get(prdt=prod, cart=ct)
    c_items.delete()
    return redirect('cartdetails')
