import csv

from django.core.management import call_command
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.template.defaultfilters import floatformat, slugify

from pricecompare.models import *

def index(request):
    extra_context = {
        'groups': ProductGroup.objects.order_by('name')
    }
    
    return render_to_response(
        'index.html',
        extra_context,
        context_instance=RequestContext(request),
    )
    
def detail(request, id):
    g = ProductGroup.objects.get(pk=id)
    order = {}
    if 'sort' in request.GET:
        field, direction = request.GET['sort'].split(":")
        print direction
        if direction == "ASC":
            order_by = "%s" % field
            order[field] = "DESC"
        else:
            order_by = "-%s" % field
            order[field] = "ASC"
        products = Product.objects.filter(product_group=g).order_by(order_by)
    else:
        products = Product.objects.filter(product_group=g).order_by('price')
        order['source'] = "DESC"
        order['price'] = "DESC"
        
    candidates = products.filter(got_price=True)
        
    cheapest = 0
    
    for i, p in enumerate(candidates):
        if p.price < candidates[cheapest].price:
            cheapest = i
        
    extra_context = {
        'cheapest': candidates[cheapest].pk,
        'products': products,
        'order': order,
    }
    
    return render_to_response(
        'detail.html',
        extra_context,
        context_instance=RequestContext(request),
    )
    
def detail_csv(request, id):
    g = ProductGroup.objects.get(pk=id)
    
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % (slugify(g.name))
    
    writer = csv.writer(response)
    products = Product.objects.filter(product_group=g).order_by('price')
    for p in products:
        writer.writerow([p.product_group.name, p.source.name, p.url, floatformat(p.price, 2)])
        
    return response
    
def update(request):
    print request.GET.get('redirect_to', '/')
    call_command('getprices')
    return HttpResponseRedirect(request.GET.get('redirect_to', '/'))