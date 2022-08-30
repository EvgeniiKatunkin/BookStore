from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    header = "Personal data"
    langs = ["English", "German", "Spanish"]
    user = {"name": "Max", "age": 30}
    addr = ("Kralja Nikole", 23, 45)
    data = {"header": header, "langs": langs, "user": user, "address": addr}
    return render(request, "index.html", context=data)


def products(request, productid):
    category = request.GET.get("cat", "")
    output = "<h2>Product #{0} Category:{1}</h2>".format(productid, category)
    return HttpResponse(output)


def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Max")
    output = "<h2>User</h2><h3>id:{0} " \
             "Name:{1}</h3>".format(id, name)
    return HttpResponse(output)
