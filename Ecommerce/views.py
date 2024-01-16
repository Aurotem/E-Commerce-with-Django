from django.shortcuts import render
import requests



def index(request):
    response = requests.get('https://api.escuelajs.co/api/v1/products')
    data = response.json()
    context = {
        'products':data
    }
    return render(request, 'index.html',context)