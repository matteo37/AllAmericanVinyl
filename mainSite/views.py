from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader, RequestContext
def index(request):
    return render(request,"mainSite/home.html")
