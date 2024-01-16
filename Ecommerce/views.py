from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import json
import urllib.request



def index(request):
    return render(request, 'index.html')