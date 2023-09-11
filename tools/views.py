from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_http_methods
import datetime


# Create your views here.
@require_http_methods(["GET"])
def index(request):
    context = {}
    urls = [
        {"title":"homeassistant","link":'http://www.baidu.com'},
        {"title":"photo","link":'http://www.baidu.com'},
        {"title":"","link":'http://www.baidu.com'}
    ]
    context["urls"] = urls

    return render(request,"index.html", context)