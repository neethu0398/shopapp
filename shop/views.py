from django.shortcuts import render,get_object_or_404
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.

def homepage(request,c_slug=None):
    c_page=None
    pdt=None
    crt=None
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        pdt=products.objects.filter(category=c_page,available=True)
    else:
        crt=categ.objects.all()
        pdt=products.objects.all().filter(available=True)
        paginator=Paginator(pdt,6)
        try:
            page=int(request.GET.get('page','1'))
        except:
            page=1
        try:
            product=paginator.page(page)
        except(EmptyPage,InvalidPage):
            product=paginator.page(paginator.num_pages)
    return render(request,"index.html",{'pdt':product,'crt':crt})

def prodetails(request,c_slug,product_slug):
    try:
        prod=products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,"item.html",{'prod':prod})

def searching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=products.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    return render(request,"search.html",{'qr':query,'pdt':prod})