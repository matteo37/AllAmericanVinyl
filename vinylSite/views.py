
from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def about_us(request):
	return render(request,"about.html")

def products(request):
	return render(request,"products.html")

def contact(request):
	return render(request,"contact.html")
# Create your views here.
