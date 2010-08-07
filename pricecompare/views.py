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
    order = {}
    
    detail = _get_group_detail(id)
    
    if 'sort' in request.GET:
        field, direction = request.GET['sort'].split(":")
        print direction
        if direction == "ASC":
            order_by = "%s" % field
            order[field] = "DESC"
        else:
            order_by = "-%s" % field
            order[field] = "ASC"
        products = detail['products'].order_by(order_by)
    else:
        products = detail['products'].order_by('price')
        order['source'] = "ASC"
        order['price'] = "DESC"
        
    extra_context = {
        'products': products,
        'cheapest': detail['cheapest'],
        'order': order,
    }
    
    return render_to_response(
        'detail.html',
        extra_context,
        context_instance=RequestContext(request),
    )
    
def viewall(request):
    groups = []
    for g in ProductGroup.objects.all():
        d = _get_group_detail(g.pk)
        groups.append({
            'id': g.pk,
            'name': g.name,
            'products': d['products'].order_by('price'),
            'cheapest': d['cheapest'],
        })
        
    extra_context = {
        'groups': groups,
    }
    
    return render_to_response(
        'viewall.html',
        extra_context,
        context_instance=RequestContext(request),
    )
    
def _get_group_detail(id):
    g = ProductGroup.objects.get(pk=id)
    products = Product.objects.filter(product_group=g)
    candidates = products.filter(got_price=True)

    cheapest = 0

    for i, p in enumerate(candidates):
        if p.price < candidates[cheapest].price:
            cheapest = i

    return {
        'cheapest': candidates[cheapest].pk,
        'products': products,
    }
    
def write_csv(request, id=None):
    response = HttpResponse(mimetype='text/csv')
    if id:
        g = ProductGroup.objects.get(pk=id)
        products = Product.objects.filter(product_group=g).order_by('price')
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % (slugify(g.name))
    else:
        groups = ProductGroup.objects.all()
        products = []
        for g in groups:
            products.extend(Product.objects.filter(product_group=g).order_by('price'))
        response['Content-Disposition'] = 'attachment; filename=allproducts.csv'
    
    writer = csv.writer(response)
    for p in products:
        writer.writerow([p.product_group.name, p.source.name, p.url, floatformat(p.price, 2)])
        
    return response
    
def update(request):
    print request.GET.get('redirect_to', '/')
    if request.GET.get('group_id', None):
        call_command('getprices', request.GET.get('group_id'))
    else:
        call_command('getprices')
    return HttpResponseRedirect(request.GET.get('redirect_to', '/'))