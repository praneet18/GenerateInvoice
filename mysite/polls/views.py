from django.shortcuts import render,  redirect
from django.http import HttpResponse, JsonResponse
from .modules.jsonModule import createJson
from .modules.utils import uniqueid, validateUser
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
from .models import Product
import json
import csv
import io

from django.contrib import messages


def index(request):
    return render(request, "index.html", {'oderid': uniqueid()})


def autocomplete(request):
    if 'term' in request.GET:
        data = list()
        for i in Product.objects.filter(product_name__contains=request.GET.get('term'), product_available=True):
            f = {
                'label': i.product_name,
                'value': i.product_name,
                'pdes': i.product_desc,
                'rate': i.product_price,
            }
            data.append(f)
        print(data)
    return JsonResponse(data, safe=False)


def generateinvoice(request):
    print(createJson(request))
    return render(request, "invoice.html", createJson(request))


def profile_upload(request):
    # declaring template
    template = "profile_upload.html"
    data = Product.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, email, address,    phone, profile',
        'profiles': data
    }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')

    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        if int(column[4]) == 1:
            product_available = True
        else:
            product_available = False
        print(product_available)
        _, created = Product.objects.update_or_create(
            product_name=column[0],
            product_desc=column[1],
            publish_date=column[2],
            product_price=column[3],
            product_available=product_available,
            product_quantity=column[5],
            product_mrp=column[6],
        )
    context = {}
    return render(request, template, context)


def login_view(request):
    user = ''
    if request.method == "POST":
        validUser = validateUser(request)
        if validUser:
            return redirect('index')
        else:
            user = 'Invalid User'
    return render(request, "login.html", {'user': user})
