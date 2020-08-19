

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa


import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.staticfiles import finders


def createJson(request):
    names = ('sub_total', 'tax_amount', 'total_amount', 'tax')
    data = {}
    for i in names:

        if i == 'tax':
            data[i] = request.POST.get(i, default='18')
        else:
            data[i] = request.POST.get(i)
    j = []
    names = ('product', 'price', 'qty', 'total')
    print(request.POST.getlist('product'))
    print(request.POST.getlist('price'))
    print(request.POST.getlist('quantity'))
    print(request.POST.getlist('total'))
    print(request.POST)
    for i in zip(request.POST.getlist('product'), request.POST.getlist('price'), request.POST.getlist('quantity'), request.POST.getlist('total')):
        res = dict(zip(names, i))
        j.append(res)
    data['product'] = j
    data['date'] = request.POST.get('date')
    data['customerAddress'] = request.POST.get('customerAddress')
    data['customerName'] = request.POST.get('customerName')
    data['customerContact'] = request.POST.get('customerContact')
    print(data)
    return data
